from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',include('root.urls')),
    path('', include('accounts.urls')),
    path('', include('courses.urls')),
    path('', include('users.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
