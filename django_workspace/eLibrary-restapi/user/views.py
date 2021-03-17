from django.shortcuts import render
from .models import User
from .userdto import UserSerializer
from rest_framework.decorators import api_view, schema
from rest_framework.response import Response


@api_view(['GET'])
def userList(request):
    users = User.objects.all() # DB에 있는 모든 레코드들을 조회
    
    # 조회된 레코드들을 직렬화, 다수의 레코드들을 직렬화 해야하기 때문에, many=True 지정
    serializer = UserSerializer(instance=users, many=True)
    return Response(serializer.data) # 직렬화된 데이터를 넘겨준다.

@api_view(['GET'])
def userDetail(request, pk):
    try:
        user = User.objects.get(email=pk)
    except:
        return Response("존재하지 않는 이메일입니다.")
    serializer = UserSerializer(instance=user)
    return Response(serializer.data)

@api_view(['DELETE'])
def userDelete(request, pk):
    # 삭제를 할 때, 직렬화를 필요로하지 않는다.(i.e. 직렬화는 요청한 데이터를 넘길 때 사용)
    try:
        user = User.objects.get(email=pk)
    except:
        return Response('존재하지 않는 이메일입니다.')
    user.delete()
    return Response('Deleted!')

@api_view(['PUT'])
def userUpdate(request, pk):
    try:
        user = User.objects.get(email=pk)
    except:
        return Response("존재하지 않는 이메일입니다.")

    for key in request.data.keys():
        if key == 'firstname': user.firstname = request.data[key]
        elif key == 'lastname': user.lastname = request.data[key]
        elif key == 'email': return Response("이메일은 수정할 수 없습니다.")
        elif key == 'password': user.password = request.data[key]
        elif key == 'address': user.address = request.data[key]
        elif key == 'phonenumber': user.phonenumber = request.data[key]
        else: return Response("key 값을 다시 확인하세요")

    user.save()
    return Response("업데이트 완료")

@api_view(['POST'])
def userCreate(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid(): 
        serializer.save()
        return Response(serializer.data)
    return Response('유효하지 않는 데이터입니다.')