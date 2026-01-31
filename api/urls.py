from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExpenseViewSet, IncomeViewSet, register_user
from rest_framework_simplejwt.views import TokenObtainPairView

router = DefaultRouter()
# Ye ab /api/expenses/ aur /api/incomes/ banayega
router.register(r'expenses', ExpenseViewSet, basename='expense')
router.register(r'incomes', IncomeViewSet, basename='income')

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', register_user),
    # Yahan khali string ('') rakhein kyunke main urls.py mein 'api/' pehle se hai
    path('', include(router.urls)), 
]