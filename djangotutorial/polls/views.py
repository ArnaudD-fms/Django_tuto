from django.db.models import F, Sum, Max
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question
from .utils import minimax


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


class AllQuestionsView(generic.ListView):
    template_name = "polls/all.html"

    def get_queryset(self):
        """Return all published questions."""
        return Question.objects.all()


class FrequencyView(generic.DetailView):
    model = Question
    template_name = "polls/frequency.html"
    context_object_name = "question"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["frequencies"] = self.object.get_choices()
        return context

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
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))


def statistics(request):
    nbr_sondages = Question.objects.count()
    nbr_choix = Choice.objects.count()
    nbr_votes = Choice.objects.aggregate(somme=Sum('votes'))['somme']
    moyenne_par_sondage = nbr_votes / nbr_sondages
    (question_la_moins_populaire, question_la_plus_populaire) = minimax()
    id_derniere_question = Question.objects.aggregate(max=Max('id'))['max']
    derniere_question = Question.objects.get(pk=id_derniere_question)

    return render(request, 'polls/statistics.html', {
         'nbr_sondages': nbr_sondages,
         'nbr_choix': nbr_choix,
         'nbr_votes': nbr_votes,
         'moyenne_par_sondage': moyenne_par_sondage,
         'question_la_plus_populaire': question_la_plus_populaire,
         'question_la_moins_populaire':
         question_la_moins_populaire,
         'derniere_question': derniere_question,
    })


def add(request):
    return render(request, 'polls/add.html')


def confirm_add(request):
    question_text = request.POST['question_text'].strip()
    if question_text:
        question = Question(question_text=question_text,
                            pub_date=timezone.now())
        question.save()
        return render(request, 'polls/confirm_add.html')
    else:
        return render(request, 'polls/add.html', {
            'error_message': "You didn't enter a question text",
        })
