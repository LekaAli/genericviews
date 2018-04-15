from django.conf.urls import url, include
from viewsets import EmployeeCreateViewSet, EmployeeListViewSet, EmployeeUpdateViewSet
from views import employee_created, employee_updated, main_page, update_info, update_employee

urlpatterns = [
    url(r'^create-employee/$', EmployeeCreateViewSet.as_view(), name='create-employee'),
    url(r'^list-employees/$', EmployeeListViewSet.as_view(), name='list-employee'),
    url(r'^update-employee/(?P<pk>[0-9]+)/$', EmployeeUpdateViewSet.as_view(), name='update-employee'),
    url(r'^created/$', employee_created, name='created'),
    url(r'^updated/$', employee_updated, name='updated'),
    url(r'^update-info/$', update_info, name='update-info'),
    url(r'index/$', main_page, name='main-page'),
    url(r'^update/$', update_employee, name='update'),

]