from django.shortcuts import render
from django.shortcuts import redirect
from django.core.mail import send_mail
from datetime import datetime
# from .forms import Profileform
from . import models

def home(request):
    Pricings = models.pricing.objects.all()
    Dentists = models.dentist.objects.all()
    Reviews = models.review.objects.all()
    return render(request, 'pages/index.html', {
        'pricings':Pricings,
        'dentists':Dentists,
        'reviews':Reviews,
    })


def about(request):
    return render(request, 'pages/about.html', {})


def service(request):
    return render(request, 'pages/service.html', {})


def pricing(request):
    return render(request, 'pages/pricing.html', {})

def blog(request):
    return render(request, 'pages/blog.html', {})


def blog_details(request):
    return render(request, 'pages/blog-details.html', {})

def contact(request):
    if request.method == "POST":
        Name = request.POST['message-name']
        Email = request.POST['message-email']
        Msg = request.POST['message']
        
        # Save the message in the database
        Contact = models.contact(
            name=Name,
            email=Email,
            msg=Msg,
        )
        Contact.save()

        return render(request, 'pages/contact.html', {'message_name': Name})

    return render(request, 'pages/contact.html', {})

def appointment(request):

    if request.method == 'POST':
        Name = request.POST['name']
        Phone = request.POST['phone']
        Email = request.POST['email']
        Address = request.POST['address']
        DateOfAppointment = request.POST['dateOfAppointment']
        Slot = request.POST['slot']
        Msg = request.POST['formMessage']
        
        appointment = models.appointment(
            name=Name,
            mobile=Phone,
            email=Email,
            address=Address,
            msg=Msg,
            slot=Slot,
            dateOfAppointment=DateOfAppointment,
            timestamp=datetime.now(),
        )
        appointment.save()
        print("Appointment saved")
        return render(request,'pages/appointment.html',{
            'name':Name,
            'phone':Phone,
            'email':Email,
            'address':Address,
            'dateOfAppointment':DateOfAppointment,
            'time':Slot,
            'formMessage':Msg,
        })
    return redirect('home')  