from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='planner-home'),
    path('calendar/', views.calendar, name='planner-calendar'),
]
