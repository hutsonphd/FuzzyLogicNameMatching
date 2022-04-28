from django.urls import include, path, re_path
import app.views as views

app_name = "app"

urlpatterns = [
	path('', views.index, name='home' ),
	path('upload_entso',views.upload_entso, name='upload_entso')
]