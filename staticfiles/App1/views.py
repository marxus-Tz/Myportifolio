from django.shortcuts import render, redirect
from .models import projects,ContactMessage
from .forms import HireMeForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def cv(request):
    return render(request, 'cv.html')

def project(request):
    context= {
        'title': 'projects',
        'projects':projects.objects.all()
    }   
    # return render(request, 'projects.html',{'projects':projects.objects.all()})
    return render(request, 'projects.html', context)

def hire_me(request):
    if request.method == 'POST':
        form = HireMeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            hire_date = form.cleaned_data['hire_date']
            # Save the form data to the database
            contact_message = ContactMessage.objects.create(
                subject=subject,
                email=email,
                message=message,
                hire_date=hire_date
            )
            # Optionally, perform additional actions like sending emails, notifications, etc.
            # Redirect to a success page or do something else
            return redirect('success')
    else:
        form = HireMeForm()
    return render(request, 'contacts.html', {'form': form})

def success(request):
    return render(request, 'success.html')
