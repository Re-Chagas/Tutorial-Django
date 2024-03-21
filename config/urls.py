from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from livraria.views import CategoriaViewSet
from livraria.views import AutorViewSet
from livraria.views import LivroViewSet
from livraria.views import EditoraViewSet

router = DefaultRouter()
router.register(r"categorias", CategoriaViewSet)
router.register(r"livros", LivroViewSet)
router.register(r"autores", AutorViewSet)
router.register(r"editoras", EditoraViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]