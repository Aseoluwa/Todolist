from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TaskSerializer
from .models import Task
# from API.Ase import serializers

# Create your views here.


@api_view(['GET'])
def apiOverview(request):
    api_urls={
        'List':'/task-list/', #(to do objects we can use)
        'Detail View': '/task-list/<str:pk>', #(allows us to see one object base on id passed in)
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>',
        'Delete': '/task-delete/<str:pk>',


    }

    return Response(api_urls)
    # return Response('API BASE POINT', safe=False)

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all().order_by('-id')
    serializers =TaskSerializer(tasks, many=True)

    return Response(serializers.data)





@api_view(['GET'])
def taskDetail(request,pk):
    tasks = Task.objects.get(id=pk)
    serializers =TaskSerializer(tasks, many=False)

    return Response(serializers.data)



@api_view(['POST'])
def taskCreate(request):


    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)



@api_view(['POST'])
def taskUpdate(request, pk):
    task= Task.objects.get(id=pk)
    serializer =TaskSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):

    task= Task.objects.get(id=pk)
    task.delete()

    return Response('Successfully deleted')    