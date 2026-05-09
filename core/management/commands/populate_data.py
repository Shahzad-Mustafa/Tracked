from django.core.management.base import BaseCommand
from core.models import Profile, SkillCategory, Skill, Experience, Education, Project
import datetime


class Command(BaseCommand):
    help = 'Populate portfolio with Shahzad Ali resume data'

    def add_arguments(self, parser):
        parser.add_argument('--clear', action='store_true', help='Delete existing data before populating')

    def handle(self, *args, **options):
        if options['clear']:
            self.stdout.write('Clearing existing data...')
            Project.objects.all().delete()
            Skill.objects.all().delete()
            SkillCategory.objects.all().delete()
            Experience.objects.all().delete()
            Education.objects.all().delete()
            self.stdout.write(self.style.WARNING('Cleared.'))

        self._create_profile()
        self._create_skill_categories()
        self._create_skills()
        self._create_experience()
        self._create_education()
        self._create_projects()
        self.stdout.write(self.style.SUCCESS('Portfolio data populated successfully!'))

    def _create_profile(self):
        Profile.objects.update_or_create(
            name='Shahzad Ali',
            defaults={
                'tagline': 'Python Backend Developer',
                'bio_short': 'Building scalable REST APIs and production systems with Django · FastAPI · AWS. 13+ production projects delivered across multiple industries.',
                'bio_detail': "I'm a backend-focused developer with 2+ years of experience building scalable, production-grade web applications using Django, DRF, and FastAPI. Based in Lahore, Pakistan, I've delivered 13+ production projects across industries including real estate, recruitment, AI SaaS, and e-commerce. My expertise spans REST API design, database optimization, async systems with Celery + Redis, cloud infrastructure on AWS, and advanced web scraping covering 87+ websites.",
                'email': 'Shahzadmustafa755@gmail.com',
                'phone': '+92 313 4046317',
                'whatsapp': '923134046317',
                'location': 'Lahore, Pakistan',
                'github_url': 'https://github.com/Shahzad-Mustafa',
                'linkedin_url': 'https://linkedin.com/in/shahzad-mustafa',
                'is_available': True,
                'available_label': 'Available for opportunities',
                'years_experience': '2+',
                'total_projects': '13+',
                'sites_scraped': '87+',
                'open_to_remote': True,
            }
        )
        self.stdout.write('  Profile created.')

    def _create_skill_categories(self):
        categories = [
            ('Languages & Core', 'bi-code-slash', 1),
            ('Backend Frameworks', 'bi-layers', 2),
            ('Databases', 'bi-database', 3),
            ('Cloud & DevOps', 'bi-cloud', 4),
            ('Scraping & Automation', 'bi-robot', 5),
            ('Testing & Tools', 'bi-tools', 6),
        ]
        for name, icon, order in categories:
            SkillCategory.objects.get_or_create(name=name, defaults={'icon': icon, 'order': order})
        self.stdout.write('  Skill categories created.')

    def _create_skills(self):
        skills_data = {
            'Languages & Core': [
                ('Python', 95, 1), ('JavaScript (ES6)', 70, 2), ('SQL', 85, 3),
                ('HTML5', 75, 4), ('CSS3', 70, 5),
            ],
            'Backend Frameworks': [
                ('Django', 95, 1), ('Django REST Framework', 92, 2), ('FastAPI', 88, 3),
                ('Flask', 82, 4), ('Celery', 85, 5), ('Redis', 80, 6),
                ('Gunicorn', 75, 7), ('Nginx', 72, 8),
            ],
            'Databases': [
                ('PostgreSQL', 90, 1), ('MongoDB', 80, 2), ('SQLite', 85, 3),
                ('Django ORM', 92, 4),
            ],
            'Cloud & DevOps': [
                ('AWS EC2', 78, 1), ('AWS S3', 80, 2), ('AWS RDS', 75, 3),
                ('AWS IAM', 72, 4), ('Docker', 80, 5), ('GitHub Actions', 75, 6),
                ('Linux Server Admin', 78, 7), ('SSL Configuration', 70, 8),
            ],
            'Scraping & Automation': [
                ('Scrapy', 92, 1), ('Selenium', 88, 2), ('BeautifulSoup4', 90, 3),
                ('Pandas', 82, 4), ('Proxy Rotation', 78, 5), ('Requests', 85, 6),
            ],
            'Testing & Tools': [
                ('Pytest', 78, 1), ('Django TestCase', 80, 2), ('Postman', 82, 3),
                ('Git', 90, 4), ('VS Code', 88, 5),
            ],
        }
        for category_name, skills in skills_data.items():
            try:
                category = SkillCategory.objects.get(name=category_name)
            except SkillCategory.DoesNotExist:
                continue
            for name, proficiency, order in skills:
                Skill.objects.get_or_create(
                    name=name, category=category,
                    defaults={'proficiency': proficiency, 'order': order}
                )
        self.stdout.write('  Skills created.')

    def _create_experience(self):
        experiences = [
            {
                'company': 'WebBuggs',
                'role': 'Python Developer',
                'start_date': datetime.date(2025, 1, 1),
                'end_date': None,
                'is_current': True,
                'order': 1,
                'description': 'Architect and implement backend APIs using Django, Flask, FastAPI, and Celery. Manage full development lifecycle from design to cloud deployment on AWS and VPS environments.',
                'highlights': [
                    'Engineered REST APIs and core automation workflows at CRMCopilot.ai, eliminating 30 minutes of manual work weekly',
                    'Refactored a critical Django backend service, boosting performance by 40% through query optimization and database indexing',
                    'Designed and deployed a modular web scraping framework for 87+ websites using Selenium, Scrapy, and BeautifulSoup',
                    'Implemented Celery + Redis for asynchronous task processing, ensuring system responsiveness under heavy load',
                    'Deployed and managed applications on AWS (EC2, S3, RDS) and VPS (Linux/Nginx)',
                    'Integrated FastAPI microservices for high-performance endpoints and connected React frontends via RESTful API contracts',
                ],
                'tech_used': ['Python', 'Django', 'DRF', 'FastAPI', 'Flask', 'Celery', 'Redis', 'AWS EC2', 'AWS S3', 'AWS RDS', 'Nginx', 'Scrapy', 'Selenium'],
            },
            {
                'company': 'BNR360',
                'role': 'Django Developer',
                'start_date': datetime.date(2024, 6, 1),
                'end_date': datetime.date(2024, 12, 31),
                'is_current': False,
                'order': 2,
                'description': 'Backend developer focused on scalable Django applications, RESTful APIs, and PostgreSQL optimization.',
                'highlights': [
                    'Enhanced API response times by 25% through query optimization and Redis caching strategies',
                    'Designed secure JWT-based authentication and permission systems using Django REST Framework',
                    'Collaborated with frontend (React) teams to streamline API integration, improving load times by 20%',
                    'Managed AWS RDS (PostgreSQL) instances and configured S3 for media/static file storage',
                ],
                'tech_used': ['Django', 'DRF', 'PostgreSQL', 'Redis', 'JWT', 'AWS RDS', 'AWS S3', 'React'],
            },
            {
                'company': 'Website Access',
                'role': 'Full-Stack Developer',
                'start_date': datetime.date(2023, 7, 1),
                'end_date': datetime.date(2024, 3, 31),
                'is_current': False,
                'order': 3,
                'description': 'Developed and maintained web applications using Python, Django, Bootstrap, and JavaScript for a UK-based client.',
                'highlights': [
                    'Collaborated with UX/UI teams to design responsive interfaces, improving user engagement by 20%',
                    'Implemented AJAX for dynamic content updates and integrated third-party APIs (payment gateways, auth systems)',
                    'Ensured 99.9% uptime through deployment support and ongoing maintenance',
                ],
                'tech_used': ['Python', 'Django', 'JavaScript', 'Bootstrap', 'AJAX', 'HTML5', 'CSS3'],
            },
        ]
        for data in experiences:
            Experience.objects.update_or_create(
                company=data['company'], role=data['role'],
                defaults={k: v for k, v in data.items() if k not in ('company', 'role')}
            )
        self.stdout.write('  Experience entries created.')

    def _create_education(self):
        entries = [
            {
                'institution': 'University of South Asia',
                'degree': 'Bachelor of Science in Computer Science',
                'field': 'Computer Science',
                'start_year': 2020,
                'end_year': 2024,
                'order': 1,
            },
            {
                'institution': 'Punjab College Raiwind',
                'degree': 'Intermediate in Computer Science (ICS)',
                'field': 'Computer Science',
                'start_year': 2018,
                'end_year': 2020,
                'order': 2,
            },
        ]
        for data in entries:
            Education.objects.update_or_create(
                institution=data['institution'],
                defaults={k: v for k, v in data.items() if k != 'institution'}
            )
        self.stdout.write('  Education entries created.')

    def _create_projects(self):
        projects = [
            {
                'title': 'CRMCopilot.ai',
                'slug': 'crmcopilot-ai',
                'tagline': 'AI-Powered CRM Assistant',
                'description': 'Integrated OpenAI GPT models to build an NLP engine for summarizing call transcripts and generating context-aware email drafts. Engineered secure OAuth-based integrations with Salesforce, Zoho, and HubSpot for real-time CRM data sync.',
                'tech_stack': ['Python', 'DRF', 'FastAPI', 'OpenAI API', 'PostgreSQL', 'Celery', 'Redis', 'AWS'],
                'highlight_stat': 'Eliminated 30 min/week manual work',
                'project_type': 'featured',
                'order': 1,
            },
            {
                'title': 'CompareTheBuild',
                'slug': 'comparethebuild',
                'tagline': 'E-Commerce Price Comparison Platform',
                'description': 'Built a modular scraping system extracting product data (names, prices, specs) from 87+ e-commerce sites. Developed automated price monitoring with Celery and Redis for real-time product updates.',
                'tech_stack': ['Python', 'Flask', 'Scrapy', 'MongoDB', 'Celery', 'Redis', 'Selenium'],
                'highlight_stat': '87+ e-commerce websites scraped',
                'project_type': 'featured',
                'order': 2,
            },
            {
                'title': 'Hello-Living',
                'slug': 'hello-living',
                'tagline': 'Property Hosting CRM',
                'description': 'Developed multi-role authentication (hosts, clients, admins) with JWT and role-based permissions. Built property listing and booking management with real-time reservation handling and automated email notifications.',
                'tech_stack': ['Django', 'DRF', 'PostgreSQL', 'Celery', 'Redis', 'JWT'],
                'highlight_stat': 'Multi-role CRM with real-time reservations',
                'project_type': 'featured',
                'order': 3,
            },
            {
                'title': 'Premier Snag',
                'slug': 'premier-snag',
                'tagline': 'Property Inspection Booking System',
                'description': 'Implemented role-based access control for clients, inspectors, and administrators. Built a booking system with automated inspector assignment logic and PDF inspection report generation with photo uploads stored on AWS S3.',
                'tech_stack': ['Django', 'DRF', 'PostgreSQL', 'AWS S3', 'AWS EC2', 'Nginx', 'Gunicorn'],
                'highlight_stat': 'AWS EC2 + S3 full production deployment',
                'project_type': 'featured',
                'order': 4,
            },
            {
                'title': 'Advanced Scraping Engine',
                'slug': 'scraping-engine',
                'tagline': '87+ Website Data Acquisition Framework',
                'description': 'Deployed custom spiders for IEEE Xplore, SpringerLink, ScienceDirect, and 87+ e-commerce platforms. Engineered hybrid approach: Selenium for JS-rendered content plus Scrapy/BS4 for static HTML. Implemented anti-bot evasion with proxy rotation.',
                'tech_stack': ['Python', 'Scrapy', 'Selenium', 'BeautifulSoup4', 'Pandas', 'PostgreSQL'],
                'highlight_stat': '87+ websites, anti-bot evasion',
                'project_type': 'featured',
                'order': 5,
            },
            {
                'title': 'Sphere',
                'slug': 'sphere',
                'tagline': 'Recruitment Management Platform',
                'description': 'Developed scalable RESTful APIs with pagination, filtering, and throttling for job postings and applicant tracking. Optimized PostgreSQL with strategic indexing and query tuning. Implemented JWT + Django Allauth for secure authentication.',
                'tech_stack': ['Django', 'DRF', 'PostgreSQL', 'JWT', 'Redis'],
                'highlight_stat': '25% load time reduction via DB indexing',
                'project_type': 'featured',
                'order': 6,
            },
            {
                'title': 'ClickHub',
                'slug': 'clickhub',
                'tagline': 'Full-Featured E-Commerce Platform',
                'description': 'Designed a robust e-commerce platform with relational database management and optimized queries. Implemented AJAX and Bootstrap for dynamic, user-friendly interfaces. Delivered from inception to deployment with A grade.',
                'tech_stack': ['Django', 'PostgreSQL', 'AJAX', 'Bootstrap', 'JavaScript'],
                'highlight_stat': 'Full e-commerce platform, A grade delivery',
                'project_type': 'regular',
                'order': 7,
            },
        ]
        for data in projects:
            Project.objects.update_or_create(
                slug=data['slug'],
                defaults={k: v for k, v in data.items() if k != 'slug'}
            )
        self.stdout.write('  Projects created.')
