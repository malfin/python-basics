from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('mainapp.urls', namespace='main')),
    path('accounts/', include('authapp.urls', namespace='authapp')),
    # path('accounts/', include(('django.contrib.auth.urls', 'auth'), namespace='auth')),
    path('admin/', admin.site.urls),
]
