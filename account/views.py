from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from . models import Profile, CustomersEmail, CustomersMessages

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('profile')
    else:
        form = SignUpForm()
        return render(request, 'signup.html', {'form':form})

    return render(request, 'signup.html', {'form':form })

def profile(request):
    try:
        profile = request.user.profile
        messages.success(request, "Your already created a profile !!!")
        return redirect('search')
    except Profile.DoesNotExist:
        
        if request.method == 'POST':
            company_name = request.POST['company_name']
            job_title = request.POST['job_title']
            # get user
            user = request.user
            profile = Profile(user=user, company_name=company_name, job_title=job_title)
            profile.save()
            messages.success(request, "Your profile has been succefully been created!!!")
            return redirect('search')
        else:
            return render(request, 'profile.html')

def signin(request):
    if request.user.is_authenticated:
       messages.success(request, "You Are Already Logged In!")
       return redirect('search')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            # Authenticate
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You Have Been Logged In!")
                return redirect('search')
            else:
                messages.success(request, "There Was An Error Logging In, Please Try Again...")
                return redirect('signin')
        else:
            return render(request, 'signin.html')

def signout(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out...")
    return redirect('signin')

def subscribe(request):
    if request.method == 'POST':
        print('yes')
        email = request.POST['email']

        if CustomersEmail.objects.filter(email=email).exists():
            messages.success(request, "Email already EXISTS ,,,")
            return redirect('search')
        else:
            newsletter = CustomersEmail(email=email)
            newsletter.save()
            messages.success(request, "Thanks For Subcribing!!! expect best content on how to collect defaulted accounts.")
    return redirect('search')


def launchAcomplain(request):
    context = {
       
    }
    return render(request, 'message.html', context)

def contactMessage(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        contact = CustomersMessages(name=name, email=email, subject=subject, message=message)
        contact.save()
        messages.success(request, 'Thanks for reaching out, we will reply within two working days')
        return redirect('search')

def terms(request):
    context = {
       
    }
    return render(request, 'terms.html', context)

def privacy(request):
    context = {
       
    }
    return render(request, 'privacy.html', context)
