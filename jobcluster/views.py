from django.shortcuts import render
from django.views.generic import ListView
from .models import Question

# Create your views here.
def home(request):
    return render(request, 'home.html')

def assessment(request):
    return render(request, 'assessment.html')
	
class AssessmentView(ListView):
#referred from mentors.views.MentorListView
    model = Question
    context_object_name = 'questions'
    template_name = 'assessment.html'

