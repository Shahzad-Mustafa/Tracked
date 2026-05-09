# Advanced Web Scraping Engine — 87+ Websites

> A production-grade, modular web scraping framework capable of extracting data from 87+ websites — including JS-heavy pages — with built-in anti-bot evasion and resilient data pipelines.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Scrapy](https://img.shields.io/badge/Scrapy-60A839?style=flat-square&logo=scrapy&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=flat-square&logo=selenium&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup4-3776AB?style=flat-square&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=flat-square&logo=postgresql&logoColor=white)

---

## Overview

A large-scale, production-ready scraping framework targeting 87+ academic databases, e-commerce platforms, and property websites. The hybrid approach combines Scrapy for high-throughput static scraping with Selenium for JavaScript-rendered content — complete with anti-bot evasion and resilient retry pipelines.

---

## Key Features

- **87+ Custom Spiders** — Individual spiders for IEEE Xplore, SpringerLink, ScienceDirect, and 84+ more
- **Hybrid Engine** — Scrapy/BS4 for static HTML + Selenium/ChromeDriver for JS-rendered pages
- **Anti-Bot Evasion** — Proxy rotation, user-agent switching, randomized delays, CAPTCHA handling
- **Resilient Pipelines** — Retry logic, error handling, and dead-letter queue for failed requests
- **Multi-Format Output** — Clean JSON/CSV exports and direct PostgreSQL ingestion
- **Modular Architecture** — Add new spiders without touching existing code

---

## Tech Stack

| Component | Technology |
|---|---|
| Scraping Framework | Scrapy 2.x |
| JS Rendering | Selenium + ChromeDriver |
| HTML Parsing | BeautifulSoup4, lxml |
| Data Processing | Pandas, NumPy |
| Data Storage | PostgreSQL, CSV, JSON |
| Anti-Bot | Rotating proxies, user-agent rotation, `scrapy-fake-useragent` |
| Scheduling | Celery + Redis (periodic scrapes) |

---

## Architecture

```
Target Websites (87+)
        │
        ├── Static HTML ──► Scrapy Spider + BeautifulSoup4 parser
        └── JS-Rendered ──► Selenium WebDriver ──► Scrapy pipeline
                │
                ▼
        Item Pipeline
            ├── Deduplication filter
            ├── Data cleaning & normalization
            └── Output router
                    ├── PostgreSQL (primary storage)
                    ├── JSON export
                    └── CSV export
```

---

## Anti-Bot Techniques

| Technique | Implementation |
|---|---|
| Proxy Rotation | Pool of residential/datacenter proxies, rotated per request |
| User-Agent Rotation | `scrapy-fake-useragent` with realistic browser signatures |
| Request Rate Limiting | Randomized delays (1–5s) with Scrapy's `AUTOTHROTTLE` |
| Session Management | Cookie persistence for authenticated scraping |
| Retry Logic | Exponential backoff with max 3 retry attempts |

---

## Covered Domains (Sample)

| Category | Sites |
|---|---|
| Academic | IEEE Xplore, SpringerLink, ScienceDirect |
| E-Commerce | 80+ product listing sites |
| Property | CompareTheBuild, Premier Snag, Hello-Living |

---

## Setup

```bash
git clone https://github.com/Shahzad-Mustafa/scraping-engine.git
cd scraping-engine
pip install -r requirements.txt
cp .env.example .env

# Run a specific spider
scrapy crawl ieee_xplore -o output/ieee.json

# Run all spiders via Celery
celery -A tasks worker --loglevel=info
```

---

*Built at WebBuggs — Production framework Jan 2025*
