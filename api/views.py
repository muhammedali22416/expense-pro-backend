from rest_framework import viewsets
from .models import Expense, Income # Income add kiya
from .serializers import ExpenseSerializer, IncomeSerializer # IncomeSerializer add kiya

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all().order_by('-id')
    serializer_class = ExpenseSerializer

class IncomeViewSet(viewsets.ModelViewSet):
    queryset = Income.objects.all().order_by('-id') # Latest income pehle dikhegi
    serializer_class = IncomeSerializer