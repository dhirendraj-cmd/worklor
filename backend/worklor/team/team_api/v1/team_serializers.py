from rest_framework import serializers
from team.team_models import Membership, Team


class MembershipSerializer(serializers.ModelSerializer):

    class Meta:
        model = Membership
        fields = ['user', 'team', 'role']


class TeamSerializer(serializers.ModelSerializer):
    members = MembershipSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ['id', 'team_name', 'created_by', 'members']

    def create(self, validated_data):
        print(validated_data)


class TeamCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = ['team_name']

    def create(self, validated_data):
        print("validated data is >>>>>>>>>>>>>>> ")
        print(validated_data)
        return super().create(validated_data)

