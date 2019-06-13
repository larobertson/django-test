from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

def index(request):
  latest_question_list = Question.objects.order_by('-pub_date')[:5]
  context = {
    'latest_question_list': latest_question_list,
  }
  return render(request, 'polls/index.html', context)
  # The render() function takes the request object as its first argument, a template name as 
  # its second argument and a dictionary as its optional third argument. It returns an 
  # HttpResponse object of the given template rendered with the given context.

def detail(request, question_id):
  return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
  response = "You're looking at the results of question %s."
  return HttpResponse(response % question_id)

def vote(request, question_id):
  return HttpResponse("You're voting on question %s" % question_id)