from django.urls import path
from . import views
urlpatterns = [
    path("<int:id>/", views.index, name='index'),
    path("",views.home,name="home"),
    path("create/",views.newlist,name="createlist"),
    path("logout/",views.user_logout,name="user_logout"),
    path("getlist/",views.getlist,name="getlist"),
]