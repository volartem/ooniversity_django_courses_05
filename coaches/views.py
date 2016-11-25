from django.shortcuts import render
from .models import Coach
from courses.models import Course
# Create your views here.

def detail(request, coach_id):
    coach = Coach.objects.get(id=int(coach_id))
    couch_cours = Course.objects.filter(coach=coach.id)
    assistant_cours = Course.objects.filter(assistant=coach.id)
    return render(request, 'coaches/detail.html', {'coach': coach, 'couch_cours': couch_cours, 'assistant_cours': assistant_cours})