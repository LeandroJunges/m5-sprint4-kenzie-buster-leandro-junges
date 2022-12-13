from rest_framework import serializers
from movies.models import Movie, MovieOrder, Rating

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, default=None)
    rating = serializers.ChoiceField(choices=Rating.choices, default=Rating.G)
    synopsis = serializers.CharField(allow_null=True, allow_blank=True, default=None)
    added_by = serializers.SerializerMethodField()

    def get_added_by(self, obj):

        return obj.user.email

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.SerializerMethodField()
    buyed_at = serializers.DateTimeField(read_only=True)
    
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    buyed_by = serializers.SerializerMethodField()

    def get_title(self, obj:MovieOrder)->str:
        return obj.movie.title
    
    def get_buyed_by(self, obj:MovieOrder)->str:
        return obj.order.email
    

    def create(self, validated_data:dict)-> MovieOrder:

        return MovieOrder.objects.create(**validated_data)