from django.urls import path
from . import views

urlpatterns=[
    path('lists/',views.alllists.as_view(),name='alllists'),
    path('login/',views.Login.as_view(),name='login'),
]