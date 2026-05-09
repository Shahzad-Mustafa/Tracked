# Sphere — Recruitment Management Platform

> A scalable recruitment management system with optimized RESTful APIs, JWT authentication, and real-time HR analytics.

![Django](https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/DRF-092E20?style=flat-square&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=flat-square&logo=postgresql&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-000000?style=flat-square&logo=jsonwebtokens&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white)

---

## Overview

Sphere is a full-featured recruitment management platform handling job postings, applicant tracking, HR analytics, and role-based access. Built with performance-first engineering — strategic PostgreSQL indexing and Redis caching reduced load times by 25%.

---

## Key Features

- **Scalable REST APIs** — Pagination, filtering, searching, and throttling on all major endpoints
- **Applicant Tracking System (ATS)** — Full lifecycle from job posting to hire decision
- **JWT Authentication** — Secure login via JWT + Django Allauth with role-based permissions
- **Performance Optimized** — Strategic DB indexing + query tuning = 25% faster load times
- **HR Analytics Dashboard** — Real-time reporting for HR decision-making
- **Throttling & Rate Limiting** — DRF throttle classes protect API from abuse

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django 4.x, Django REST Framework |
| Auth | JWT (SimpleJWT), Django Allauth |
| Database | PostgreSQL (indexed & tuned) |
| Caching | Redis |
| API Features | Pagination, filtering, throttling, search |

---

## API Design

```
GET    /api/jobs/                   List job postings (paginated, filterable)
POST   /api/jobs/                   Create job posting (HR only)
GET    /api/jobs/{id}/applicants/   List applicants for a job
POST   /api/apply/{job_id}/         Submit application
PATCH  /api/applications/{id}/      Update application status
GET    /api/analytics/              HR dashboard data
POST   /api/auth/token/             JWT login
POST   /api/auth/token/refresh/     Refresh JWT token
```

---

## Performance Highlights

- Added **composite indexes** on frequently filtered columns (`status`, `created_at`, `job_id`)
- Used `select_related` and `prefetch_related` to eliminate N+1 query patterns
- **Redis caching** on analytics and listing endpoints with 5-minute TTL
- Result: **25% reduction** in average API response time

---

## Setup

```bash
git clone https://github.com/Shahzad-Mustafa/sphere-recruitment.git
cd sphere-recruitment
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py runserver
```

---

*Built at BNR360 — Jun 2024 to Dec 2024*
