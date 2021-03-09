from rest_framework import serializers, viewsets
from .models import lessons


class lessonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = lessons
        fields = (
            "id",
            "title",
            "description",
            "lecturer_name",
            "date",
            "duration",
            "slides_url",
            "is_required",
        )


class lessonsViewSet(viewsets.ModelViewSet):
    queryset = lessons.objects.all()
    serializer_class = lessonsSerializer