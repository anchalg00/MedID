from django.db import models

# Create your models here.


class SignUpPatientModel(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    birth_date = models.DateField()
    gender = models.CharField(max_length=10)
    blood_group = models.CharField(max_length=3)
    aadhar_no = models.IntegerField()
    address = models.CharField(max_length=200)
    pincode = models.IntegerField()
    occupation = models.CharField(max_length=10)
    profile_pic = models.FileField(upload_to='profile_pics/')
    verify = models.BooleanField()


class SignUpDoctorModel(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    birth_date = models.DateField()
    gender = models.CharField(max_length=10)
    blood_group = models.CharField(max_length=3)
    aadhar_no = models.IntegerField()
    address = models.CharField(max_length=200)
    pincode = models.IntegerField()
    occupation = models.CharField(max_length=10)
    profile_pic = models.FileField(upload_to='profile_pics/')
    verify = models.BooleanField()


class SignUpPathLabModel(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    birth_date = models.DateField()
    gender = models.CharField(max_length=10)
    blood_group = models.CharField(max_length=3)
    aadhar_no = models.IntegerField()
    address = models.CharField(max_length=200)
    pincode = models.IntegerField()
    occupation = models.CharField(max_length=10)
    profile_pic = models.FileField(upload_to='profile_pics/')
    verify = models.BooleanField()


class SignUpMedicalInsuranceModel(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    birth_date = models.DateField()
    gender = models.CharField(max_length=10)
    blood_group = models.CharField(max_length=3)
    aadhar_no = models.IntegerField()
    address = models.CharField(max_length=200)
    pincode = models.IntegerField()
    occupation = models.CharField(max_length=18)
    profile_pic = models.FileField(upload_to='profile_pics/')
    verify = models.BooleanField()


class MedicalHistoryModels(models.Model):
    email = models.EmailField()
    date = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    height = models.CharField(max_length=100)
    weight = models.CharField(max_length=100)
    illness_cancer = models.BooleanField()
    illness_aids = models.BooleanField()
    illness_heart_disease = models.BooleanField()
    illness_diabetes = models.BooleanField()
    illness_asthma = models.BooleanField()
    illness_renal_dialysis = models.BooleanField()
    other_illness = models.CharField(max_length=200, default='None')
    allergy_pollen = models.BooleanField()
    allergy_dust = models.BooleanField()
    allergy_nuts = models.BooleanField()
    allergy_dairy = models.BooleanField()
    allergy_wheat = models.BooleanField()
    other_allergy = models.CharField(max_length=200, default='None')
    medication = models.CharField(max_length=200, default='None')


class PrescriptionModel(models.Model):
    email = models.EmailField()
    date = models.DateField()
    image = models.FileField(upload_to='prescription/')


class ReportModel(models.Model):
    email = models.EmailField()
    date = models.DateField()
    image = models.FileField(upload_to='reports/')
