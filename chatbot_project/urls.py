from django.contrib import admin
from django.urls import path, include  # Asegúrate de importar `include`
from django.views.generic import RedirectView

urlpatterns = [
    # Redirects
    path(
        '',
        RedirectView.as_view(url='/admin/'),
        name='home-redirect-admin'
    ),
    
    # Apps
    path('admin/', admin.site.urls),
    path('', include('chatbot_app.urls')),  # Redirige al `chatbot_app`
]
