
from django.contrib import admin


from django.urls import path, include

from django.conf import settings

from django.conf.urls.static import static


# from elements import views as e_views

# from authusers import views as auth_views

from authy.views import UserProfile, follow


urlpatterns = [

    path('admin/', admin.site.urls),

    path('users/', include('authy.urls')),

    path('', include('post.urls')),

    path('message/', include('directs.urls')),

    path('notifications/', include('notification.urls')),


    # profile

    path('<username>/', UserProfile, name='profile'),

    path('<username>/saved/', UserProfile, name='profilefavourite'),

    path('<username>/follow/<option>/', follow, name='follow'),


]

# This is used for media ans ststic work in deployment

if settings.DEBUG:

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

