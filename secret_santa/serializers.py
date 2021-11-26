import random
from rest_framework import serializers
from secret_santa.models import Game, Participant

class ParticipantSerializer(serializers.Serializer):
	name = serializers.CharField(max_length=50)
	email = serializers.EmailField(max_length=254)
	secret_santa = serializers.StringRelatedField(read_only=True)

class GameSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    participants = ParticipantSerializer(many=True)

    def create(self, validated_data):
        participant_data = validated_data.pop('participants')
        game = Game.objects.create(**validated_data)
        for participant in participant_data:
        	Participant.objects.create(game=game, **participant)
        for participant in game.participants.all():
        	unassigned = game.participants.exclude(id=participant.id).filter(secret_santa=None)
        	i = random.randrange(unassigned.count())
        	recipient = unassigned.all()[i]
        	recipient.secret_santa = participant
        	recipient.save()
        return game

    def validate(self, data):
        participants = [p.get('email') for p in data['participants']]
        if len(participants) < 2:
        	raise serializers.ValidationError('Must specify more than one participant')
        if len(participants) != len(set(participants)):
            raise serializers.ValidationError('Each participant must have a unique email')
        return data