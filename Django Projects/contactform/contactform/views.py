from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail

def index(request):
    if request.method == 'POST':
        name = request.POST.get('full-name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        data = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message
        }

        message = '''
        New Message: {}

        From: {}

        
        with regards,
        {}
        '''.format(data['message'], data['email'], data['name'])
        send_mail(data['subject'], message, '', ['abhishek21022002@gmail.com'] )

    return render(request, 'contactform/index.html', {})