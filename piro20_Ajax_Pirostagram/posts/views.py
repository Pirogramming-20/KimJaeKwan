from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

# Create your views here.
def main(request):
    posts = Post.objects.all()
    ctx = {
        'posts':posts
    }
    return render(request, 'posts/posts_list.html', ctx)

def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts:main')
        else:
            ctx = {
                'form': form,
            }
            return render(request, 'posts/post_create.html', ctx)
    else:
        form = PostForm()
        ctx = {
                'form': form,
        }
        return render(request, 'posts/post_create.html', ctx)
    
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def like_ajax(request):
    req = json.loads(request.body)
    post_id = req['id']

    post = Post.objects.get(id=post_id)

    post.like = not post.like
    
    post.save()

    return JsonResponse({'id': post_id, 'liked': post.like})