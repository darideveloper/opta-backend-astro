from django.contrib import admin
from django.urls import path, include  # Asegúrate de importar `include`
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.authtoken import views as authtoken_views


urlpatterns = [
    # Redirects
    path(
        '',
        RedirectView.as_view(url='/admin/'),
        name='home-redirect-admin'
    ),
    
    # Apps
    path('admin/', admin.site.urls),
    path('', include('chatbot_app.urls')),
    path('', include('core.urls')),
    
    # Auth
    path('api/login/', authtoken_views.obtain_auth_token)
]

if not settings.STORAGE_AWS:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)