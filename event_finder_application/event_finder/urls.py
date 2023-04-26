from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('event_finderapp/', include('event_finderapp.urls')),
    path('admin/', admin.site.urls),
]
