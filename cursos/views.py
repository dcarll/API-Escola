"""
utlizando as class genericas do django_rest_framework, o generics.ListCreateAPIView 
substitui o get e post
O generics.RetrieveUpdateDestroyAPIView implementa o get, post, upload e delete
"""

from rest_framework import generics
from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer
from rest_framework.generics import get_object_or_404


class CursosAPIView(generics.ListCreateAPIView):
    '''get e post cursos'''
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    '''atualiza, deleta ou pega apenas um curso'''
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class AvaliacoesAPIView(generics.ListCreateAPIView):
    '''atualiza, e deleta'''

    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    #get_queryset trás uma lista
    def get_queryset(self):
        if self.kwargs.get('curso_pk'):
            #devolve todas as avaliações filtradas pelo curso
            return self.queryset.filter(curso_id=self.kwargs.get('curso_pk'))

        #caso não passou um id, pega todas as avaliações
        return self.queryset.all()

class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    '''atualiza, deleta ou pega apenas uma avalicao'''
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    #sobscrever o metodo para devolver um objeto
    def get_object(self):
        if self.kwargs.get('curso_pk'):
            return get_object_or_404(self.get_queryset(), curso_id=self.kwargs.get('curso_id'), 
                                                        pk=self.kwargs.get('avaliacao_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('avaliacao_pk'))

