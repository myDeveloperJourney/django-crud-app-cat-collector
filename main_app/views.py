from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Cat
from .forms import FeedingForm
# Create your views here.

# controller code in python
# we call these view functions
def home(request):
    # each view function or "view" 
    # recieves a request object
    return render(request, 'home.html')
    # to send a response, we return it!

def about(request):
    contact_details = 'you can reach support at support@catcollector.com' 
    return render(request, 'about.html', {
        'contact': contact_details
    }) # this is the same as res.render()

def cat_index(request):
    cats = Cat.objects.all()
    return render(request, 'cats/index.html', {
        'cats': cats
    })

def cat_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    feeding_form = FeedingForm()
    return render(request, 'cats/detail.html', {
        'cat': cat,
        'feeding_form': feeding_form
    })

def add_feeding(request, cat_id):
    form = FeedingForm(request.POST)
    
    if form.is_valid():
        new_feeding = form.save(commit=False) 
        # ^ save in memory, but do NOT commit to the db!
        new_feeding.cat_id = cat_id 
        # making the association to the cat
        new_feeding.save() # now it's saved to the database
    
    return redirect('cat-detail', cat_id)


class CatCreate(CreateView):
    model = Cat
    fields = ['name', 'breed', 'description', 'age']

class CatUpdate(UpdateView):
    model = Cat
    fields = ['breed', 'description', 'age']

class CatDelete(DeleteView):
    model = Cat
    success_url = '/cats/'