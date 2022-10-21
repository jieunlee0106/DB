from dataclasses import dataclass
from functools import partial
from django.shortcuts import render, get_list_or_404, get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from movies import serializers 

from .models import Actor, Movie, Review

@api_view(['GET'])
def actor_list(request):
    if request.method == 'GET':
        actors = get_list_or_404(Actor)
        serializer = serializers.ActorListSerializer(actors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def actor_detail(request, actor_pk):
    if request.method == 'GET':
        actor = get_object_or_404(Actor, pk = actor_pk)
        serializer = serializers.ActorSerializer(actor)
        return Response(serializer.data, status=status.HTTP_200_OK)

#-----------------------------------------------------------------------------


@api_view(['GET'])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = serializers.MovieListSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def movie_detail(request, movie_pk):
    if request.method == 'GET':
        movie = get_object_or_404(Movie, pk = movie_pk)
        serializer = serializers.MovieSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)

#-----------------------------------------------------------------------------

@api_view(['GET'])
def review_list(request):
    if request.method == 'GET':
        reviews = get_list_or_404(Review)
        serializer = serializers.ReviewListSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'DELETE', 'PUT'])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        serializer = serializers.ReviewSerializer(review)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        # partial=True 을 사용해서 하나의 context 만 수정할 수 있도록 함.
        # review- 원래 자료 / request.data - 수정 데이터 
        # raise_exception=True - 유효성 검사 통과 못할 시 
        serializer = serializers.ReviewSerializer(review, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        # serializer variable - x
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# create 함수 잘 보기
# read_only_fields 로  movie_id 불러오기
@api_view(['POST'])
def review_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = serializers.ReviewSerializer(data=request.data)
    
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)