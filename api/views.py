from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated

from .models import Expense, Income
from .serializers import ExpenseSerializer, IncomeSerializer

# --- EXISTING VIEWSETS ---
from rest_framework import viewsets, permissions

class ExpenseViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseSerializer
    # 1. Sirf logged-in users hi access kar sakein
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # 2. Filter: Sirf apna data dikhao
        return Expense.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # 3. Save: Request bhejne wale user ko owner banao
        serializer.save(user=self.request.user)

# Yahi logic IncomeViewSet mein bhi copy-paste kar dein
class IncomeViewSet(viewsets.ModelViewSet):
    serializer_class = IncomeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Income.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# --- NEW AUTH VIEWS (Login/Signup) ---

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    data = request.data
    try:
        # Username aur Email dono ko email value hi assign kar rahe hain safety ke liye
        user = User.objects.create_user(
            username=data.get('email'), 
            email=data.get('email'),
            password=data.get('password'),
            first_name=data.get('fullName', '')
        )
        refresh = RefreshToken.for_user(user)
        return Response({
            'access': str(refresh.access_token),
            'user': {'fullName': user.first_name, 'email': user.email}
        }, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': 'Registration failed. Email might already exist.'}, status=400)

@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    login_id = request.data.get('email') # React se jo bhi text aaye
    password = request.data.get('password')
    
    # User ko 'auth_user' table mein dhoondna (Username ya Email se)
    user_obj = User.objects.filter(Q(username=login_id) | Q(email=login_id)).first()
    
    if user_obj and user_obj.check_password(password):
        refresh = RefreshToken.for_user(user_obj)
        return Response({
            'access': str(refresh.access_token),
            'user': {'fullName': user_obj.first_name or user_obj.username, 'email': user_obj.email}
        })
    return Response({'detail': 'Invalid Credentials'}, status=401)