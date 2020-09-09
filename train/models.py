from django.db import models

# Create your models here.
class Subject(models.Model):
    name = model.CharField(max_length=50)
    instructor = models.ForeignKey('Instructor', on_delete=models.SET_NULL, null=True)
    schedule = models.DateTimeField(auto_now_add=True)
    age_group = models.CharField(MaxLength=50)
    prerequisite = models.CharField(MaxLength=100)
    material = models.CharField(MaxLength=100)
    comment = models.CharField(MaxLength=2000)

class Instructor(models.Model):
    name = model.CharField(max_length=50)
    grade = model.CharField(max_length=50)
    school = model.CharField(max_length=50)
    bio = model.CharField(max_length=2000)

class Student(models.Model):
    name =  model.CharField(max_length=50)
    email =  model.EmailField(max_length=100)
    grade = model.IntegerField()
    state =  model.CharField(max_length=50)
    subject = ManyToManyField(Subject, help_text='Select a Class') 

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('student_detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.name}'