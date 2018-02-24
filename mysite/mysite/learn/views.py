from django.shortcuts import get_object_or_404,render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views import generic

from .models import Choice,Question

class IndexView(generic.ListView):
	template_name = 'learn/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		return Question.objects.order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
	model = Question
	template_name = 'learn/detail.html'

class ResultsView(generic.DetailView):
	model = Question
	template_name = 'learn/results.html'


def vote(request,question_id):
	#return HttpResponse("You're voting on question %s." % question_id)
	question = get_object_or_404(Question,pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError,Choice.DoesNotExist):
		return render(request,'learn/detail.html',{
			'question':question,
			'error_message':"You didn't select a choice.",
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('learn:results',args=(question.id,)))
