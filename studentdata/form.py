from django import forms
from .models import Student


class DaTa(forms.ModelForm):
    student_name = forms.CharField()
    student_roll_no = forms.IntegerField()
    study_field = forms.CharField()

    class Meta:
        model = Student
        fields = ('student_name', 'student_roll_no', 'study_field')
