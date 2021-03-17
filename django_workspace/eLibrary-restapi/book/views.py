from django.shortcuts import render
from .models import Book
from .bookdto import BookSerializer
from rest_framework.decorators import api_view, schema
from rest_framework.response import Response


@api_view(['GET'])
def bookList(request):
    books = Book.objects.all() # DB에 있는 모든 레코드들을 조회
    
    # 조회된 레코드들을 직렬화, 다수의 레코드들을 직렬화 해야하기 때문에, many=True 지정
    serializer = BookSerializer(instance=books, many=True)
    return Response(serializer.data) # 직렬화된 데이터를 넘겨준다.

@api_view(['GET'])
def bookDetail(request, pk):
    try:
        book = Book.objects.get(isbn=pk) # 주어진 id가 db에 존재하는지 검사하기 위해 try-except구문 사용
    except:
        return Response("존재하지 않는 isbn입니다.")
    serializer = BookSerializer(instance=book)
    return Response(serializer.data)

@api_view(['DELETE'])
def bookDelete(request, pk):
    # 삭제를 할 때, 직렬화를 필요로하지 않는다.(i.e. 직렬화는 요청한 데이터를 넘길 때 사용)
    try:
        book = Book.objects.get(isbn=pk)
    except:
        return Response('존재하지 않는 isbn입니다.')
    book.delete()
    return Response('Deleted!')

@api_view(['PUT'])
def bookUpdate(request, pk):
    try:
        book = Book.objects.get(isbn=pk)
    except:
        return Response("존재하지 않는 isbn입니다.")
    
    for key in request.data.keys():
        if key == 'image_URL ': book.image_URL = request.data[key]
        elif key == 'author': book.author = request.data[key]
        elif key == 'isbn': return Response('ISBN은 수정 불가능 합니다.')
        elif key == 'title': book.title = request.data[key]
        elif key == 'desc': book.desc = request.data[key]
        elif key == 'edition': book.edition = request.data[key]
        elif key == 'rating': book.rating = request.data[key]
        else: return Response("key 값을 다시 확인하세요")

    book.save()
    return Response("업데이트 완료")
    

@api_view(['POST'])
def bookCreate(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid(): 
        serializer.save()
        return Response(serializer.data)
    return Response('유효하지 않는 데이터입니다.')