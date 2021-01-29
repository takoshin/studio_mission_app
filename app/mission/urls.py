
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static 
from django.conf import settings

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', include('manual.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)