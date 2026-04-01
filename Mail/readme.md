# CS50 Web - Mail Client

![Screenshot or demo GIF](screenshot.png)

**Single-page email SPA** with Django API + vanilla JS: inbox/sent/archive, compose/reply/archive.

## Features Implemented
- **Mailboxes**: Load via GET `/emails/{inbox|sent|archive}` (JSON: sender/subject/timestamp/read/archived).
- **Compose/Send**: POST `/emails` with recipients/subject/body; clear form on switch.
- **View/Reply**: GET `/emails/ID`, mark read (PUT), prefills "Re: " + quoted body.
- **Archive**: Toggle archived (PUT), refresh inbox.
- Tech: Fetch API, view toggles (no reloads), read styling.[file:78]

**What I Learned**: Async JS fetches, state management without frameworks.
