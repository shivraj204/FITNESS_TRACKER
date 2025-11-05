from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('log-workout/', views.log_workout, name='log_workout'),
    path('log-daily/', views.log_daily, name='log_daily'),
    path('send-reminder/', views.send_reminder, name='send_reminder'),
]