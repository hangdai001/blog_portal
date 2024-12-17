from django.contrib import admin
from django.urls import path
from.import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.BASE, name = 'base'),
    path('home/', views.HOME, name = 'home'),
    path('category/', views.CATA, name = 'category'),
    path('contact/', views.CONT, name = 'contact'),
    path('article/<int:a_id>', views.SINGLE, name = 'article'),
    path('authentication/', views.AUTH_USER, name = 'authentication'),
    path('login/', views.HandleLogin, name = 'login'),
    path('logout/', views.HandleLogout, name = 'logout'),
    path('profile/', views.UserProfile, name = 'profile'),
    path('pgallery/', views.PHOTO, name = 'pgallery')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
