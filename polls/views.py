from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.utils import timezone

from .models import Choice, Question
from .forms import CreateQuestionForm

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[
               :5
               ]


class DetailView(generic.DetailView):
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

    model = Question
    template_name = "polls/detail.html"

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

class CreateView(generic.FormView):
    form_class = CreateQuestionForm
    template_name = "polls/create_question.html"
    success_url = reverse_lazy('polls:index')

    def form_valid(self, form):
        question_text = form.cleaned_data['question_text']
        question, created = Question.objects.get_or_create(question_text=question_text, pub_date=timezone.now())

        choice_texts = form.cleaned_data['choice_texts'].split('\n')

        for choice_text in choice_texts:
            choice_text = choice_text.strip()
            if choice_text:
                Choice.objects.create(question=question, choice_text=choice_text)

        return HttpResponseRedirect(self.success_url)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
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
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
