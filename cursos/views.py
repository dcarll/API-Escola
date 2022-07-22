
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer


class CursoAPIView(APIView):
    """
    API de cursos
    """

    def get(self, request):
        print(request.data)

        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True) #todos os cursos
        return Response(serializer.data)

class AvaliacaoAPIView(APIView):
    """
    API das avaliações
    """
    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)