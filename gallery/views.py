from django.shortcuts import render,redirect
from .models import Category, Photos
from .forms import CategoryCreate
from django.http import HttpRequest, HttpResponse

# Create your views here.

def index(request):
    photo = Photos.objects.all()
   
    
    ctx = {'photo':photo}
    
   
    return render(request, 'index.html', ctx)

       
def upload(request):
    upload=CategoryCreate()
    if request.method=='POST':
        upload=CategoryCreate(request.POST,request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse('Your form is wrong')
    else:
        return render(request,'gallery/upload_form.html',{'upload':upload})

def update(request,blog_id):
    blog_id=int(blog_id)
    try:
     blog_up=Category.objects.get(id=blog_id)
    except Category.DoesNotExist:
        return redirect('index')
    blog_form=CategoryCreate(request.POST or None,instance=blog_up)
    if blog_form.is_valid():
        blog_form.save()
        return redirect('index')
    return render (request,'gallery/upload_form.html',{'upload':blog_form})

def delete(request,blog_id):
     
    blog_id=int(blog_id)
    try:
        blog_up=Category.objects.get(id=blog_id)
    except Category.DoesNotExist:
        return redirect('gallery/index.html')
    blog_up.delete()
    return redirect('gallery/index.html')

def about(request):
    return render(request, 'about.html')