from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from rest_framework.routers import DefaultRouter
from restaurant import views
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('', lambda request: redirect('restaurant/', permanent=False)),  # Redirect root to /restaurant/
    path('admin/', admin.site.urls),
    path('restaurant/', include('restaurant.urls')),
    path('api/', include(router.urls)),  # API endpoints for bookings
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api-token-auth/', obtain_auth_token),
]