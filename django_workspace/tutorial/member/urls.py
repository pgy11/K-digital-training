from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.memberList, name='members'),
    path('detail/<str:pk>/', views.memberDetail, name='detail'),
    path('create/', views.memberCreate, name='create'),
    path('update/<str:pk>/', views.memberUpdate, name='update'),
    path('delete/<str:pk>/', views.memberDelete, name='delete'),
    #path('api_admin/', include('rest_framework.urls', namespace='rest_framework')),
    #path('api/v1/', include('rest_framework.urls', namespace='api')),
    #url('', schema_view),
]