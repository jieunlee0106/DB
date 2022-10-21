from rest_framework import serializers
from .models import Actor, Movie, Review


class review_name(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('title', 'content',)

class Movie_name(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title',)

class Actor_name(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ('name',)


# ---------------------------------------------------------

class ActorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ('id', 'name',)


class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = '__all__'
#-----------------------------------------------------------

class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title', 'overview',)

class MovieSerializer(serializers.ModelSerializer):
    review_set = review_name(many=True, read_only=True)
    actors = Actor_name(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'
#-----------------------------------------------------------
class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('title', 'content',)

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie',)