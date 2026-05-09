import logging
from pathlib import Path

from django.conf import settings
from django.contrib import messages
from django.core.cache import cache
from django.core.mail import send_mail
from django.http import FileResponse, Http404
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.views import View
from django.views.generic import TemplateView

from .forms import ContactForm
from .models import Education, Experience, HeroBadge, Profile, Project, SkillCategory

logger = logging.getLogger(__name__)

CONTACT_RATE_LIMIT = 5    # max submissions
CONTACT_RATE_WINDOW = 3600  # per hour (seconds)


def _get_profile():
    return Profile.objects.first() or Profile()


def _check_rate_limit(ip):
    key = f'rl_contact_{ip}'
    count = cache.get(key, 0)
    if count >= CONTACT_RATE_LIMIT:
        return False
    cache.set(key, count + 1, timeout=CONTACT_RATE_WINDOW)
    return True


def _home_context(contact_form=None):
    profile = _get_profile()
    return {
        'profile':            profile,
        'hero_badges':        HeroBadge.objects.filter(is_active=True),
        'skills_by_category': SkillCategory.objects.prefetch_related('skills').filter(
                                  skills__isnull=False).distinct(),
        'experiences':        Experience.objects.all(),
        'projects':           Project.objects.filter(is_active=True),
        'educations':         Education.objects.all(),
        'contact_form':       contact_form or ContactForm(),
    }


class HomeView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(_home_context())
        return context


class ContactView(View):
    def post(self, request):
        ip = (
            (request.META.get('HTTP_X_FORWARDED_FOR') or '').split(',')[0].strip()
            or request.META.get('REMOTE_ADDR', 'unknown')
        )
        if not _check_rate_limit(ip):
            messages.error(request, 'Too many submissions from your IP. Please try again in an hour.')
            return redirect('core:home')

        form = ContactForm(request.POST)
        if form.is_valid():
            contact_msg = form.save(commit=False)
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                contact_msg.ip_address = x_forwarded_for.split(',')[0].strip()
            else:
                contact_msg.ip_address = request.META.get('REMOTE_ADDR')
            contact_msg.save()

            profile = _get_profile()
            try:
                notification_body = render_to_string(
                    'core/emails/contact_notification.txt',
                    {'msg': contact_msg}
                )
                send_mail(
                    subject=f'Portfolio Contact: {contact_msg.subject}',
                    message=notification_body,
                    from_email=None,
                    recipient_list=[profile.email or settings.CONTACT_EMAIL],
                    fail_silently=False,
                )
                autoresponse_body = render_to_string(
                    'core/emails/contact_autoresponse.txt',
                    {'msg': contact_msg, 'profile': profile}
                )
                send_mail(
                    subject=f'Thanks for reaching out — {profile.name}',
                    message=autoresponse_body,
                    from_email=None,
                    recipient_list=[contact_msg.email],
                    fail_silently=False,
                )
            except Exception:
                logger.exception('Failed to send contact email')

            messages.success(request, "Your message has been sent! I'll get back to you soon.")
            return redirect('core:home')

        return render(request, 'core/index.html', _home_context(contact_form=form))

    def get(self, request):
        return redirect('core:home')


class ResumeDownloadView(View):
    def get(self, request):
        resume_path = Path(settings.BASE_DIR) / 'static' / 'resume' / 'Shahzad_Ali_Resume.pdf'
        if not resume_path.exists():
            raise Http404('Resume not found')
        response = FileResponse(open(resume_path, 'rb'), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="Shahzad_Ali_Resume.pdf"'
        return response
