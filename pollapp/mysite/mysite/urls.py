from django.contrib import admin
from django.urls import include,path
from poll import views

urlpatterns = [
    path('poll/',include('poll.urls')),
    path('admin/', admin.site.urls),
    
]
