from django.db import models
from django.contrib.auth.models import User # Default Django User import kiya

class Expense(models.Model):
    # Foreign Key add ki taake pata chale ye kharcha kisne kiya
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expenses')
    expense_title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.expense_title}"

class Income(models.Model):
    # Foreign Key yahan bhi add ki
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='incomes')
    income_title = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.income_title}"