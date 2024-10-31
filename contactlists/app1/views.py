from django.shortcuts import render,redirect
from app1.models import Contacts

# Create your views here.
def home(request):
    k=Contacts.objects.all()
    return render(request,'home.html',{'contacts':k})
def add(request):
    if request.method=="POST":
        name = request.POST.get('n')
        number = request.POST.get('nu')
        place = request.POST.get('p')
        image = request.FILES.get('i', None)  # Use request.FILES for file upload

        c=Contacts.objects.create(name=name,number=number,place=place,image=image)
        c.save()
        return home(request) # Redirect to home page after saving


    return render(request,'add.html')
def detail(request,m):
    k=Contacts.objects.get(id=m)
    return render(request,'detail.html',{'contacts':k})

def edit(request,m):
    k=Contacts.objects.get(id=m)
    if request.method == "POST":
        k.name= request.POST['n']
        k.number = request.POST['nu']
        k.place = request.POST['p']


        if request.FILES.get('i') == None:
            k.save()
        else:
            k.image = request.FILES.get('i')
        k.save()
        return home(request)
    return render(request,'edit.html',{'contacts':k})

def delete(request,m):
    k=Contacts.objects.get(id=m)
    k.delete()
    return home(request)