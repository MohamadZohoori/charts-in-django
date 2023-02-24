from django.contrib import admin
from django.urls import path
from chartapp import views
  
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home.as_view()),
    path('api/', views.chart.as_view()),
]