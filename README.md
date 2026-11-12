# PHLP Neo

I’m a Master of Information Technology student at Monash University. I build Python web applications and APIs, and my projects also cover cloud deployment, web and Android interfaces, and data analysis.

[Portfolio website](https://www.phlpneo.com/) · [Project case studies and demos](https://www.phlpneo.com/projects/)

## Featured projects

### Cloud-Native YOLO Inference Service

*Individual Monash project · Python, FastAPI, Docker, Kubernetes, Terraform, Ansible, Locust*

I built an API that uses a pretrained YOLO model to detect plastic waste in images and return annotated results. I implemented request batching and a bounded queue for inference, deployed the service to a Kubernetes cluster on Google Cloud, and used Locust to compare throughput and latency across pod counts.

[Case study and report](https://www.phlpneo.com/projects/cloud-native-yolo-inference-service/) · [Code](MonashCourseWork/FeaturedProjects/CloudEco%20Scalable%20ML-Inference%20System%20%28Kubernetes%20%26%20FastAPI%29/)

### Aussie EcoLens — Multi-Cloud Wildlife Media Platform

*Monash team project · Python, FastAPI, AWS Cognito, Cloud Run, Firestore*

Our team built a platform for sharing wildlife observations. I worked on Cognito sign-in and API authorization, built the tag subscription and notification service on Cloud Run and Firestore, and configured Workload Identity Federation so AWS Lambda could call the GCP service without long-lived service account keys.

[Case study and report](https://www.phlpneo.com/projects/aussie-ecolens-multi-cloud-wildlife-media-platform/)

### Canopy Connect — Melbourne Volunteer Opportunities

*Individual Monash project · Vue 3, Firebase, Mapbox*

I built a web app for finding environmental volunteer opportunities in Melbourne. It includes map search and walking directions, sign-in, ratings stored in Firestore, and role-based tools for managing listings.

[Case study](https://www.phlpneo.com/projects/canopy-connect/) · [Code](MonashCourseWork/FIT5032/CanopyConnect/)

### Capstone Gallery — Django Image Sharing Platform

*Individual CS50W capstone · Python, Django, JavaScript, SQLite*

I built an image-sharing app where users can upload and tag images, browse or search the gallery, and leave comments and likes. Only the owner can delete an image, and deletion removes both the database record and the uploaded file.

[Case study](https://www.phlpneo.com/projects/capstone-gallery-django-image-sharing-platform/) · [Code and setup](CS50W/capstone/)

### MediaWiki Data Extraction Toolkit

*Personal project · Python, Beautiful Soup, regular expressions*

I built a command-line tool for a Dwarf Fortress translation project. It discovers MediaWiki pages, extracts configurable text and game data tokens, and exports the results to CSV for review.

[Case study](https://www.phlpneo.com/projects/mediawiki-data-extraction-toolkit/) · [Code and usage](PersonalProjects/DF-Scraper/)

### AquaGuard — Household Water Monitoring and Leak Detection

*Monash team project · Kotlin, Jetpack Compose, StateFlow, WorkManager*

I built the monitoring module for our Android app. It replays historical water-meter readings, keeps the dashboard and leak monitor in sync, and runs background checks for sustained flow when the household is marked away. I integrated the module with account and settings features built by teammates.

[Case study](https://www.phlpneo.com/projects/aquaguard-household-water-monitoring/)

## Data and analytics coursework

- **MonCity data warehouse and dashboard:** Designed an Oracle SQL warehouse for bookings, maintenance, and accidents, implemented the aggregated model, and built a Power BI dashboard for accident analysis.
- **Public transit coverage:** Used PostgreSQL/PostGIS and QGIS to measure proximity to bus stops, map service coverage, and compare spatial query plans.
- **Text classification in R:** Compared decision trees and random forests using precision, recall, and F1 on a validation split.

## Browse the repository

- [Monash coursework](MonashCourseWork/) — project code, labs, and study notes.
- [CS50W projects](CS50W/) — web applications built during CS50’s Web Programming with Python and JavaScript.
- [Personal projects](PersonalProjects/) — tools and experiments outside coursework.
