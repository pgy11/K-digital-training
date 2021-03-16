from django.shortcuts import render
# vscode의 pylint가 에러 취급(unable to import rest_framework)하지만 무시해도된다.
# from rest_framework import serializers, viewsets
from .models import Member
from .memberdto import MemberSerializer
from rest_framework.decorators import api_view, schema
from rest_framework.response import Response

# quick start에서 제공된 방법
"""
class MemberViewSet(viewsets.ModelViewSet): 
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
"""

# 데코레이터를 이용한 방법
@api_view(['GET'])
def memberList(request):
    members = Member.objects.all() # db에 있는 모든 데이터 조회해서
    serializer = MemberSerializer(instance=members, many=True) # 위의 결과를 직렬화한다.
    return Response(serializer.data)

@api_view(['GET'])
def memberDetail(request, pk):
    member = Member.objects.get(id=pk)
    serializer = MemberSerializer(instance=member)
    return Response(serializer.data)

@api_view(['DELETE'])
def memberDelete(request, pk):
    member = Member.objects.get(id=pk)
    member.delete()
    return Response('Deleted!')

@api_view(['PUT'])
def memberUpdate(request, pk):
    member = Member.objects.get(id=pk)
    serializer = MemberSerializer(instance=member, data=request.data)
    if serializer.is_valid(): serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def memberCreate(request):
    serializer = MemberSerializer(data=request.data)
    if serializer.is_valid(): serializer.save()
    return Response(serializer.data)