from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = 'index'),
    path('navbar/', views.navbar, name = 'navbar'),
    path('userreg/',views.userreg, name = 'userreg'),
    path('insertuser/',views.insertuser, name = 'insertuser'),
]
