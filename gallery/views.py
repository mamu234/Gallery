from django.shortcuts import render
from .models import Category, Photos

# Create your views here.

def index(request):
    photo = Photos.objects.all()
   
    
    ctx = {'photo':photo}
    
   
    return render(request, 'index.html', ctx)

       
def about(request):
    return render(request, 'about.html')

def category(request):
    return render(request, 'category.html')

def location(request):
    return render(request, 'location.html')

def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_categories = Category.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"categories": searched_categories})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})