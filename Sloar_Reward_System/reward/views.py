from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Subscription, User, RewardHistory
from .serializers import DistributeRewardSerializer,WalletSerializer


@api_view(["GET"])
def wallet(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = WalletSerializer(user)
    return Response(serializer.data)


@api_view(["POST"])
def rewards(request):
    serializer = DistributeRewardSerializer(data=request.data)
    if serializer.is_valid():
        project_id = serializer.validated_data['projectId']
        kWh_generated = serializer.validated_data['kWh_generated']

        subs = Subscription.objects.filter(project_id=project_id)
        rewards = []

        for sub in subs:
            reward = (kWh_generated * 1.5) * (sub.subscribedAmount / 1000)

            user = sub.user
            user.walletBalance += reward
            user.save()

            RewardHistory.objects.create(
                user=user,
                creditsEarned=reward,
                kWh_generated=kWh_generated
            )

            rewards.append({
                "userId": user.id,
                "creditsEarned": reward,
                "newWalletBalance": user.walletBalance
            })

        return Response({"rewards": rewards}, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def home(request):
    return HttpResponse("<h1>Solar Reward System</h1>")
