from django.shortcuts import render,HttpResponse
from .models import Contact
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'index.html')
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        sub = request.POST['sub']
        msg = request.POST['msg']
        
        if len(name)<2 or len(email)<3 or len(msg)<10 or len(msg)<4:
            messages.error(request,"Please fill the form correctly!")
        else:
            contact = Contact(name=name,email=email,sub=sub,msg=msg)
            contact.save();
            messages.success(request,"Your message has been successfully sent!")
    return render(request,'contact.html')
