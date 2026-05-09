from django.db import models
from django.utils.text import slugify


class Profile(models.Model):
    name = models.CharField(max_length=100, default='Shahzad Ali')
    tagline = models.CharField(max_length=200, default='Python Backend Developer')
    bio_short = models.TextField(help_text='1-2 sentence hero bio (plain text)', blank=True)
    bio_detail = models.TextField(help_text='Longer about-me paragraph (HTML from rich editor)', blank=True)
    avatar = models.ImageField(upload_to='avatar/', blank=True, null=True, help_text='Profile photo — auto-cropped to square')
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=30, blank=True)
    whatsapp = models.CharField(max_length=30, blank=True, help_text='Phone number with country code e.g. 923134046317')
    location = models.CharField(max_length=100, blank=True)
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    website_url = models.URLField(blank=True)
    is_available = models.BooleanField(default=True, help_text='Show "Available for opportunities" badge')
    available_label = models.CharField(max_length=100, default='Available for opportunities')

    # Hero stat chips — value + label both editable
    total_projects = models.CharField(max_length=10, default='13+')
    projects_label = models.CharField(max_length=30, default='Projects')
    years_experience = models.CharField(max_length=10, default='2+')
    experience_label = models.CharField(max_length=30, default='Years Exp')
    sites_scraped = models.CharField(max_length=10, default='87+')
    scraped_label = models.CharField(max_length=30, default='Sites Scraped')

    # About section metric cards
    metric1_value = models.CharField(max_length=20, default='40%')
    metric1_label = models.CharField(max_length=50, default='Performance Boost')
    metric1_icon = models.CharField(max_length=60, default='bi-lightning-charge-fill')
    metric2_value = models.CharField(max_length=20, default='25%')
    metric2_label = models.CharField(max_length=50, default='Faster APIs')
    metric2_icon = models.CharField(max_length=60, default='bi-speedometer2')
    metric3_value = models.CharField(max_length=20, default='87+')
    metric3_label = models.CharField(max_length=50, default='Sites Scraped')
    metric3_icon = models.CharField(max_length=60, default='bi-globe2')
    metric4_value = models.CharField(max_length=20, default='30min')
    metric4_label = models.CharField(max_length=50, default='Saved Weekly')
    metric4_icon = models.CharField(max_length=60, default='bi-clock-history')

    open_to_remote = models.BooleanField(default=True)
    resume_label = models.CharField(max_length=50, default='Download Resume')

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profile'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.avatar:
            try:
                from PIL import Image, ImageOps
                img_path = self.avatar.path
                with Image.open(img_path) as img:
                    img = ImageOps.exif_transpose(img)
                    img = ImageOps.fit(img, (600, 600), Image.LANCZOS)
                    img.save(img_path, optimize=True, quality=92)
            except Exception:
                pass

    @property
    def initials(self):
        parts = self.name.split()
        return ''.join(p[0].upper() for p in parts[:2])

    @property
    def whatsapp_url(self):
        return f'https://wa.me/{self.whatsapp}' if self.whatsapp else ''


class SkillCategory(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, help_text='Bootstrap Icons class e.g. bi-code-slash')
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name_plural = 'Skill Categories'

    def __str__(self):
        return self.name


class Skill(models.Model):
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)
    proficiency = models.PositiveSmallIntegerField(default=80, help_text='0–100')
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.name} ({self.category.name})'


class Project(models.Model):
    FEATURED = 'featured'
    REGULAR = 'regular'
    TYPE_CHOICES = [(FEATURED, 'Featured'), (REGULAR, 'Regular')]

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    tagline = models.CharField(max_length=300)
    description = models.TextField()
    tech_stack = models.JSONField(default=list, help_text='List of tech names e.g. ["Python","DRF"]')
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True)
    project_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default=FEATURED)
    highlight_stat = models.CharField(max_length=200, blank=True, help_text='Key achievement shown on card')
    order = models.PositiveSmallIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Experience(models.Model):
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True, help_text='Leave blank for "Present"')
    location = models.CharField(max_length=200, default='Lahore, Pakistan')
    description = models.TextField(blank=True)
    highlights = models.JSONField(default=list, help_text='List of achievement bullet points')
    tech_used = models.JSONField(default=list, help_text='List of tech names used in this role')
    order = models.PositiveSmallIntegerField(default=0)
    is_current = models.BooleanField(default=False)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.role} at {self.company}'

    @property
    def end_label(self):
        return 'Present' if self.is_current else self.end_date.strftime('%b %Y')

    @property
    def start_label(self):
        return self.start_date.strftime('%b %Y')


class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    field = models.CharField(max_length=200, blank=True)
    start_year = models.PositiveSmallIntegerField()
    end_year = models.PositiveSmallIntegerField(null=True, blank=True)
    grade = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.degree} — {self.institution}'


class HeroBadge(models.Model):
    POSITIONS = [
        ('top-right',   'Top Right'),
        ('top-left',    'Top Left'),
        ('bottom-left', 'Bottom Left'),
    ]
    label    = models.CharField(max_length=30)
    icon     = models.CharField(max_length=60, help_text='Bootstrap Icons class e.g. bi-code-slash')
    position = models.CharField(max_length=20, choices=POSITIONS, default='top-right')
    order    = models.PositiveSmallIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'Hero Badge'
        verbose_name_plural = 'Hero Badges'

    def __str__(self):
        return f'{self.label} ({self.position})'


class PageVisit(models.Model):
    DEVICE_CHOICES = [
        ('desktop', 'Desktop'),
        ('mobile',  'Mobile'),
        ('tablet',  'Tablet'),
        ('other',   'Other'),
    ]
    ip_address      = models.GenericIPAddressField(null=True, blank=True)
    user_agent      = models.TextField(blank=True)
    browser         = models.CharField(max_length=100, blank=True)
    browser_version = models.CharField(max_length=30,  blank=True)
    os              = models.CharField(max_length=100, blank=True)
    device_type     = models.CharField(max_length=10, choices=DEVICE_CHOICES, default='other')
    referrer        = models.CharField(max_length=500, blank=True)
    path            = models.CharField(max_length=500, default='/')
    session_key     = models.CharField(max_length=40,  blank=True)
    visited_at      = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-visited_at']
        indexes = [
            models.Index(fields=['visited_at']),
            models.Index(fields=['ip_address']),
            models.Index(fields=['device_type']),
        ]

    def __str__(self):
        return f'{self.ip_address} — {self.browser} ({self.visited_at:%Y-%m-%d %H:%M})'


class ContactMessage(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=300)
    message = models.TextField()
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    is_read = models.BooleanField(default=False)
    replied = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} — {self.subject} ({self.created_at:%Y-%m-%d})'
