from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from datacsv import views as user_views

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('register/', user_views.register, name='register'),
                  path('', include('datacsv.urls')),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
