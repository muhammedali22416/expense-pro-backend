from rest_framework import serializers
from .models import Expense, Income

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        # Naye field names yahan likh diye
        fields = ['id', 'expense_title', 'price', 'date'] 

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = ['id', 'income_title', 'amount', 'date', 'created_at']