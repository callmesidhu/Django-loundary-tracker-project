from django.shortcuts import render, redirect
from django.contrib import messages
from django.template.context_processors import csrf
from .models import Employee
from django.contrib.auth import logout as django_logout

def accounts(request):
    context = {}
    context.update(csrf(request))  # Inject CSRF token into the context
    return render(request, "accounts.jinja", context, using="jinja2")

def logout(request):
    django_logout(request)  # Django's built-in logout
    request.session.flush()  # Clears all session data
    messages.success(request, "You have been logged out.")  # Optional success message
    return redirect('/')  # Redirect to homepage or login page

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
    
    # Ensure the CSRF token is included when rendering the login page
    context = {}
    context.update(csrf(request))
    return render(request, "accounts.jinja", context, using="jinja2")
