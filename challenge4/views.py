from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Mentor,Mentee,Blog

# Create your views here.


def home(request):
    return render(request,'challenge4/home.html')

def blog(request):
    blogs = Blog.objects.all()
    for blog in blogs:
        blog.date_post = blog.date_post.strftime('%d-%b-%Y %H:%M')
        if len(blog.content) > 250:
            blog.content = blog.content[:250]
            blog.content += '......'
    return render(request,'challenge4/blog.html',{'blogs':blogs,})

def mentor(request):
    mentors = Mentor.objects.all()
    return render(request,'challenge4/mentor.html',{'mentors':mentors,})

def mentee(request):
    mentees = Mentee.objects.all()
    return render(request,'challenge4/mentee.html',{'mentees':mentees,})


def author(request):
    return render(request,'challenge4/author.html')

def input_blog(request):
    return render(request, 'challenge4/input_blog.html')

def save_new_blog(request):
    if request.POST:
        title = request.POST['blog-title']
        content = request.POST['blog-content']
        img_url = request.POST['blog-img-url']

        proceed = Blog(title=title,content=content, img_url=img_url)
        proceed.save()

        # blogs = Blog.objects.all()
        # return render(request,'challenge4/blog.html',{'blogs':blogs})
        return redirect('blog')  #hasilnya sama dengan dua kode di atas


def article_base(request,blog_id):
    blog = get_object_or_404(Blog,pk=blog_id)
    return render(request, 'challenge4/article-base.html', {'blog': blog})
    