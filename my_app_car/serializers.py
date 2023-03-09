from .models import Car, Person, Rent
from rest_framework import status
from rest_framework import serializers

#
# def post_serializer(post: Post):
#     return {"title": post.title,
#             "content": post.content,
#             "date": post.date
#             }


# class PostSerializer1(serializers.Serializer):
#     title = serializers.CharField(max_length=20)
#     content = serializers.CharField(max_length=2000)
#     date = serializers.DateField()
#
#     def create(self, validated_data):
#         Post.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get("title", instance.title)
#         instance.content = validated_data.get("content", instance.content)
#         instance.date = validated_data.get("date", instance.date)


class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = "__all__"


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = "__all__"


class RentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rent
        fields = "__all__"
