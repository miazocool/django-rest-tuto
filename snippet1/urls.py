from django.urls import path
from snippet1 import views

urlpatterns = [
    path('snippet1/', views.snippet_list),
    path('snippet1/<int:pk>/', views.snippet_detail),
]