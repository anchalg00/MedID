"""quadA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='homepage'),

    path('login/', login_view, name='login'),

    path('sign-up/', sign_up_view, name='sign up page'),

    path('patient/', patient_dashboard_view, name='patient dashboard'),
    path('patient/generate/', generate_qr_code, name='generate qr code'),
    path('patient/update-medical-history/', patient_medical_update_view,
         name='patient medical history update'),
    path('patient/summary/', patient_summary_view, name='patient summary'),
    path('patient/view-prescription/',
         patient_view_prescription_view, name='view prescription'),
    path('patient/view-report/', patient_view_report_view, name='view report'),

    path('doctor/', doctor_dashboard_view, name='doctor dashboard'),
    path('doctor/scan-qrcode/', scan_qrcode_view, name='upload'),
    path('doctor/upload-prescription/',
         upload_prescription_view, name='upload prescription'),
    path('doctor/upload-report/', upload_report_view, name='upload report'),
    path('doctor/patient-summary/',
         doctor_patient_summary_view, name='patient summary'),
    path('doctor/view-prescription/',
         doctor_view_prescription, name='view prescriptioin'),
    path('doctor/view-report/',
         doctor_view_report, name='view report'),

    path('pathlab/', pathlab_dashboard_view, name='pathlab dashboard'),

    path('medical-insurance/', medical_insurance_dashboard_view,
         name='medical insurance dashboard'),

    path('pneumonia-check/', pnemonia_create_view, name='pneumonia ml model'),
    path('pneumonia-check/diagnosis/',
         diagnosis_view, name='pneumonia diagnosis'),

    path('blood-donor/', blood_donors_view, name='blood donors'),

    path('doctor-search/', doctor_search_view, name='search for doctor'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
