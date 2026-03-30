from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include("apps.bookmodule.urls")),   # الصفحة الرئيسية
    path('admin/', admin.site.urls),
    path('books/', include("apps.bookmodule.urls")),
    path('users/', include("apps.usermodule.urls")),
]