from django.urls import path
from . import views

urlpatterns = [
	path ('', views.index, name='index'),
	path ('index_version.html/', views.index, name='index_version'),
	path ('login.html/', views.login, name='login'),
	path ('machines/', views.machine_list_view, name='machines'),
	path ('machine/<pk>' ,views.machine_detail_view, name='machine-detail'),
]

