from django.urls import path
from .import views

app_name = 'articles'


urlpatterns = [
    path('', views.index, name="list"),
    path('<slug:slug>/', views.detail, name="detail"),
]