from django.contrib import admin
from django.urls import include, path

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('library.books.urls')),
]

# api docs
urlpatterns += [
    path('api/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
]
