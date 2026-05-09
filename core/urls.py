from django.urls import path
from .views import HomeView, ContactView, ResumeDownloadView

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('resume/download/', ResumeDownloadView.as_view(), name='resume_download'),
]
