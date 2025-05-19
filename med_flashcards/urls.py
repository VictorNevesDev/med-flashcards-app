from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # App 
    path("api/v1/", include("app.urls")),
]
