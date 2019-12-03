from rest_framework import serializers
from webapp.models import Issue, Projects


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = "__all__"

class ProjectsSerializer(serializers.ModelSerializer):
    issues = IssueSerializer(many=True, read_only=True)
    create_date = serializers.DateTimeField(read_only=True)
    updated_date = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Projects
        fields = "__all__"


