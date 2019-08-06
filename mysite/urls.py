from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('run/', include('blog.urls')),
    path('', include('blog.urls')),
]
