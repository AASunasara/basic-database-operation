from django.views.generic import TemplateView
from django.shortcuts import render
from studentdata.form import DaTa


class HomeView(TemplateView):
    template_name = 'studentdata/studentdata.html'

    def get(self, request):
        form = DaTa()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = DaTa(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.user = request.user
            student.save()
            student_name = form.cleaned_data['student_name']
            student_roll_no = form.cleaned_data['student_roll_no']
            study_field = form.cleaned_data['study_field']
            args = {'student_name': student_name, 'form': form, 'student_roll_no': student_roll_no,
                    'study_field': study_field}
            return render(request, self.template_name, args)

