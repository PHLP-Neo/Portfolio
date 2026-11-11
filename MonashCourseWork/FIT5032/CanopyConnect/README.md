# Canopy Connect

Canopy Connect is a web application for finding environmental volunteering opportunities in Melbourne. I developed it as an individual project for Monash University's FIT5032 unit. I wanted volunteers to find positions near them and give editors a way to remove filled positions from the listings without losing their records.

[Open the live application](https://canopy-connect-a3.pages.dev/)

## Try the demo

1. Sign in with Google or create an account with an email address and password. New accounts start as viewers.
2. On **Positions**, search for `volunteer` and select **Show Matching Jobs**. The map groups matches by suburb; select a pin to see the position titles.
3. Enter a starting suburb such as `Footscray`, then select **Find Three Nearest Jobs**. Choose **Show Walking Route** on a result to see the route, walking distance and estimated time.

## What the application does

| Role | Features |
| --- | --- |
| Viewer | Search position titles and descriptions, browse map results, get walking directions, and submit or update one rating per position. |
| Editor | Create, edit, archive and restore positions. The management table supports sorting, column filters, pagination and CSV export. |
| Administrator | Manage user roles, compare positions by suburb in the dashboard, and send announcements to selected role groups or position details as an email attachment. |

The nearest-job list is ranked by straight-line distance to each position's listed suburb. Walking distance is calculated separately, after the user selects a route. Archived positions stay in Firestore for editors to restore, but are excluded from the available listings and public API responses.

## How it works

- **Frontend:** Vue 3 Composition API, Vue Router and Vite. Bootstrap and PrimeVue provide the interface and tables, and Chart.js renders the dashboard chart. Cloudflare Pages serves the built frontend.
- **Authentication and data:** Firebase Authentication handles Google and email sign-in. Cloud Firestore stores profiles, roles, positions and ratings. Vue Router guards control navigation, while Firestore rules govern client access to the data.
- **Server functions:** Node.js Firebase Cloud Functions provide two public endpoints for available positions. A separate callable function checks the caller's administrator role before sending email through Resend. The Resend key is stored in Secret Manager.
- **Mapping:** Mapbox GL JS renders the map, the Geocoding API resolves suburbs and addresses, and the Directions API calculates walking routes.

The public endpoints return JSON:

| Endpoint | Response |
| --- | --- |
| [`countPositions`](https://australia-southeast2-canopy-connect-16c1a.cloudfunctions.net/countPositions) | Count of available positions. |
| [`getPositions`](https://australia-southeast2-canopy-connect-16c1a.cloudfunctions.net/getPositions) | Count and list of available positions, with each position's ID, title, suburb and description. |

## Run the frontend locally

Use Node.js 24.12 or later in the 24.x series. From the repository root:

```sh
cd MonashCourseWork/FIT5032/CanopyConnect
npm ci
```

Create `.env.local` in the `CanopyConnect` folder and add your own **public** Mapbox token:

```dotenv
VITE_MAPBOX_TOKEN=your_public_mapbox_token
```

```sh
npm run dev
```

Open the local URL shown by Vite. Run `npm run build` to generate the production files in `dist/`.

The local frontend uses the Firebase project configured in [`src/firebase/init.js`](src/firebase/init.js). Running Vite does not start a separate backend or database. For a separate deployment, configure your own Firebase project, enable the sign-in providers and authorised domains, publish Firestore rules, and add sample data. Update the dashboard's count endpoint to point to your own function. To enable email, deploy the functions with a `RESEND_API_KEY` secret and change the sender to an address on your verified Resend domain. The published Firestore rules are managed in Firebase Console and are not bundled in this repository.

## Scope

This was a university project. The map uses suburb locations as an approximation where the listing provides only a suburb. I used AI assistance during development and reviewed the code and its main workflows before presenting the application in a technical interview.
