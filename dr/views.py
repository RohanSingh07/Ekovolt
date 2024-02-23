from django.shortcuts import render
from .tasks import execute_script
from time import sleep

# Create your views here.
def homepage(request):
    result = execute_script.delay()
    task_id = result.task_id
    print(task_id)
    return render(request,"index.html",{"task_id":task_id})