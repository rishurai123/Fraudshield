from djongo import models
from bson import ObjectId  

class TestModel(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId)  
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    class Meta:
        app_label = 'mainApp'

class Transaction(models.Model):
    transaction_id = models.IntegerField(unique=True)
    user_id = models.CharField(max_length=100)
    amount = models.FloatField()
    transaction_type = models.CharField(max_length=50)
    merchant = models.CharField(max_length=100)
    time = models.DateTimeField()
    location = models.CharField(max_length=100)
    is_fraudulent = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user_id} - {self.amount}"

class Transaction(models.Model):
    transaction_id = models.IntegerField()
    user_id = models.CharField(max_length=255)
    amount = models.FloatField()
    transaction_type = models.CharField(max_length=50)
    merchant = models.CharField(max_length=255)
    time = models.DateTimeField()
    location = models.CharField(max_length=255)
    is_fraudulent = models.BooleanField()

    class Meta:
        db_table = "transactions"