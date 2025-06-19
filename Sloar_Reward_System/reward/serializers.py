from rest_framework import serializers
from .models import RewardHistory, User

class DistributeRewardSerializer(serializers.Serializer):
    projectId = serializers.IntegerField()
    kWh_generated = serializers.FloatField()

class RewardResultSerializer(serializers.Serializer):
    userId = serializers.IntegerField()
    creditsEarned = serializers.FloatField()
    newWalletBalance = serializers.FloatField()

class RewardHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RewardHistory
        fields = ['user','creditsEarned', 'kWh_generated', 'timestamp']

class WalletSerializer(serializers.ModelSerializer):
    rewardHistory = RewardHistorySerializer(source='rewardhistory_set', many=True)

    class Meta:
        model = User
        fields = ['walletBalance', 'rewardHistory']