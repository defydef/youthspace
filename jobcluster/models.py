from django.db import models

# Job Clusters
class JobCluster(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)
	
    def __str__(self):
        return self.name

# Occupation
class Occupation(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)
    jobcluster = models.ForeignKey(JobCluster, related_name='occupations')
	
    def __str__(self):
        return self.name

# Skill
class Skill(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)
    jobcluster = models.ForeignKey(JobCluster, related_name='skills')
	
    def __str__(self):
        return self.name
		
# Questions
class Question(models.Model):
    description = models.CharField(max_length=300)
    q_img = models.ImageField(upload_to='img/question', blank=True)

    def __str__(self):
        return self.description

# Answer Options
class Option(models.Model):
    question = models.ForeignKey(Question, related_name='options')
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description

