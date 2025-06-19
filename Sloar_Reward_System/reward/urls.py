from django.urls import path
from. import views

urlpatterns = [
    path('',views.home),
    path("rewards/distribute", views.rewards),
    path("user/<int:user_id>/wallet", views.wallet),
]