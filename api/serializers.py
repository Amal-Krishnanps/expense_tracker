from rest_framework import serializers
from tracker.models import Expense

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Expense
        fields=['id','title','amount','category','date']