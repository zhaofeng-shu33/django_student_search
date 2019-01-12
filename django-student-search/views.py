from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
gender_map = {'M':'男','F':'女'}
# Create your views here.
def index(request):   
    context = {}
    rq=request.GET
    if(rq): # get has parameters
        student_list = []
        student_name_list=rq.get('sn','')
        for i in student_name_list.split('，'):
            result = Student.objects.filter(student_name = i)
            if(result):
                for j in result:
                    student_list.append({'name':i,'id':j.student_id,'gender':gender_map[j.student_gender],'dormitory':j.student_dormitory})
        context['students'] = student_list
    return render(request,'search.html', context)