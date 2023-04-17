from rest_framework import serializers
from .models import Movies,Cast,MoviesCast

class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movies
        fields='__all__'
        
class CastSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cast
        fields='__all__'        
        
class MoviesCastSerializer(serializers.ModelSerializer):
    class Meta:
        model=MoviesCast
        fields='__all__'        
        
        
def create(self,validated_data):
    data=validated_data('movies')
    data=validated_data('cast')
    
    Movies=Movies.objecs.create(**validated_data)
    for cast_data in cast_data:
        cast=Cast.objects.get_or_create(**cast_data)
        MoviesCast.objects.create(movies=Movies,cast=Cast)
    return Movies.objects.create(**validated_data)

def update(self,instance,validated_data):
    instance.movies_name=validated_data.get('movies_name',instance.movies_name)
    instance.cast=validated_data.get('cast',instance.cast)
    instance.save()
    return instance        