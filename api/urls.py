from django.urls import path
from home import views
from home.views import PersonView, RegisterAPI, LoginAPI

urlpatterns = [
    path('', views.home, name='home'),
    path('person/', views.person, name='person'),
    path('classperson/',PersonView.as_view(), name='classperson'),
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
]