# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Board, Topic, Post
from .forms import NewTopicForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    ''' Home page '''
    boards = Board.objects.all()
    return HttpResponse(render(request, 'home.html', {'boards': boards}))


def board_topics(request, pk):
    ''' The topics of the board '''
    #try:
    #    board = Board.objects.get(pk=pk)
    #except Board.DoesNotExist:
    #    raise Http404
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'topics.html', {'board': board})

@login_required
def new_topic(request, pk):
    '''Create a new topic'''
    board = get_object_or_404(Board, pk=pk)
    user = User.objects.first()     # get the currently logged user
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = user
            topic.save()

            # Add a new data to Post table
            Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=user
            )
            return redirect('board_topics', pk=board.pk)    # redirect to the created topic page
    else:
        form = NewTopicForm()
    return render(request, 'new_topic.html', {'board': board, 'form': form})