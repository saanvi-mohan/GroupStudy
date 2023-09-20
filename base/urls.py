from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home),
    path('pages/<str:pk>',views.Rooms),
    path('create-room/',views.createRoom),
    path('edit-room/<str:pk>',views.editRoom),
    path('edit-user/',views.editUser),
    path('delete-room/<str:pk>',views.deleteRoom),
    path('login/',views.loginUser),
    path('logout/',views.logoutUser),
    path('register/',views.registerUser),
    path('delete-message/<str:pk>',views.deleteMessage),
    path('profile/<str:pk>',views.Profile),
    path('browse-topic/',views.browseTopic),
    path('activity/',views.activity)
]