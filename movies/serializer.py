from rest_framework import serializers
from movies.models import Movie, Rating

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, allow_null=True)
    rating = serializers.ChoiceField(choices=Rating.choices, default=Rating.G, allow_null=True)
    synopsis = serializers.CharField(allow_null=True)
    added_by = serializers.SerializerMethodField()

    def get_added_by(self, obj):

      return obj.added_by.email

    def create(self, validated_data):
      return Movie.objects.create(**validated_data)
