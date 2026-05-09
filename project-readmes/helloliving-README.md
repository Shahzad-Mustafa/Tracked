# Hello-Living — Property Hosting CRM

> A full-featured property hosting and booking management CRM with multi-role authentication, real-time reservation handling, and automated notifications.

![Django](https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/DRF-092E20?style=flat-square&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=flat-square&logo=postgresql&logoColor=white)
![Celery](https://img.shields.io/badge/Celery-37814A?style=flat-square&logo=celery&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-000000?style=flat-square&logo=jsonwebtokens&logoColor=white)

---

## Overview

Hello-Living is a property hosting CRM built for hosts, clients, and administrators. It handles property listings, real-time booking reservations, dispute resolution, and automated email workflows — all secured by role-based access control.

---

## Key Features

- **Multi-Role Authentication** — Separate JWT-authenticated portals for hosts, clients, and admins
- **Real-Time Reservation Handling** — Booking system with conflict detection and instant confirmation
- **Admin Panel** — Deal management, analytics reporting, and dispute resolution tools
- **Automated Notifications** — Celery-powered async email queue for booking confirmations, reminders, and alerts
- **Property Listings** — Full CRUD with filtering, availability calendars, and pricing management

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django 4.x, Django REST Framework |
| Auth | JWT (SimpleJWT), Role-Based Access Control |
| Database | PostgreSQL |
| Task Queue | Celery + Redis |
| Email | Celery async workers + SMTP/SendGrid |
| API | RESTful with DRF serializers, pagination, filtering |

---

## User Roles

| Role | Permissions |
|---|---|
| **Host** | Create/manage listings, view bookings, handle disputes |
| **Client** | Browse listings, make reservations, manage bookings |
| **Admin** | Full access — analytics, deal management, dispute resolution |

---

## API Endpoints (Sample)

```
POST   /api/auth/register/          Register new user (role-based)
POST   /api/auth/login/             JWT token login
GET    /api/properties/             List all properties (filterable)
POST   /api/properties/             Create property listing (host only)
POST   /api/bookings/               Create reservation
GET    /api/bookings/{id}/          Booking details
POST   /api/admin/disputes/         Create/resolve disputes (admin)
GET    /api/admin/analytics/        Dashboard analytics (admin)
```

---

## Setup

```bash
git clone https://github.com/Shahzad-Mustafa/hello-living.git
cd hello-living
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py runserver

# In a separate terminal — start Celery worker
celery -A hello_living worker --loglevel=info
```

---

*Built at WebBuggs — Jan 2025*
