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
    return render(request, 'blog/homepage.html', context)
    



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
    return render(request, 'blog/blog.html', context)
    
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('login')
    else:
        form = RegisterForm()
    context = {
        'form':
        form
    }
    return render(request, 'blog/signup.html', context)
