# CRMCopilot.ai — AI-Powered CRM Assistant

> An intelligent CRM assistant powered by OpenAI GPT, integrating with Salesforce, Zoho, and HubSpot via OAuth for real-time data sync and AI-driven automation.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Django REST Framework](https://img.shields.io/badge/DRF-092E20?style=flat-square&logo=django&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=flat-square&logo=postgresql&logoColor=white)
![Celery](https://img.shields.io/badge/Celery-37814A?style=flat-square&logo=celery&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazon-aws&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI_API-412991?style=flat-square&logo=openai&logoColor=white)

---

## Overview

CRMCopilot.ai is an AI-powered backend system that eliminates manual CRM workflows. It uses GPT models to summarize call transcripts, generate email drafts, and sync data across Salesforce, Zoho, and HubSpot in real time — saving teams 30+ minutes of manual work per week.

---

## Key Features

- **AI NLP Engine** — OpenAI GPT integration for call transcript summarization and context-aware email draft generation
- **OAuth CRM Integrations** — Secure OAuth-based real-time sync with Salesforce, Zoho CRM, and HubSpot
- **Async Email Processing** — Celery + Redis batch email pipeline keeps the main app fully responsive under load
- **Versioned REST APIs** — DRF + FastAPI endpoints with versioning for seamless React frontend integration
- **CI/CD Pipeline** — GitHub Actions for automated testing and deployment
- **AWS Infrastructure** — EC2 (app server), RDS PostgreSQL (database), S3 (file storage)

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend API | Django REST Framework, FastAPI |
| AI / NLP | OpenAI API (GPT-4) |
| Task Queue | Celery + Redis |
| Database | PostgreSQL (AWS RDS) |
| File Storage | AWS S3 |
| Server | AWS EC2, Nginx, Gunicorn |
| CI/CD | GitHub Actions |
| Auth | JWT, OAuth 2.0 |

---

## Architecture Highlights

```
Client (React)
    │
    ▼
FastAPI / DRF REST API (versioned)
    │
    ├── OpenAI GPT Service  ──►  Transcript Summarization
    │                            Email Draft Generation
    │
    ├── OAuth Service  ──►  Salesforce / Zoho / HubSpot sync
    │
    └── Celery + Redis  ──►  Async email batch processing
            │
            ▼
    PostgreSQL (AWS RDS)   AWS S3 (file storage)
```

---

## Impact

- Eliminated **30 minutes of manual work weekly** per team member
- Enhanced **data consistency** across CRM platforms via real-time sync
- Zero downtime async processing via Celery worker pools

---

## Setup

```bash
git clone https://github.com/Shahzad-Mustafa/crmcopilot-ai.git
cd crmcopilot-ai
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env      # Add your API keys
python manage.py migrate
python manage.py runserver
```

---

## Environment Variables

```env
OPENAI_API_KEY=your_openai_key
DATABASE_URL=postgresql://user:pass@host:5432/dbname
REDIS_URL=redis://localhost:6379/0
AWS_ACCESS_KEY_ID=your_key
AWS_SECRET_ACCESS_KEY=your_secret
AWS_S3_BUCKET=your_bucket
SALESFORCE_CLIENT_ID=...
ZOHO_CLIENT_ID=...
HUBSPOT_CLIENT_ID=...
```

---

*Built at WebBuggs — Jan 2025*
