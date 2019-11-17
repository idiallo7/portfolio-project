from django.shortcuts import render, get_object_or_404
from . models import BlogModel


def blog_home(request):
    blogs = BlogModel.objects.all()

    context ={'blogs': blogs}
    return render(request, 'blog/home.html', context)


def blog_detail(request, blog_id):
    blog_detail = get_object_or_404(BlogModel, pk=blog_id)


    context ={'blog_detail': blog_detail}
    return render(request, 'blog/detail.html',context)

