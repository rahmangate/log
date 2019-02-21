from django.shortcuts import render
from logapp.models import Employee ,Visitor
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.
def index(request):
    """View function for home page of site."""
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html')


def visitors_today(request):
    return render (request,'logapp/visitors/today.html')



def employees(request):
    return render (request,'logapp/employees/employees.html')


class EmployeesListView(generic.ListView):
    model = Employee
    #context_object_name = employee_list
    template_name = 'logapp/employees/employees.html'

class EmployeeDetailView(generic.DetailView):
    model=Employee
    template_name='logapp/employees/employee_detail.html'

class EmployeeCreate(CreateView):
    model=Employee
    fields='__all__'
    template_name = 'logapp/employees/employee_form.html'


class EmployeeUpdate(UpdateView):
    model=Employee
    fields='__all__'


class VisitorsListView(generic.ListView):
    model = Visitor
    template_name='logapp/visitors/visitors.html'

class VisitorDetailView(generic.DetailView):
    model=Visitor
    template_name='logapp/visitors/visitor_detail.html'


class VisitorCreate(CreateView):
    model=Visitor
    fields= '__all__'
    template_name = 'logapp/visitors/visitor_form.html'