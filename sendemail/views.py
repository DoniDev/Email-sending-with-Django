from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from sendemail.forms import ContactForm


def email_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(email, message, name, ['dabduvokhidov@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    else:
        form = ContactForm()
    return render(request=request,template_name='sendemail/home.html',context={'form':form})



def success_view(request):
    return HttpResponse('Success! Thank you for your message.')
