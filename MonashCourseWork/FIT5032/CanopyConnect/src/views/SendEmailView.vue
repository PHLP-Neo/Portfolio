<template>
    <div class="container mt-5">
        <h1>Send Volunteer Information</h1>
        <p>
            Send announcements to selected user groups, or email a volunteer position’s details as an attachment to an individual recipient.
        </p>

        <div v-if="loadError" class="alert alert-danger" role="alert">
            {{ loadError }}
        </div>

        <div v-if="successMessage" class="alert alert-success" role="status">
            {{ successMessage }}
        </div>

        <div v-if="errorMessage" class="alert alert-danger" role="alert">
            {{ errorMessage }}
        </div>

        <form @submit.prevent="submitEmail">
            <div>
                <h2 class="h5">Group Announcement</h2>

                <div class="mb-3">
                    <label for="announcement-subject" class="form-label">
                        Subject
                    </label>
                    <input
                        id="announcement-subject"
                        v-model="announcementSubject"
                        type="text"
                        class="form-control"
                        maxlength="150"
                        :disabled="emailControlsDisabled"
                    >
                </div>

                <div class="mb-3">
                    <label for="announcement-message" class="form-label">
                        Message
                    </label>
                    <textarea
                        id="announcement-message"
                        v-model="announcementMessage"
                        class="form-control"
                        rows="5"
                        maxlength="5000"
                        :disabled="emailControlsDisabled"
                    ></textarea>
                </div>

                <div class="mb-3">
                    <h2 class="h6">Recipient groups</h2>

                    <div class="mb-3">
                        <label for="announcement-position" class="form-label">
                            Include a volunteer position — optional
                        </label>

                        <select
                            id="announcement-position"
                            v-model="announcementPositionId"
                            class="form-select"
                            :disabled="emailControlsDisabled"
                        >
                            <option value="">General announcement — no position</option>

                            <option
                                v-for="position in availablePositions"
                                :key="position.id"
                                :value="position.id"
                            >
                                {{ position.title }} — {{ position.location }}
                            </option>
                        </select>

                        <p class="small mt-2">
                            When selected, the position’s details are included in the email body.
                        </p>
                    </div>


                    <div
                        v-for="group in recipientGroups"
                        :key="group.value"
                        class="form-check mb-2"
                    >
                        <input
                            :id="'email-group-' + group.value"
                            v-model="selectedRoles"
                            :value="group.value"
                            type="checkbox"
                            class="form-check-input"
                            :disabled="emailControlsDisabled"
                        >

                        <label
                            :for="'email-group-' + group.value"
                            class="form-check-label"
                        >
                            {{ group.label }}
                        </label>
                    </div>

                    <p class="small mt-2" role="status">
                        {{ selectedRoles.length }} group(s) selected.
                    </p>

                    <button
                        type="button"
                        class="btn btn-success"
                        :disabled="emailControlsDisabled || selectedRoles.length === 0"
                        @click="submitBulkEmail"
                    >
                        {{ isSending ? 'Sending…' : 'Send Announcement to Groups' }}
                    </button>

                    <p class="small mt-2">
                        Sends a separate email to every user in the selected groups.
                        Duplicate email addresses receive one email.
                        Maximum 20 unique recipients per request.
                    </p>
                </div>

                <h2 class="h5 mt-4">Send Position with Attachment</h2>

                <div class="mb-3">
                    <label for="email-position" class="form-label">
                        Position
                    </label>
                    <select
                        id="email-position"
                        v-model="selectedPositionId"
                        class="form-select"
                        required
                        :disabled="emailControlsDisabled"
                    >
                        <option disabled value="">Select a position</option>
                        <option
                            v-for="position in availablePositions"
                            :key="position.id"
                            :value="position.id"
                        >
                            {{ position.title }} — {{ position.location }}
                        </option>
                    </select>
                </div>

                <div class="mb-3">
                    <label for="recipient-email" class="form-label">
                        Recipient email — registered or external
                    </label>
                    <input
                        id="recipient-email"
                        v-model="recipientEmail"
                        type="email"
                        class="form-control"
                        maxlength="254"
                        required
                        :disabled="emailControlsDisabled"
                    >
                </div>

                <button
                    type="submit"
                    class="btn btn-primary"
                    :disabled="emailControlsDisabled || availablePositions.length === 0"
                >
                    <span v-if="isSending">Sending…</span>
                    <span v-else>Send Email with Attachment</span>
                </button>
            </div>
        </form>
    </div>
</template>

<script setup>
    import { ref, onMounted, computed } from 'vue';
    import { positions, loadPositions } from '../positions.js';
    import { httpsCallable } from 'firebase/functions';
    import { functions } from '../firebase/init.js';
    
    const selectedPositionId = ref(''); //Individual attachment’s position
    const recipientEmail = ref(''); //Individual recipient
    const selectedRoles = ref([]); //Groups selected for an announcement
    const announcementSubject = ref(''); //Announcement content
    const announcementMessage = ref(''); //Announcement content
    const announcementPositionId = ref(''); //Optional position included in the announcement
    const availablePositions = ref([]); //Unarchived jobs available in both dropdowns
    const successMessage = ref(''); //Sending feedback
    const errorMessage = ref(''); //Sending feedback
    const loadError = ref(''); //Initial loading failure
    const isLoading = ref(true); //Busy states
    const isSending = ref(false); //Busy states

    const emailControlsDisabled = computed(() => {
        return isLoading.value || isSending.value || loadError.value !== '';
    });

    const recipientGroups = [
        { value: 'viewer', label: 'Viewers — regular users' },
        { value: 'editor', label: 'Editors' },
        { value: 'admin', label: 'Administrators' },
    ];

    const sendPositionEmail = httpsCallable(
        functions,
        'sendPositionEmail'
    );

    onMounted(async () => {
        try {
            await loadPositions();

            availablePositions.value = positions.value.filter((position) => {
                return !position.archived;
            });
        } catch (error) {
            console.error('Loading email form failed:', error);
            loadError.value = 'Could not load positions.';
        } finally {
            isLoading.value = false;
        }
    });

    const submitEmail = async () => {
        if (isSending.value) return;

        successMessage.value = '';
        errorMessage.value = '';

        if (!selectedPositionId.value || !recipientEmail.value.trim()) {
            errorMessage.value = 'Select a position and enter a recipient email.';
            return;
        }

        isSending.value = true;

        try {
            await sendPositionEmail({
                positionId: selectedPositionId.value,
                recipientEmail: recipientEmail.value.trim(),
            });

            successMessage.value = 'Email accepted for delivery.';
        } catch (error) {
            console.error('Sending email failed:', error);
            errorMessage.value = error.message;
        } finally {
            isSending.value = false;
        }
    };

    const submitBulkEmail = async () => {
        if (isSending.value) return;

        successMessage.value = '';
        errorMessage.value = '';

        if (
            !announcementSubject.value.trim() ||
            !announcementMessage.value.trim()
        ) {
            errorMessage.value = 'Enter an announcement subject and message.';
            return;
        }

        if (selectedRoles.value.length === 0) {
            errorMessage.value = 'Select at least one recipient group.';
            return;
        }

        isSending.value = true;

        try {
            const result = await sendPositionEmail({
                selectedRoles: selectedRoles.value,
                subject: announcementSubject.value.trim(),
                message: announcementMessage.value.trim(),
                positionId: announcementPositionId.value,
            });

            successMessage.value = result.data.acceptedCount + ' email(s) accepted for delivery.';

            selectedRoles.value = [];
        } catch (error) {
            console.error('Sending bulk email failed:', error);
            errorMessage.value = error.message;
        } finally {
            isSending.value = false;
        }
    };
</script>