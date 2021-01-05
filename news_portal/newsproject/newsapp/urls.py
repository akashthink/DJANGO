from django.contrib import admin
from django.urls import path
from newsapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.display),
    path('h2/',views.emp_info),
]
