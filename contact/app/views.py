from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import *
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def home(request):
    return render(request,'home.html')

def add_contact(request):
    if request.method == 'POST':
        cname = request.POST.get('cname')
        cemail = request.POST.get('cemail')
        cno = request.POST.get('cno')

    
        if Contact.objects.filter(cno=cno).exists():
            contact = Contact.objects.get(cno=cno)
            return render(request, 'Exist.html', {'contact': contact})
        else:
            contact = Contact(cname=cname, cemail=cemail, cno=cno)
            contact.save()
            return HttpResponseRedirect(reverse('view'))

    return render(request, 'add_contact.html')

def view(request):
    contact=Contact.objects.all()
    return render(request,'view.html',{'contact':contact})

def update(request,pk):
    contact=Contact.objects.get(pk=pk)
    if request.method == 'POST':
        cname=request.POST.get('cname')
        cemail=request.POST.get('cemail')
        cno=request.POST.get('cno')
        contact.cname=cname
        contact.cemail=cemail
        contact.cno=cno
        contact.save()
        return HttpResponseRedirect(reverse('view'))
    return render(request,'add_contact.html',{'contact':contact})

def delete(request,pk):
    contact=Contact.objects.get(pk=pk)
    if request.method == 'POST':
        contact.delete()
        return HttpResponseRedirect(reverse('view'))
    return render(request,'delete.html',{'contact':contact})


def search(request):
    if request.method == 'POST':
        cno = request.POST.get('no')
        try:
            pno = Contact.objects.get(cno=cno)
            return render(request, 'search.html', {'pno': pno})
        except Contact.DoesNotExist:
            return render(request, 'search.html', {'error': 'No contact found with that number.'})
    else:
        return render(request, 'search.html')  # For GET requests, show the search form



