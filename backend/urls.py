from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('auth/', include('authentication.urls')),
    path('crm/', include('crm.urls')),
    path('sales/', include('sales.urls')),
    path('business/', include('business.urls')),
    path('inventory/', include('inventory.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)