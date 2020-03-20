from django.shortcuts import render
from django.http import HttpResponse
# from django.template.loader import get_template
# from django.template import Context
from django.shortcuts import render_to_response
from .models import Post, Author, Comment
from django.shortcuts import get_object_or_404
from .forms import PostForm
from django.core.context_processors import csrf

# Create your views here.


def post_home(request):
    home = 'Welcome home!'
    return render_to_response('home.html', {'name': home})


def post_detail(request, id=None):
    instance = get_object_or_404(Post, id=id)
    context = {'title': 'Post Detail',
               'instance': instance}
    return render(request, 'post_detail.html', context)


def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    context = {'pageTitle': 'Update post',
               'title': instance.title,
               'instance': instance,
               'form': form,
               'btnValue': 'Update'}
    return render(request, 'post_create.html', context)


def post_delete(request):
    return HttpResponse('<h1>4</h1>')


def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid:
        instance = form.save(commit=False)
        instance.save()
    context = {'pageTitle': 'Create post',
               'form': form,
               'btnValue': 'Create'}
    return render(request, 'post_create.html', context)


def post_list(request):
    queryset = Post.objects.all()
    context = {'queryset': queryset, 'title': 'Posts List'}
    return render(request, 'index.html', context)
