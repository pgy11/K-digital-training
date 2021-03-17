from django.shortcuts import render
from .models import Todo
from .tododto import TodoSerializer
from rest_framework.decorators import api_view, schema
from rest_framework.response import Response


@api_view(['GET'])
def todoList(request):
    todos = Todo.objects.all()
    serializer = TodoSerializer(instance=todos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def todoDetail(request, pk):
    try:
        todo = Todo.objects.get(id=pk)
    except:
        return Response("존재하지 않는 id입니다.")
    serializer = TodoSerializer(instance=todo)
    return Response(serializer.data)

@api_view(['DELETE'])
def todoDelete(request, pk):
    try:
        todo = Todo.objects.get(id=pk)
    except:
        return Response('존재하지 않는 id입니다.')
    todo.delete()
    return Response('Deleted!')

@api_view(['PUT'])
def todoUpdate(request, pk):
    try:
        todo = Todo.objects.get(id=pk)
    except:
        return Response("존재하지 않는 id입니다.")
    serializer = TodoSerializer(instance=todo, data=request.data)
    if serializer.is_valid(): serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def todoCreate(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid(): serializer.save()
    return Response(serializer.data)