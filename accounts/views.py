from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Employee

def accounts(request):
    return render(request, "accounts.html")

def login(request):
    if request.method == "POST":
        employeeID = request.POST.get("employeeID")
        password = request.POST.get("password")
        
        # Debug prints
        print("DEBUG: employeeID =", repr(employeeID))
        print("DEBUG: password =", repr(password))
        
        try:
            employee = Employee.objects.get(employee_id=employeeID)
            print("DEBUG: Retrieved employee.password =", repr(employee.password))
            
            if employee.password.strip() == password.strip():
                return redirect("/task-schedule/")
            else:
                print("DEBUG: Password mismatch")
                messages.error(request, "Incorrect username or password.")
        except Employee.DoesNotExist:
            print("DEBUG: Employee not found")
            messages.error(request, "Incorrect username or password.")
    
    return render(request, "accounts.html")
