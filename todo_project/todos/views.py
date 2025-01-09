from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view


from .models import ToDoTask
from .serializers import ToDoTaskSerializer

# Create your views here.
class ToDoListDisplay(APIView):
    def get(self, request):
        tasks = ToDoTask.objects.all()
        serializer = ToDoTaskSerializer(tasks, many=True)
        return Response(serializer.data)

class ToDoCreate(APIView):
    def post(self, request):
        serializer = ToDoTaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def get_object(pk):
    try:
        return ToDoTask.objects.get(pk=pk)
    except ToDoTask.DoesNotExist:
        return None
    
class ToDoGetDetail(APIView):
    def get(self, request, pk):
        task = get_object(pk)
        if task is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ToDoTaskSerializer(task)
        return Response(serializer.data)
    
class ToDoEdit(APIView):
    def put(self, request, pk):
        task = get_object(pk)
        if task is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ToDoTaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ToDoDelete(APIView):
    permission_classes = [AllowAny]
    def delete(self, request, pk):
        task = get_object(pk)
        if task is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE'])    
def delete_todo(self, request, pk):
    task = get_object(pk)
    if task is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    task.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class DeleteAllTasks(APIView):
    def delete(self, request):
        ToDoTask.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
