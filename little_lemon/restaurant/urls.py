from django.urls import path
from . import views

urlpatterns = [
    # HTML views
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('menu/', views.menu, name="menu"),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),
    path('bookings/', views.bookings, name="bookings"),

    # REST API views — avoid path conflict with 'menu/' above
    path('api/menu/', views.MenuItemView.as_view(), name="api-menu"),
    path('api/menu/<int:pk>/', views.SingleMenuItemView.as_view(), name="api-single-menu"),
]
