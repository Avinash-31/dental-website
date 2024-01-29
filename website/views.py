from django.shortcuts import render
from django.shortcuts import redirect
from django.core.mail import send_mail

def home(request):
    return render(request, 'pages/index.html', {})


def about(request):
    return render(request, 'pages/about.html', {})


def service(request):
    return render(request, 'pages/service.html', {})


def pricing(request):
    return render(request, 'pages/pricing.html', {})


def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        
        #send an email
        # send_mail(
        #     message_name, #subject
        #     message, #message
        #     message_email, #from email
        #     ['avinash.80031@gmail.com'], #to email
        # )
        return render(request, 'pages/contact.html', {'message_name':message_name})
    return render(request, 'pages/contact.html', {})


def blog(request):
    return render(request, 'pages/blog.html', {})


def blog_details(request):
    return render(request, 'pages/blog-details.html', {})

def appointment(request):
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        dateOfAppointment = request.POST['dateOfAppointment']
        time = request.POST['time']
        formMessage = request.POST['formMessage']
            
        return render(request,'pages/appointment.html',{
            'name':name,
            'phone':phone,
            'email':email,
            'address':address,
            'dateOfAppointment':dateOfAppointment,
            'time':time,
            'formMessage':formMessage,
        })
    return redirect('home')