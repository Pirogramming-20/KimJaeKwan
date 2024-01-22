from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from comments.models import Comment
from comments.forms import CommentForm
from django.db.models import Q

# Create your views here.
def main(request):
    #모든 게시물 가져오기
    posts = Post.objects.all()
    search_query = request.GET.get('q', '')
    if search_query:
        posts = Post.objects.filter(Q(title__icontains=search_query))
    # 각 게시물에 대한 연관된 코멘트 가져오기
    post_comments = {}
    for post in posts:
        comments = Comment.objects.filter(post=post)
        post_comments[post.id] = comments
    
    #print("여기", post_comments) 
    ctx = {
        'posts': posts,
        #검색 결과가 없는 경우를 위해 추가
        #'comments': comments,
        'comments': post_comments.get(post.id, []) if posts else [],
        'search_query': search_query,
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

def detail(request, pk):
    post = Post.objects.get(id=pk)
    form = CommentForm()
    ctx ={
        'post': post,
        'comments': post.comment_set.all(),
        'form': form
    }
    return render(request, 'posts/post_detail.html', ctx)

# def comment_create(request, pk):
#     post = Post.objects.get(pk=pk)
#     comment_form = CommentForm(request.POST)
#     if comment_form.is_valid():
#         comment = comment_form.save(commit=False)
#         comment.post = post
#         comment.save()
#     return redirect('posts:detail', post.pk)

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

@csrf_exempt
def delete_ajax(request, pk):
    if request.method == 'POST':
        comment = Comment.objects.get(id=pk)
        comment_id = comment.id
        comment.delete()
        return JsonResponse({'id': comment_id})
    
@csrf_exempt
def create_ajax(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(id=pk)
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()

            # 새로운 댓글 데이터를 응답으로 반환
            response_data = {
                'id': comment.id,
                'content': comment.content,
            }

            return JsonResponse(response_data)

    return JsonResponse({'error': '유효하지 않은 폼 데이터'})

def search_view(request):
    search_query = request.GET.get('q', '')
    results = Post.objects.filter(Q(title__icontains=search_query))

    response_data = {
        'results': [{'id': post.id, 'title': post.title} for post in results]
    }
    return JsonResponse(response_data)