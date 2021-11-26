from rest_framework import viewsets, mixins
from secret_santa.models import Game
from secret_santa.serializers import GameSerializer

class GameViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
	queryset = Game.objects.all()
	serializer_class = GameSerializer
