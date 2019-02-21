from django.urls import path
from . import views

urlpatterns = [

]


urlpatterns = [
    path('', views.index, name='index'),
    path('visitors/today',views.visitors_today,name='visitors-today'),
    path('employees/',views.EmployeesListView.as_view(),name='employees'),
    path('employees/create',views.EmployeeCreate.as_view(),name='employee_create'),
    path('visitors/create',views.VisitorCreate.as_view(),name='visitor_create'),
    path('visitors/',views.VisitorsListView.as_view(),name='visitors')
]


urlpatterns += [
    path('employee/<int:pk>',views.EmployeeDetailView.as_view(),name='employee_detail'),
    path('employees/<int:pk>/update',views.EmployeeUpdate.as_view(),name='employee_update'),
]