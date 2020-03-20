from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(SignUpPatientModel)
admin.site.register(SignUpDoctorModel)
admin.site.register(SignUpPathLabModel)
admin.site.register(MedicalHistoryModels)
admin.site.register(SignUpMedicalInsuranceModel)
admin.site.register(PrescriptionModel)
admin.site.register(ReportModel)
