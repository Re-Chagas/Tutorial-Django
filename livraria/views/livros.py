from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from livraria.models import Livro
from livraria.serializers.livros import LivroSerializer, LivroDetailSerializer #,LivroListSerializer

class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    permission_classes = [IsAuthenticated]


    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return LivroDetailSerializer
        return LivroSerializer

#    def get_serializer_class(self):
#         if self.action == "list":
#             return LivroListSerializer
#         elif self.action == "retrieve":
#             return LivroDetailSerializer
#         return LivroSerializer