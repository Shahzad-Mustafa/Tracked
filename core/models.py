from django.db import models
from django.utils.text import slugify


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
