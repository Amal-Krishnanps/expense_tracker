from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('signin/',views.signin,name='signin'),
    path('signout/',views.signout,name='signout'),
    path('', views.dashboard, name='dashboard'),
    path('add/', views.add_expense, name='add_expense'),
    path('edit/<int:expense_id>/', views.edit_expense, name='edit_expense'),
    path('delete/<int:expense_id>/', views.delete_expense, name='delete_expense'),
    path('export/excel/', views.export_expenses_excel, name='export_excel'),
    
]
