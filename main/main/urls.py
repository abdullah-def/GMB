
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path('admin/', admin.site.urls),
    path("ckeditor/", include("ckeditor_uploader.urls")),

    path('', include('accounts.urls')),
    path('app/', include('app.urls')),
    path('payment/', include('payment.urls')),
    path("blog/", include("lotus.urls"), name="blog"),
    path("api/", include("api.urls")),



]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
