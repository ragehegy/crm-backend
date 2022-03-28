from django.contrib import admin
from django.urls import path, include

from django.conf import settings, urls
from django.conf.urls.static import static

from adminsite.admin import custom_admin

admin.site = custom_admin
admin.autodiscover()

urlpatterns = [
    path('auth/', include('authentication.urls')),
    path('crm/', include('crm.urls')),
    path('sales/', include('sales.urls')),
    path('business/', include('business.urls')),
    path('inventory/', include('inventory.urls')),
    path('plan/', include('plan.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)