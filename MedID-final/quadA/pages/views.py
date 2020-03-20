from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.staticfiles.templatetags.staticfiles import static
import pyqrcode
from pyqrcode import QRCode
from pyzbar.pyzbar import decode
from PIL import Image
import os
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import tensorflow as tf
from datetime import date
from PIL import Image, ImageDraw, ImageFont

from .forms import *
from .models import *

def graph(height, weight, date):
    import pandas as pd
    import matplotlib.pyplot as plt
    from matplotlib import style
    style.use('ggplot')

    height = height.split(',')
    weight = weight.split(',')
    
    bmi = list()
    for i in range(len(height)):
        x = (int(height[i]) ** 2)/int(weight[i])
        bmi.append(x)

    x=date
    y=bmi

    x1 = date
    y1 = weight

    plt.plot(x,y,'g',label='BMI', linewidth=5)
    plt.plot(x1, y1, 'g', label='Weight', linewidth=5)
    plt.title('Graph for BMI and Weight')
    plt.ylabel('Weight & BMI')
    plt.xlabel('Date')
    plt.legend()

    plt.savefig('static/img2.png')

# Create your views here.


def home_view(response, *args, **kwargs):
    return render(response, 'home.html', {})


def sign_up_view(request):
    if request.POST.get('occupation', False) == 'Patient':
        form = SignUpPatientForm(request.POST, request.FILES or None)

        if form.is_valid():
            form.save()

    elif request.POST.get('occupation', False) == 'Doctor':
        form = SignUpDoctorForm(request.POST, request.FILES or None)

        if form.is_valid():
            form.save()

    elif request.POST.get('occupation', False) == 'Medical Insurance':
        form = SignUpMedicalInsuranceForm(request.POST, request.FILES or None)

        if form.is_valid():
            form.save()

    else:
        form = SignUpPathLabForm(request.POST, request.FILES or None)

        if form.is_valid():
            form.save()

    return render(request, 'signup.html', {})


def login_view(request):
    email_entered = request.POST.get('email', False)
    password_entered = request.POST.get('password', False)

    if request.POST.get('occupation', False) == 'Patient':
        x = SignUpPatientModel.objects.filter(email=email_entered)
        x = x.values()

        if len(x) != 0:
            x = x[0]

            if x['password'] == password_entered:
                request.session['patient_email'] = email_entered
                request.session['password'] = password_entered
                request.session.set_expiry(7200)
                return redirect('/patient/')

            else:
                return redirect('/')

        else:
            return redirect('/')

    elif request.POST.get('occupation', False) == 'Doctor':
        x = SignUpDoctorModel.objects.filter(email=email_entered)
        x = x.values()

        if len(x) != 0:
            x = x[0]

            if x['password'] == password_entered:
                request.session['doctor_email'] = email_entered
                request.session['password'] = password_entered
                request.session.set_expiry(7200)
                return redirect('/doctor/')

            else:
                return redirect('/')

        else:
            return redirect('/')

    elif request.POST.get('occupation', False) == 'Test Lab':
        x = SignUpPathLabModel.objects.filter(email=email_entered)
        x = x.values()

        if len(x) != 0:
            x = x[0]

            if x['password'] == password_entered:
                request.session['pathlab_email'] = email_entered
                request.session['password'] = password_entered
                request.session.set_expiry(7200)
                return redirect('/pathlab/')

            else:
                return redirect('/')

        else:
            return redirect('/')

    elif request.POST.get('occupation', False) == 'Medical Insurance':
        x = SignUpMedicalInsuranceModel.objects.filter(email=email_entered)
        x = x.values()

        if len(x) != 0:
            x = x[0]

            if x['password'] == password_entered:
                request.session['medical_insurance_email'] = email_entered
                request.session['password'] = password_entered
                request.session.set_expiry(7200)
                return redirect('/medical-insurance/')

            else:
                return redirect('/')

        else:
            return redirect('/')


def patient_dashboard_view(request):
    email = request.session.get('patient_email', False)

    if email:
        data = SignUpPatientModel.objects.filter(email=email)
        data = data.values()
        data = data[0]

        return render(request, 'patient_home_page.html', data)

    else:
        return redirect('/')


def doctor_dashboard_view(request):
    email = request.session.get('doctor_email', False)

    if request.method == 'POST':
        p_email = request.POST.get('p_email', False)

        obj = SignUpPatientModel.objects.filter(email=p_email)
        obj = obj.values()

        if len(obj) > 0:
            request.session['p_email'] = p_email

            if(request.session.get('p_password', False)):
                del request.session['p_password']

    if email:
        context = {}
        if(request.session.get('p_email', False)):
            p_email = request.session.get('p_email', False)

            if(request.session.get('p_password', False)):
                p_password = request.session.get('p_password', False)
                context = {'email': p_email, 'password': p_password}

            else:
                context = {'email': p_email}

        return render(request, 'doctor_page1.html', context)

    else:
        return redirect('/')


def pathlab_dashboard_view(request):
    email = request.session.get('pathlab_email', False)

    if email:
        return render(request, 'pathlab_page1.html', {})

    else:
        return redirect('/')


def medical_insurance_dashboard_view(request):
    email = request.session.get('medical_insurance_email', False)

    if email:
        return render(request, 'medical_insurance_page1.html', {})

    else:
        return redirect('/')

def generate_qr_code(request):
    email = request.session.get('patient_email', False)

    obj = SignUpPatientModel.objects.filter(email = email)
    obj = obj.values()
    obj = obj[0]

    name = obj['name']
    dob = obj['birth_date']
    blood_group = obj['blood_group']
    aadhar = obj['aadhar_no']

    
    image = Image.new('RGB', (900,600), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('/Library/Fonts/Arial.ttf',15)
    import random
    import os
    import datetime
    import qrcode

    (x, y) = (10, 40)

    color = 'rgb(255, 0, 0)' # black color
    font = ImageFont.truetype('/Library/Fonts/Arial.ttf', 30)
    draw.text((x, y),"Name: "+ name, fill=color, font=font)

    (x, y) = (10, 90)
    color = 'rgb(0, 0, 0)' # black color 
    draw.text((x, y), "Date of Birth: "+ str(dob), fill=color, font=font)

    (x, y) = (10, 140)
    bloodgroup=blood_group
    color = 'rgb(0, 0, 0)' # black color 
    draw.text((x, y),"Blood Group: "+ bloodgroup, fill=color, font=font)

    (x, y) = (10, 190)
    adhaarno= aadhar
    color = 'rgb(0, 0, 0)' # black color 
    draw.text((x, y), "Adhaar Number: "+str(adhaarno), fill=color, font=font)
     
    image.save('code.png')

    img = qrcode.make(str(name)+','+str(adhaarno))   # this info. is added in QR code, also add other things
    img.save('qr.jpeg')

    til = Image.open('code.png')
    im = Image.open('qr.jpeg') #25x25
    til.paste(im,(500,0))
    til.save('static/qr/code.png')

    url = static('/qr/code.png')

    return redirect(url)


def scan_qrcode_view(request):
    if request.method == 'POST':
        a = request.FILES
        a = a['image']

        with open('abc.png', 'wb+') as f:
            for chunks in a.chunks():
                f.write(chunks)

        f.close()

        x = decode(Image.open('abc.png'))
        print(x)

        os.remove('abc.png')

        x = x[0][0]
        x = x.decode('utf-8')
        message = x.split(',')
        name = message[0]
        aadhar = message[1]

        request.session['name'] = name
        request.session['aadhar'] = aadhar

    return redirect('../')


def pnemonia_create_view(request):
    url = {
        'gif': static('/pneumonia/loading.gif')
    }

    if request.method == 'POST':
        a = request.FILES['image']

        with open('image.jpeg', 'wb+') as f:
            for chunks in a.chunks():
                f.write(chunks)

        f.close()

        return redirect('diagnosis/')

    return render(request, 'pnemonia.html', url)


def diagnosis_view(request):
    url = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

    graph = tf.get_default_graph()

    with graph.as_default():
        model = load_model(url + '/static/model.hdf5')

    data = image.load_img('image.jpeg', target_size=(224, 224, 3))
    data = image.img_to_array(data)
    data = np.expand_dims(data, axis=0)

    with graph.as_default():
        predicted = model.predict(data)

    result = predicted

    if(result[0][0] > result[0][1]):
        predicted_class = 0
        percentage = result[0][0] * 100
    else:
        predicted_class = 1
        percentage = result[0][1] * 100

    indices = {0: 'Normal', 1: 'Pneumonia'}

    predicted_class = indices[predicted_class]

    os.remove('image.jpeg')

    return render(request, 'predict.html', {'prediction': predicted_class, 'accuracy': percentage})


def patient_medical_update_view(request):
    if request.method == 'GET':
        return render(request, 'patient_update_medical_history.html', {})

    email = request.session.get('patient_email', False)
    query_set = MedicalHistoryModels.objects.filter(email=email)
    query_set = query_set.values()

    post = request.POST.copy()

    today = date.today()

    post['email'] = email
    post['date'] = str(today)

    if len(query_set) != 0:
        query_set = query_set[0]
        post['height'] = query_set['height'] + ',' + post['height']
        post['weight'] = query_set['weight'] + ',' + post['weight']
        post['date'] = query_set['date'] + ',' + post['date']

    request.POST = post

    form = MedicalHistoryForm(request.POST)
    form.fields['other_illness'].required = False
    form.fields['other_allergy'].required = False
    form.fields['medication'].required = False

    if form.is_valid():
        query_set = MedicalHistoryModels.objects.filter(
            email=email)
        query_set = query_set.values()

        if(len(query_set) > 0):
            obj = MedicalHistoryModels.objects.get(email=email)
            obj.delete()

        form.save()

    else:
        print(form.errors)

    return render(request, 'patient_update_medical_history.html', {})


def blood_donors_view(request):
    blood_group = request.POST.get('blood_group', False)
    pincode = request.POST.get('pincode', False)
    locality = request.POST.get('locality', False)

    query_set = SignUpPatientModel.objects.filter(
        blood_group=blood_group, pincode=pincode)

    query_set = query_set.values()
    return render(request, 'blood_donors.html', {'query_set': query_set, 'length': len(query_set)})


def doctor_search_view(request):
    if request.method == 'POST':
        speciality = request.POST.get('speciality', False)
        pincode = request.POST.get('pincode', False)
        locality = request.POST.get('locality', False)

        query_set = SignUpDoctorModel.objects.filter(pincode=pincode)
        query_set = query_set.values()
        return render(request, 'doctor_search.html', {'query_set': query_set, 'length': len(query_set)})

    return render(request, 'doctor_search.html', {})


def patient_summary_view(request):
    email = request.session.get('patient_email', False)

    if not email:
        email = request.session.get('p_email', False)

    query_set1 = SignUpPatientModel.objects.filter(email=email)
    query_set1 = query_set1.values()
    query_set1 = query_set1[0]
    name = query_set1['name']

    query_set1 = MedicalHistoryModels.objects.filter(email=email)
    query_set1 = query_set1.values()
    query_set1 = query_set1[0]

    date = query_set1['date']
    date = date.split(',')

    temp = dict()

    for key, val in query_set1.items():
        if type(val) == int:
            temp[key] = val

        elif type(val) == str and len(val) != 0:
            temp[key] = val

        elif val == True:
            temp[key] = val

    str1 = str()
    str2 = str()

    for key, val in temp.items():
        l = key.split('_')

        if l[0] == 'illness':
            str1 = str1 + l[1] + ', '

        elif l[0] == 'allergy':
            str2 = str2 + l[1] + ', '

    str1 = str1[:-2]
    str2 = str2[:-2]

    context = dict()

    context['name'] = name

    for key, val in temp.items():
        if type(val) == bool:
            continue

        else:
            context[key] = val

    if len(str1) != 0:
        context['illness'] = str1

    if len(str2) != 0:
        context['allergy'] = str2

    height = context['height']
    weight = context['weight']

    context['height'] = context['height'].split(',')
    context['height'] = context['height'][0]
    context['weight'] = context['weight'].split(',')
    context['weight'] = context['weight'][0]

    graph(height, weight, date)

    return render(request, 'patient_summary.html', context)


def upload_prescription_view(request):
    if request.method == 'POST':
        obj = SignUpPatientModel.objects.filter(request.session.get('aadhar', false))
        obj = obj.values()
        print(obj)
        # post = request.POST.copy()
        # post['email'] = request.session.get('p_email', False)
        # request.POST = post

        # form = PrescriptionForm(request.POST, request.FILES or None)
        # if form.is_valid():
        #     form.save()

    return render(request, 'doctor_upload_prescription.html', {})


def upload_report_view(request):
    if request.method == 'POST':
        post = request.POST.copy()
        post['email'] = request.session.get('p_email', False)
        request.POST = post

        form = ReportForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()

    return render(request, 'doctor_upload_report.html', {})

def patient_view_prescription_view(request):
    email = request.session.get('patient_email', False)
    obj = PrescriptionModel.objects.filter(email = email)
    obj = obj.values()
    temp = list()
    for item in obj:
        temp.append(item['image'])

    context = dict()
    for i in range(len(temp)):
        context[temp[i]] = i

    context = {'context': context}

    return render(request, 'patient_view_prescription.html', context)


def patient_view_report_view(request):
    email = request.session.get('patient_email', False)
    obj = ReportModel.objects.filter(email=email)
    obj = obj.values()
    temp = list()
    for item in obj:
        temp.append(item['image'])

    context = dict()
    for i in range(len(temp)):
        context[temp[i]] = i

    context = {'context': context}

    print(context)

    return render(request, 'patient_view_report.html', context)

def doctor_patient_summary_view(request):
    return render(request, 'doctor_patient_summary.html', {})

def doctor_view_prescription(request):
    return render(request, 'doctor_view_prescription.html', {})


def doctor_view_report(request):
    return render(request, 'doctor_view_report.html', {})
