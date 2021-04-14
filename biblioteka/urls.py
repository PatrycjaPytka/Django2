from . import views
from django.urls import path

urlpatterns = [
    path('', views.glowna, name = 'glowna'),
    path('email/', views.email, name = 'email'),
    path('new_form/', views.new_form, name = 'new_form'),
]