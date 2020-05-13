from django.urls import path
from deriveweb import views
urlpatterns = [
    path('', views.derive_home),
    path('beer/', views.derive_beer),
]
