const { onRequest, onCall, HttpsError } = require('firebase-functions/https');
const admin = require('firebase-admin');
const { defineSecret } = require('firebase-functions/params');
const { Resend } = require('resend');

const resendApiKey = defineSecret('RESEND_API_KEY');

admin.initializeApp();

exports.countPositions = onRequest(
    {
        region: 'australia-southeast2',
        cors: true,
        maxInstances: 1,
    },
    async (req, res) => {
        try {
            const snapshot = await admin.firestore()
                .collection('positions')
                .get();

            const availablePositions = snapshot.docs.filter((document) => {
                return document.data().archived !== true;
            });

            res.json({ count: availablePositions.length });
        } catch (error) {
            console.error('Counting positions failed:', error);
            res.status(500).json({
                error: 'Could not count positions.',
            });
        }
    }
);

exports.getPositions = onRequest(
    {
        region: 'australia-southeast2',
        cors: true,
        maxInstances: 1,
    },
    async (req, res) => {
        if (req.method !== 'GET') {
            res.set('Allow', 'GET');
            res.status(405).json({
                error: 'Use GET to retrieve positions.',
            });
            return;
        }

        try {
            const snapshot = await admin.firestore()
                .collection('positions')
                .get();

            const availablePositions = snapshot.docs
                .filter((document) => {
                    return document.data().archived !== true;
                })
                .map((document) => {
                    const position = document.data();

                    return {
                        id: document.id,
                        title: position.title,
                        location: position.location,
                        description: position.description,
                    };
                });

            res.json({
                count: availablePositions.length,
                positions: availablePositions,
            });
        } catch (error) {
            console.error('Retrieving positions failed:', error);
            res.status(500).json({
                error: 'Could not retrieve positions.',
            });
        }
    }
);

exports.sendPositionEmail = onCall(
    {
        region: 'australia-southeast2',
        secrets: [resendApiKey],
        maxInstances: 1,
    },
    async (request) => {
        if (!request.auth) {
            throw new HttpsError('unauthenticated', 'Please log in.');
        }

        const input = request.data || {};
        const positionId = input.positionId;
        const recipientEmail = input.recipientEmail;
        const selectedRoles = input.selectedRoles;
        const subject = input.subject;
        const message = input.message;
        const isBulk = selectedRoles !== undefined;
        const hasPosition = (positionId !== undefined && positionId !== '');

        if (
            (!isBulk || hasPosition) &&
            (
                typeof positionId !== 'string' ||
                !positionId ||
                positionId.length > 128 ||
                positionId.includes('/')
            )
        ) {
            throw new HttpsError(
                'invalid-argument', 'Select a valid position.'
            );
        }

        if (isBulk) {
            const allowedRoles = ['viewer', 'editor', 'admin'];

            if (
                !Array.isArray(selectedRoles) ||
                selectedRoles.length === 0 ||
                selectedRoles.length > 3 ||
                selectedRoles.some((role) => {
                    return !allowedRoles.includes(role);
                })
            ) {
                throw new HttpsError(
                    'invalid-argument',
                    'Select at least one valid recipient group.'
                );
            }
        } else {
            if (
                typeof recipientEmail !== 'string' ||
                recipientEmail.length > 254 ||
                !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(recipientEmail)
            ) {
                throw new HttpsError(
                    'invalid-argument',
                    'Enter a valid recipient email.'
                );
            }
        }

        try {
            const profile = await admin.firestore()
                .collection('users')
                .doc(request.auth.uid)
                .get();

            if (!profile.exists || profile.data().role !== 'admin') {
                throw new HttpsError(
                    'permission-denied', 'Administrator access required.'
                );
            }

            if (
                isBulk &&
                (
                    typeof subject !== 'string' ||
                    !subject.trim() ||
                    subject.length > 150 ||
                    /[\r\n]/.test(subject) ||
                    typeof message !== 'string' ||
                    !message.trim() ||
                    message.length > 5000
                )
            ) {
                throw new HttpsError(
                    'invalid-argument',
                    'Enter a subject of up to 150 characters and a message of up to 5000 characters.'
                );
            }

            

            const resend = new Resend(resendApiKey.value());

            let summary = '';

            if (!isBulk || hasPosition) {
                const snapshot = await admin.firestore()
                    .collection('positions')
                    .doc(positionId)
                    .get();

                if (!snapshot.exists) {
                    throw new HttpsError('not-found', 'Position not found.');
                }

                const position = snapshot.data();

                if (position.archived === true) {
                    throw new HttpsError(
                        'failed-precondition',
                        'This position is archived and no longer available.'
                    );
                }

                summary =
                    'Position: ' + position.title + '\n' +
                    'Location: ' + position.location + '\n\n' +
                    position.description;
            }

            if (isBulk) {

                const usersSnapshot = await admin.firestore()
                    .collection('users')
                    .where('role', 'in', selectedRoles)
                    .get();

                const recipientEmails = new Set();

                for (const userDocument of usersSnapshot.docs) {
                    const email = userDocument.data().email;

                    if (
                        typeof email !== 'string' ||
                        email.length > 254 ||
                        !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)
                    ) {
                        throw new HttpsError(
                            'failed-precondition',
                            'A user in the selected groups has an invalid email address.'
                        );
                    }

                    recipientEmails.add(email.trim().toLowerCase());
                }

                if (recipientEmails.size === 0) {
                    throw new HttpsError(
                        'failed-precondition',
                        'No recipients were found in the selected groups.'
                    );
                }

                if (recipientEmails.size > 20) {
                    throw new HttpsError(
                        'failed-precondition',
                        'The selected groups exceed the limit of 20 unique recipients.'
                    );
                }

                const messages = Array.from(recipientEmails).map((email) => {
                    return {
                        from: 'Canopy Connect <canopy@send.phlpneo.com>',
                        to: email,
                        subject: subject.trim(),
                        text: 'Canopy Connect\n\n' + message.trim() + (summary ? '\n\n' + summary : ''),
                    };
                });

                const result = await resend.batch.send(messages);

                if (result.error) {
                    console.error('Resend rejected the batch:', result.error);
                    throw new HttpsError(
                        'internal',
                        'The email provider could not accept the bulk emails.'
                    );
                }

                return { acceptedCount: result.data.data.length };
            }

            const result = await resend.emails.send({
                from: 'Canopy Connect <canopy@send.phlpneo.com>',
                to: recipientEmail,
                subject: 'Canopy Connect — Volunteer Opportunity',
                text: 'Please find the volunteer opportunity details attached.',
                attachments: [{
                    filename: 'position-information.txt',
                    content: Buffer.from(
                        'Canopy Connect\n\n' + summary,
                        'utf8'
                    ).toString('base64'),
                }],
            });

            if (result.error) {
                console.error('Resend rejected the email:', result.error);
                throw new HttpsError(
                    'internal', 'The email provider could not accept the email.'
                );
            }

            return { emailId: result.data.id };
        } catch (error) {
            if (error instanceof HttpsError) throw error;

            console.error('Sending position email failed:', error);
            throw new HttpsError('internal', 'Could not send the email.');
        }
    }
);

