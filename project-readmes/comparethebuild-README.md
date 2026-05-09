# CompareTheBuild — E-Commerce Price Comparison Platform

> A large-scale web scraping and price comparison engine that monitors product data from 87+ e-commerce websites in real time.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)
![Scrapy](https://img.shields.io/badge/Scrapy-60A839?style=flat-square&logo=scrapy&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=flat-square&logo=selenium&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=flat-square&logo=mongodb&logoColor=white)
![Celery](https://img.shields.io/badge/Celery-37814A?style=flat-square&logo=celery&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white)

---

## Overview

CompareTheBuild is a modular scraping and comparison platform that aggregates product listings — names, prices, specs, and availability — from 87+ e-commerce websites. A custom matching algorithm groups identical products across retailers, enabling real-time price comparison.

---

## Key Features

- **Modular Spider Architecture** — Independent Scrapy spiders per website, easy to extend
- **Hybrid Scraping** — Selenium for JavaScript-rendered pages + Scrapy/BeautifulSoup for static HTML
- **Anti-Bot Evasion** — Proxy rotation, user-agent randomization, intelligent rate limiting
- **Automated Price Monitoring** — Celery + Redis schedule periodic re-scrapes and trigger price alerts
- **Product Matching Algorithm** — Groups similar items across retailers using name normalization and spec comparison
- **Real-Time Updates** — Price changes stored in MongoDB with full history tracking

---

## Tech Stack

| Layer | Technology |
|---|---|
| Web Framework | Flask |
| Scraping | Scrapy, Selenium, BeautifulSoup4 |
| Task Scheduling | Celery + Redis |
| Database | MongoDB |
| Data Processing | Pandas |
| Anti-Bot | Proxy rotation, rotating user-agents |

---

## Architecture

```
Scrapy Spiders (87+ sites)
    │
    ├── Static HTML  ──►  Scrapy + BeautifulSoup4
    └── JS-rendered  ──►  Selenium + ChromeDriver
            │
            ▼
    Data Pipeline (cleaning, normalization)
            │
            ▼
    Product Matching Algorithm
            │
            ▼
    MongoDB  ◄──  Celery scheduler (periodic re-scrapes)
            │
            ▼
    Flask REST API  ──►  Frontend
```

---

## Supported Sites (Sample)

| Category | Examples |
|---|---|
| Construction / Property | CompareTheBuild, Premier Snag |
| Academic | IEEE Xplore, SpringerLink, ScienceDirect |
| E-Commerce | 80+ additional retailers |

---

## Setup

```bash
git clone https://github.com/Shahzad-Mustafa/comparethebuild.git
cd comparethebuild
pip install -r requirements.txt
cp .env.example .env
# Start Redis
redis-server
# Run Celery worker
celery -A tasks worker --loglevel=info
# Run Flask app
flask run
```

---

*Built at WebBuggs — Jan 2025*
