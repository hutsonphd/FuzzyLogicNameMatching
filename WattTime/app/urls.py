from django.urls import include, path, re_path
import app.views as views

app_name = "app"

urlpatterns = [
	path('', views.index, name='home' ),
	path('upload',views.upload, name='upload'),
	path('test',views.test, name='test'),
	path('reset', views.reset, name='reset')
]