from citas.views import inicio
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='index'),

]
