from django.shortcuts import render,redirect
from .forms import RegisterForm, Message, SubsForm

def home(request):
   
    if request.method == "POST":
        form = Message(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Message()
    context = {
    'form':form
    }
    return render(request, 'newtonapp/homepage.html', context)
    



def blogview(request):
    if request.method == "POST":
        form = SubsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog')
    else:
        form = SubsForm()
    context = {
        'form': form
    }   
    return render(request, 'newtonapp/blog.html', context)
    
