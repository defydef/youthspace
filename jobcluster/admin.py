from django.contrib import admin
from .models import JobCluster, Occupation, Skill, Question, Option

# Register your models here.
admin.site.register(JobCluster)
admin.site.register(Occupation)
admin.site.register(Skill)
admin.site.register(Question)
admin.site.register(Option)