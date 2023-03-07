from rest_framework.serializers import ModelSerializer
from .models import Theater ,Film,Showtime


class FilmSerializer(ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'


class TheaterSerializer(ModelSerializer):
    class Meta:
        model = Theater
        fields = '__all__'



class ShowtimeSerializerReadOnly(ModelSerializer):
    film = FilmSerializer()
    theater = TheaterSerializer()
    class Meta:
        model = Showtime
        fields = '__all__'
