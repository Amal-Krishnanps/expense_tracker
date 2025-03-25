from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from .models import Expense
from .forms import ExpenseForm
from django.db.models import Sum
import xlwt
from django.http import HttpResponse

def signup(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('dashboard')
    else:
        form=SignUpForm()
    return render(request,'register.html',{'form':form})    
            

def signin(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form=AuthenticationForm()
    return render(request,'login.html',{'form':form})

def signout(request):
    logout(request)
    return redirect('signin')
            
@login_required
def dashboard(request):
    expenses = Expense.objects.filter(user=request.user).order_by('-date')
    total_expense = expenses.aggregate(total=Sum('amount'))['total'] or 0
    categorized_summary = expenses.values('category').annotate(total=Sum('amount')).order_by('-total') 
    
    return render(request, 'dashboard.html',{
        'expenses': expenses,
        'total_expense': total_expense,
        'categorized_summary': categorized_summary,
    })
    
# >>>>>>>>>>>>>>>>> Expenses <<<<<<<<<<<<<<<<<<<<<<<<<<<    
@login_required
def add_expense(request):
    if request.method=='POST':
        form=ExpenseForm(request.POST)
        if form.is_valid():
            expense=form.save(commit=False)
            expense.user=request.user
            expense.save()
            return redirect('dashboard')
    else:
         form=ExpenseForm()
    return render(request,'add_expense.html',{'form':form})
    
@login_required
def edit_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id, user=request.user)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'edit_expense.html', {'form': form})

@login_required
def delete_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id, user=request.user)
    expense.delete()
    return redirect('dashboard')



# Export options

def export_expenses_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="expenses.xls"'

    # Create workbook & worksheet
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('Expenses')

    # header style
    header_style = xlwt.XFStyle()
    font_bold = xlwt.Font()
    font_bold.bold = True
    header_style.font = font_bold

    # heading row
    headers = ['Sl. No.','Title', 'Amount', 'Category', 'Date']
    for col_num, header in enumerate(headers):
        worksheet.write(0, col_num, header, header_style)

    # Write data rows
    expenses = Expense.objects.filter(user=request.user)
    for row_num, expense in enumerate(expenses, start=1):
        worksheet.write(row_num, 0, row_num)
        worksheet.write(row_num, 1, expense.title)
        worksheet.write(row_num, 2, str(expense.amount))  
        worksheet.write(row_num, 3, expense.category)
        worksheet.write(row_num, 4, expense.date.strftime('%Y-%m-%d'))

    workbook.save(response)
    return response