# Surrey-Horizon

A cloud-native, microservices-based digital magazine built for organisations and universities. It provides a centralised hub for non-work updates, news, and events; combining structured publishing, moderation, and real-time engagement without cluttering email channels.

# Purpose

Modern institutions struggle to balance information sharing and focus. Surrey-Horizon solves this by creating a private, customisable magazine platform that lets users share posts, read curated content, and engage interactively; all within a moderated, secure environment.

# Architecture

Surrey-Horizon follows a distributed microservices architecture designed for scalability, reliability, and modular development.
Each service handles a focused responsibility and communicates through REST APIs secured by a central authentication layer.

<img width="682" height="640" alt="image" src="https://github.com/user-attachments/assets/7126331b-d18d-4367-a20b-99e4dd17a65a" />


# Key Design Highlights

1. Authentication/Authorisation Microservice
  - Implements Google OAuth 2.0 via NestJS middleware.
  - Manages identity, sessions, and role-based access control (Admin, Moderator, User).
  - Deployed as a serverless service on AWS Lambda via API Gateway.

2. Independent Functional Microservices
  - **Blog Service:** Handles post creation and media uploads to AWS S3.
  - **Magazine Scheduler:** Uses cron jobs to release magazines at fixed times.
  - **Admin/Moderation:** Enables moderators to review, approve, or reject content and manage roles.
  - **Likes & Comments:** Provides interactive engagement APIs.
  - **Notification Service:** Uses Django Channels and Redis (ElastiCache) for real-time push notifications.

3. Shared Resources
  - PostgreSQL as a central database ensuring data integrity and high availability.
  - Redis for pub/sub messaging and instant user updates.
  - Dockerised services running on AWS EC2 instances with load-ready configuration.

4. Frontend
  - Built with Vue 3, Vuetify, and Vue Router.
  - Communicates with backend microservices via REST and WebSocket APIs.
  - Implements a clean SPA experience with secure session storage.

# Tech Stack

| Layer            | Technologies                                     |
| ---------------- | ------------------------------------------------ |
| Frontend         | Vue 3, Vuetify, Vue Router                       |
| Backend          |	NestJS, Django, Flask, Node.js                  |  
| Authentication   |	Google OAuth 2.0, JWT, Role-Based Access        |
| Database & Cache |	PostgreSQL, Redis (AWS ElastiCache)             |
| Storage	         | AWS S3                                           |
| Deployment       |	AWS EC2, AWS Lambda, API Gateway, Docker        |
| CI/CD	           | Netlify (frontend), GitHub Flow, Docker Compose  |
| Testing	         | Unit Tests (Pytest/Jest), planned E2E automation |

# Core Features

- **Google OAuth 2.0 Authentication:** secure sign-in with role assignment.
- **Custom Blog System:** text + media posts, tagging, and categorisation.
- **Moderation Workflow:** review, feedback, approval/rejection pipeline.
- **Magazine Scheduling:** automated timed releases with pagination and archiving.
- **Real-Time Notifications:** live alerts for comments, likes, and approvals.
- **Scalable Cloud Deployment:** Dockerised microservices distributed across AWS EC2 + Lambda.
- **User-Friendly Interface:** responsive, accessible, and built for simplicity.
