from django.urls import include, path, re_path
import app.views as views

app_name = "app"

urlpatterns = [
	path('', views.index, name='home' ),
]