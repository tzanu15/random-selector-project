from django.urls import path
from .views import hello_world,protected_view


urlpatterns = [
    path('hello/', hello_world, name='hello_world'),
    path('protected/', protected_view, name='protected_view'),  # 🔒
]
