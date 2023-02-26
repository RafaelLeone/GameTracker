from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('explorer/', include('explorer.urls')),
    path("api/", include("gametracker.base.urls")),
    path("api/accounts/", include("gametracker.accounts.urls")),
    path("api/tasks/", include("gametracker.tasks.urls")),
    path("api/games/", include("gametracker.games.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
