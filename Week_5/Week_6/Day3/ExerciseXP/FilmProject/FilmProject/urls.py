from django.contrib import admin
from films.views import *
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('film/', include('films.urls')),
]
