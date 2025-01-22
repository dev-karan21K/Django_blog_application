from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from blogs.models import Blog, Category

def post_by_category(request, category_id):
    posts = Blog.objects.filter(status='Published', category=category_id)
    # try:
    #     category = Category.objects.get(pk=category_id)
    # except:
    #     return redirect('home') 
    category = get_object_or_404(Category, pk=category_id)
    context = {
        'posts': posts,
        'category': category
    }
    return render(request, 'post_by_category.html', context)
