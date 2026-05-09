# Premier Snag — Property Inspection Booking System

> A property inspection scheduling platform with automated inspector assignment, PDF report generation, and full AWS deployment.

![Django](https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/DRF-092E20?style=flat-square&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=flat-square&logo=postgresql&logoColor=white)
![AWS S3](https://img.shields.io/badge/AWS_S3-232F3E?style=flat-square&logo=amazon-s3&logoColor=white)
![AWS EC2](https://img.shields.io/badge/AWS_EC2-232F3E?style=flat-square&logo=amazon-ec2&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-009639?style=flat-square&logo=nginx&logoColor=white)

---

## Overview

Premier Snag is a booking and scheduling platform for property inspections. Clients book inspections online, the system auto-assigns available inspectors, and generates PDF reports with photo evidence — all uploaded securely to AWS S3.

---

## Key Features

- **Role-Based Access Control** — Separate interfaces for clients, inspectors, and administrators
- **Automated Inspector Assignment** — Smart scheduling logic assigns available inspectors based on location and availability
- **PDF Report Generation** — Auto-generated inspection reports with annotated photo uploads
- **AWS S3 Storage** — All photos and PDF reports stored securely on S3
- **Payment Processing** — Invoice generation, payment tracking, and confirmation workflows
- **Production Deployment** — AWS EC2 + Nginx + Gunicorn, SSL certificate via Route 53

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django 4.x, Django REST Framework |
| Database | PostgreSQL |
| File Storage | AWS S3 (boto3) |
| PDF Generation | ReportLab / WeasyPrint |
| Server | AWS EC2, Nginx, Gunicorn |
| DNS & SSL | AWS Route 53, Let's Encrypt |
| Auth | JWT, Role-Based Permissions |
| Payments | Stripe / PayPal integration |

---

## System Flow

```
Client books inspection
        │
        ▼
Auto-assign available inspector (scheduling algorithm)
        │
        ▼
Inspector completes on-site inspection
        │
        ├── Upload photos  ──►  AWS S3
        │
        ▼
PDF report auto-generated (photos + findings)
        │
        ▼
Report delivered to client + payment invoice generated
```

---

## User Roles

| Role | Capabilities |
|---|---|
| **Client** | Book inspections, view reports, make payments |
| **Inspector** | View assigned jobs, upload photos, submit findings |
| **Admin** | Manage all bookings, inspectors, invoices, and reports |

---

## Deployment

- **Server**: AWS EC2 (Ubuntu)
- **Process Manager**: Gunicorn (WSGI)
- **Reverse Proxy**: Nginx
- **Database**: PostgreSQL (local / AWS RDS)
- **Static & Media**: AWS S3 + CloudFront
- **SSL**: Route 53 + Let's Encrypt

---

## Setup

```bash
git clone https://github.com/Shahzad-Mustafa/premier-snag.git
cd premier-snag
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py runserver
```

---

*Built at WebBuggs — Jan 2025*
