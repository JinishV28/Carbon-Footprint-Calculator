from django.urls import path # type: ignore
from django.conf import settings # type: ignore
from django.conf.urls.static import static # type: ignore
from . import views

urlpatterns = [
    path('', views.home),
    path('signin/', views.signin, name='signin'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('predictionReport/', views.predictionReport, name='predictionReport'),
    path('result/', views.result, name='result'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)