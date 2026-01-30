from django.db import models

class Expense(models.Model):
    # 'title' ko 'expense_title' aur 'amount' ko 'price' kar diya
    expense_title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"{self.expense_title}"

class Income(models.Model):
    income_title = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.income_title}"