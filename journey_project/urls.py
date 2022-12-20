"""journey_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from journey.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home, name='home'),
    path("", include('journey.urls')),
    path('login/', user_login, name="user_login"),
    path('logout/', user_logout, name="user_logout"),
    path('login/user', user_homepage, name='userhome'),
    path("recommendation", recommend, name='recomendation')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = 'journey.views.page_404_page'
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        re_path(r"__dubug__", include(debug_toolbar.urls))
    ] + urlpatterns
