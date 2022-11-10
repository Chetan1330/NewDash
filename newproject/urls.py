from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path(r'new_admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),

    path('', include('authentication.urls')),



    path('', include('DasboardApp.urls'))

]