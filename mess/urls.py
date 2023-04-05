from django.urls import path

from mess import views

urlpatterns = [
    path('m/',views.mes),
]