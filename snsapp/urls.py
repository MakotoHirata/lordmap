from django.urls import path
from .views import Home, MyPost, DetailPost, CreatePost, UpdatePost                     #Home, MyPost追加
from . import views

urlpatterns = [
    path('',views.Login,name='login'),
    path("logout",views.Logout,name="logout"),
    path("register", views.AccountRegistration.as_view(), name='register'),
    path("home/",Home.as_view(),name="home"),           #追加
    path('mypost/', MyPost.as_view(), name='mypost'),  
    path('detail/<int:pk>', DetailPost.as_view(), name='detail'), #追加
    path('detail/<int:pk>/update', UpdatePost.as_view(), name='update'),
    path('create/', CreatePost.as_view(), name='create'),
]