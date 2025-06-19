from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    walletBalance = models.FloatField(default=0.0)

    def __str__(self):
        return self.name
    
class Project(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    subscribedAmount = models.FloatField()

    def __str__(self):
        return f"{self.subscribedAmount}"
    

class RewardHistory(models.Model):  
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    creditsEarned = models.FloatField()
    kWh_generated = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.kWh_generated

    
