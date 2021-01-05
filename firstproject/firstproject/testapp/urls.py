from django.contrib import admin
from django.urls import path
from testapp import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.show),
    path('home1/',views.show1),
    path('home2/',views.show2),
    path('home3/',views.show3),
    path('home4/',views.show4),
    path('home5/',views.show5),
    path('home6/',views.show6),
    path('home7/',views.show7),

]

