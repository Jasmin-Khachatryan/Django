from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("pizza.urls")),
    path("burger/", include("burgers.urls")),
    path("restaurant/", include("restaurant.urls")),
    path("search/", include("search.urls")),
    path("__debug__/", include("debug_toolbar.urls")),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
