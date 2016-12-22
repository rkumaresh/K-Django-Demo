# Create your views here.
import json
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.views.decorators.http import require_http_methods

from music.forms import LoginForm, ToDoForm
from music.models import Feedback

@require_http_methods(["GET", "POST"])
def select(request):

    id_ = request.GET.get('id', "")

    if id_ == "" :
        return HttpResponse("Welcome to Music")

    obj = Feedback.select(id_)

    return HttpResponse(obj)

@transaction.atomic()
def insert(request):
    id_ = request.GET.get('id', "")
    desc_ = request.GET.get('desc', "")
    Feedback.insert(id_, desc_)
    return select(request)

def forms(request):
    return render(request, 'music/login.html')

@require_http_methods(["GET", "POST"])
def login(request):
    if request.method == 'POST':
        loginForm = LoginForm(request.POST)
        todoForm = ToDoForm(initial={'userName' : loginForm.data.get('userName')})
        return render(request, 'music/todo.html', {'toDoFormData': todoForm})

        # return render_to_response("todo.html", {'toDoFormData', todoForm})

    return HttpResponse("Unsupported HTTP Method " + request.method)


@require_http_methods(["GET", "POST"])
def startSurvey(request):
    if request.method == 'POST':
        loginForm = LoginForm(request.POST)
        todoForm = ToDoForm(initial={'userName' : loginForm.data.get('userName')})
        return render(request, 'music/survey-1.html', {'startSurveyForm': todoForm})

        # return render_to_response("todo.html", {'toDoFormData', todoForm})

    return HttpResponse("Unsupported HTTP Method " + request.method)


