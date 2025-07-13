# cv_assistant/urls.py
from django.urls import path
from .views import improve_cv_view, process_cv, download_pdf

urlpatterns = [
    path('', improve_cv_view, name='cv-form'),
    path('submit/', process_cv, name='process_cv'),
    path('download-pdf/', download_pdf, name='download_pdf'),
]
