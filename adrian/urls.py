
from reports.urls import router
from django.contrib import admin
from django.urls import include, path # new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('reports.urls')), 
]