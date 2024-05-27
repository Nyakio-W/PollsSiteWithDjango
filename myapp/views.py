from django.db.models import F
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
#from django.template import loader
from django.urls import reverse
from django.views import generic

from .models import Choice, Question

# Create your views here.
'''def index(request):
  #return HttpResponse('<h1>Hello, world.</h1>')
  latest_question_list = Question.objects.order_by("-pub_date")[:5]
  context = {
      "latest_question_list": latest_question_list,
  }
  #template = loader.get_template("polls/index.html")
  
  return render(request, "polls/index.html", context)
  #return HttpResponse(template.render(context,' request))
  #output = ", ".join([q.question_text for q in latest_question_list])
  #return HttpResponse(output) '''
class IndexView(generic.ListView):
  template_name = "polls/index.html"
  context_object_name = "latest_question_list"

  def get_queryset(self):
    return Question.objects.order_by("-pub_date")[:5]

'''Return the last five published questions.'''
  
''' function based viewdef detail(request, question_id):
  #return HttpResponse("You're looking at question %s." % question_id)
   question = get_object_or_404(Question, pk=question_id)
   return render(request, "polls/detail.html", {"question": question})'''

class DetailView(generic.DetailView):
  model = Question
  template_name = "polls/detail.html"

'''def results(request, question_id):
  response = "You're looking at the results of question %s."
  return HttpResponse(response % question_id)'''

class ResultsView(generic.DetailView):
  model = Question
  template_name = "polls/results.html"



def vote(request, question_id):
  #return HttpResponse("You're voting on question %s." % question_id)
  question = get_object_or_404(Question, pk=question_id)
  try:
    selected_choice =question.choice_set.get(pk=request.POST["choice"])
  except (KeyError, Choice.DoesNotExist):
      # Redisplay the question voting form.
      return render(
          request,
          "polls/detail.html",
          {
              "question": question,
              "error_message": "You didn't select a choice.",
          },
      )
  else:
      selected_choice.votes = F("votes") + 1
      selected_choice.save()
      # Always return an HttpResponseRedirect after successfully dealing
      # with POST data. This prevents data from being posted twice if a
      # user hits the Back button.
      return HttpResponseRedirect(reverse("myapp:results", args=(question.id,)))