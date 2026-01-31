from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExpenseViewSet, IncomeViewSet, login_user, register_user

router = DefaultRouter()
router.register(r'expenses', ExpenseViewSet, basename='expense')
router.register(r'incomes', IncomeViewSet, basename='income')

urlpatterns = [
    path('api/login/', login_user),  # Ab ye React wale URL se match karega
    path('api/register/', register_user),
    path('api/', include(router.urls)),
]