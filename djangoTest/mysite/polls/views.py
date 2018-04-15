from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.utils import timezone

from .models import Question, Dhoice
from .knn import kevin

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    output = ', '.join([q.question_text for q in latest_question_list])
#    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list
    }
#    return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
#    try:
#        question = Question.objects.get(pk=question_id)
#    except Question.DoesNotExist:
#        raise Http404("Question does not exist")
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
    #return HttpResponse("You're looking at question %s." % question_id)



def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        asdf = request.POST['1']
        asdfasdf = request.POST['2']
        near = kevin(asdf, asdfasdf, int(timezone.now().hour))
    except (KeyError, Dhoice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "no choice selected",
        })
    else:
#        selected_choice.votes += 1
#       selected_choice.save()
        return render(request, 'polls/results.html', {'text': asdf, 'textt': asdfasdf, 'near1': near[0], 'near2': near[1]})
#    return HttpResponse("You're voting on question %s." % question_id)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

# Create your views here.
