from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from .models import Question




def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('bigweb/index.html')
    context = {                                                   #The context is a dictionary mapping template variable names to Python objects.
        'latest_question_list': latest_question_list,            #zmienia zmienną w obiekt
    }
    return render(request, 'bigweb/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'bigweb/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)    




   # Note that once we’ve done this in all these views, we no longer need to import loader and HttpResponse (you’ll want to keep HttpResponse if you still have the stub methods for detail, results, and vote).

#The render() function takes the request object as its first argument, a template name as its second argument and a dictionary as its optional third argument. It returns an HttpResponse object of the given template rendered with the given context.