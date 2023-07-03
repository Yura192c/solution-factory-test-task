from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    # path('auth/', include('djoser.urls.jwt')),

    path('', include('routers')),
    path('account/', include('src.user.urls')),
    path('ui/', include(('src.stats.urls', 'stats'), namespace='stats')),
]
