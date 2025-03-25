from django.urls import path
from .views import ExpenseListCreateView, ExpenseRetrieveUpdateDeleteView


urlpatterns = [
    path('expenses/', ExpenseListCreateView.as_view(), name='api_expenses_list_create'),
    path('expenses/<int:pk>/', ExpenseRetrieveUpdateDeleteView.as_view(), name='api_expense_detail'),
]
