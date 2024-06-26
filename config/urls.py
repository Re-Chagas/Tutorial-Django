from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework.routers import DefaultRouter

from livraria.views import CategoriaViewSet, LivroViewSet, AutorViewSet, EditoraViewSet


router = DefaultRouter()
router.register(r"categorias", CategoriaViewSet)
router.register(r"livros", LivroViewSet)
router.register(r"autores", AutorViewSet)
router.register(r"editoras", EditoraViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]