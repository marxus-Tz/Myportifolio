from django import forms
from .models import ContactMessage
from django.core.mail import send_mail
from django.conf import settings

class HireMeForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    hire_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
   

def save(self):
    name = self.cleaned_data['name']
    subject = self.cleaned_data['subject']
    email = self.cleaned_data['email']
    message = self.cleaned_data['message']
    hire_date = self.cleaned_data['hire_date']

    contact_message = ContactMessage.objects.create(
        name=name,
        subject=subject,
        email=email,
        message=message,
        hire_date=hire_date
    )

    # Send the email
    send_mail(
        'New Contact Message',
        f'Name: {name}\nSubject: {subject}\nEmail: {email}\nMessage: {message}\nHire Date: {hire_date}',
        settings.EMAIL_HOST_USER,
        ['maxiusemmanueli@gmail.com'],  # Replace with your personal Gmail account
        fail_silently=False,
    )
    return contact_message
