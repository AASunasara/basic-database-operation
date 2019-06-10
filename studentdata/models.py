from django.db import models
from django.forms import ModelForm


class Student(models.Model):
    student_name = models.CharField(max_length=25)
    student_roll_no = models.IntegerField()
    study_field = models.CharField(max_length=25)


class PickForm(ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
