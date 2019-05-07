from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('simplemooc.apps.core.urls')),
    path('conta/', include('simplemooc.apps.accounts.urls')),
    path('cursos/', include('simplemooc.apps.courses.urls')),
    path('forum/', include('simplemooc.apps.forum.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
