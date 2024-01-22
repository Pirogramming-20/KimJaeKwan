from django.shortcuts import render, redirect
from .forms import CommentForm
# Create your views here.
def comment_create(request, pk):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts:detail', pk=pk)
        else:
            ctx = {
                'form': form,
            }
            return render(request, 'comments/comments_create.html', ctx)
    else:
        form = CommentForm()
        ctx = {
                'form': form,
        }
        return render(request, 'comments/comments_create.html', ctx)
