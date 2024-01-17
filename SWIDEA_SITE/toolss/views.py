from django.shortcuts import render, redirect
from .models import Tool
from .forms import ToolForm
# Create your views here.
def main(request):
    tools = Tool.objects.all()
    ctx = {'tools':tools}
    return render(request, 'toolss/tool_list.html', ctx)

def detail(request, pk):
    tool = Tool.objects.get(id=pk)
    ctx ={'tool':tool}
    return render(request, 'toolss/tool_detail.html', ctx)

def create(request):
    if request.method == 'GET':
        form = ToolForm()
        ctx = {'form': form}
        return render(request, 'toolss/tool_create.html', ctx)

    form = ToolForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('toolss:main')

def delete(request, pk):
    if request.method == "POST":
        Tool.objects.get(id=pk).delete()
    return redirect('toolss:main')

def update(request, pk):
    tool = Tool.objects.get(id=pk)
    if request.method == 'GET':
        form = ToolForm(instance=tool)
        ctx = {'form': form, 'pk': pk}
        return render(request, 'toolss/tool_update.html', ctx)
    
    form = ToolForm(request.POST, instance=tool)
    if form.is_valid():
        form.save()
    return redirect('toolss:main')