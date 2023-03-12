from django.shortcuts import render,get_object_or_404

from .models import blog

def hello(request):
    blogs=blog.objects.order_by('-Date') [:5]
    return render(request,"my_blog/blog.html",{"blogs":blogs})
def details(request,blog_id):
    blogs=get_object_or_404(blog,pk=blog_id)
    return render(request,"my_blog/details.html",{'blogs':blogs})