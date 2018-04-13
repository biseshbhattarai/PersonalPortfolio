from django.shortcuts import render,redirect
from .forms import RegisterForm, Message, SubsForm
from django.views.generic import ListView, DetailView
from .models import Blog

def home(request):
    blogitem = Blog.objects.all()
    if request.method == "POST":
        form = Message(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Message()
    context = {
    'form':form,
    'blogitem':blogitem
    }
    return render(request, 'blog/index.html', context)
    




    
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





class BlogDetail(DetailView):
    template_name = 'blog/blog_content.html'
    model = Blog



def blog(request):
    blogitems = Blog.objects.all()
    if request.method == 'POST':
        form = SubsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs')
    else:
        form = SubsForm()
    return render(request, 'blog/blogs.html', {"blogitems": blogitems, "form": form})