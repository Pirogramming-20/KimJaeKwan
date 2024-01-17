from django.shortcuts import render, redirect
from .models import Idea
from .forms import IdeaForm
 
def main(request):
    # sort_select = request.GET.get('sort_select')
    ideas = Idea.objects.all()
    search_mode = request.GET.get('search_mode')
    if search_mode == '찜하기순':
        ideas = ideas.order_by('-interestedNum')
    elif search_mode == '이름순':
        ideas = ideas.order_by('title')
    elif search_mode == '등록순':
        ideas = ideas.order_by('created_date')
    elif search_mode == '최신순':
        ideas = ideas.order_by('-created_date')
    ctx = {'ideas': ideas}
    return render(request, 'ideas/idea_list.html', ctx)

def detail(request, pk):
    idea = Idea.objects.get(id=pk)
    ctx ={'idea':idea}
    return render(request, 'ideas/idea_detail.html', ctx)

def create(request):
    if request.method =='GET':
        form = IdeaForm()
        ctx ={'form': form}
        return render(request, 'ideas/idea_create.html', ctx)
    #POST일때
    form = IdeaForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
    return redirect('ideas:main')

def delete(request,pk):
    if request.method == "POST":
        Idea.objects.get(id=pk).delete()
    return redirect('ideas:main')

def update(request,pk):
    idea = Idea.objects.get(id=pk)
    if request.method == "GET":
        form = IdeaForm(instance=idea) #instance는 입력되어있는 값을 넣기 위해서
        ctx = {'form': form, 'pk': pk}
        return render(request, 'ideas/idea_update.html', ctx)
    form = IdeaForm(request.POST, request.FILES, instance=idea)
    if form.is_valid():
        form.save()
    return redirect('ideas:detail', pk)

def star_list(request,pk):
  star_toggle = Idea.objects.get(id=pk)
  if star_toggle.star:
    star_toggle.star = False
  else:
    star_toggle.star = True
  star_toggle.save()
  return redirect('ideas:main')

def star_detail(request,pk):
  star_toggle = Idea.objects.get(id=pk)
  if star_toggle.star:
    star_toggle.star = False
  else:
    star_toggle.star = True
  star_toggle.save()
  return redirect('ideas:detail',pk)