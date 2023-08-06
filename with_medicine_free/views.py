from django.shortcuts import render, redirect, get_object_or_404
from .forms import Free_board_Form, Free_board_CommentForm
from django.utils import timezone
from .models import Free_board, Free_Comment

# Create your views here.
def free_read(request):
    free_board = Free_board.objects.all()
    return render(request, 'free_read.html', {'free_board':free_board})

def free_create(request):
    if request.method == 'POST':
        form = Free_board_Form(request.POST)
        if form.is_valid():
            form = form.save(commit = False)
            form.pub_date = timezone.now()
            form.save()
            return redirect('free_read')
    else:
        form = Free_board_Form
        return render(request, 'free_create.html', {'form': form})
    
def free_detail(request, id):  
    free_board = get_object_or_404(Free_board, id = id)  
    if request.method == 'POST':
        form = Free_board_CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.free_board_id = free_board
            comment.save()
            return redirect('free_detail', id)
    else:
        form = Free_board_CommentForm
        return render(request, 'free_detail.html', {'form' : form, 'free_board' : free_board})  

def free_update(request, id):
    free_board = get_object_or_404(Free_board, id = id)
    if request.method == 'POST':
        form = Free_board_Form(request.POST, instance=free_board)
        if form.is_valid():
            form = form.save(commit = False)
            form.pub_date = timezone.now()
            form.save()
            return redirect('free_read')
    else:
        form = Free_board_Form(instance=free_board)
        return render(request, 'free_update.html', {'form' : form})
    
def free_delete(request, id):
    free_update = get_object_or_404(Free_board, id = id)
    free_update.delete()
    return redirect('free_read')

def free_comment_delete(request, id, c_id):
    comment = get_object_or_404(Free_Comment, id=c_id)
    comment.delete()
    return redirect('free_detail',id)

def free_comment_update(request, id, com_id):
    comment = Free_Comment.objects.get(id = com_id)
    form = Free_board_CommentForm(instance=comment)
    if request.method == "POST":
        form = Free_board_CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('free_detail', id)
    return render(request, 'free_comment_update.html', {'form':form})