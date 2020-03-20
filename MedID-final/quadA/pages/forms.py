from django import forms
from .models import *


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    occupation = forms.CharField()


class SignUpPatientForm(forms.ModelForm):
    class Meta:
        model = SignUpPatientModel
        fields = '__all__'


class SignUpDoctorForm(forms.ModelForm):
    class Meta:
        model = SignUpDoctorModel
        fields = '__all__'


class SignUpPathLabForm(forms.ModelForm):
    class Meta:
        model = SignUpPathLabModel
        fields = '__all__'


class SignUpMedicalInsuranceForm(forms.ModelForm):
    class Meta:
        model = SignUpMedicalInsuranceModel
        fields = '__all__'


class MedicalHistoryForm(forms.ModelForm):
    class Meta:
        model = MedicalHistoryModels
        fields = '__all__'


class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = PrescriptionModel
        fields = '__all__'


class ReportForm(forms.ModelForm):
    class Meta:
        model = ReportModel
        fields = '__all__'
