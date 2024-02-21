"""camp_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('hrEmployeeLeaveStatus/', views.hrEmployeeLeaveStatus, name='hrEmployeeLeaveStatus'),
    path('hrAddCamp', views.hrAddCamp, name = "hrAddCamp"),
    path('messCaptainViewMessSchedule', views.messCaptainViewMessSchedule, name = "messCaptainViewMessSchedule"),
    path('employee-profile/', views.employeeProfileView, name='employeeProfileView'),
    path('messCaptainViewLeaveSchedule/', views.messCaptainViewLeaveSchedule, name = "messCaptainViewLeaveSchedule"),
    path('employeeViewBusSchedule/', views.employeeViewBusSchedule, name='employeeViewBusSchedule'),
    path('employeeComplaintPortal/', views.employeeComplaintPortal, name="employeeComplaintPortal"),
    path('employeeLeaveRequestView/',views.employeeLeaveRequestView,name='employeeLeaveRequestView'),
    path('employeeLeaveRequest/',views.employeeLeaveRequest,name='employeeLeaveRequest'),
    path('campBossAddEmployee', views.AddEmployee, name='campBossAddEmployee'),
    
    path('campBossAddBus',views.campBossAddBus,name='campBossAddBus'),
    path('campBossProfile/', views.campBossProfileView, name='campBossProfileView'),  # Example URL pattern for campBossProfileView
    path('login',views.login_view,name='login'),

    
    path('hrlogin/',views.hr_login_view, name='hr_login'),
    path('hrhome/', views.hr_home_view, name='hrHome'),

    path('login/', views.login_view, name='login'),
    path('login/messcaptain.html/', views.mess_captain_home_view, name='mess_captain_home'),

   
    path('hrAddCamp/', views.hrAddCamp, name='hrAddCamp'),
    path('campBossAddItem/', views.add_item, name='campBossAddItem'),
    path('hrAddCampBoss/', views.add_camp_boss_view, name='hrAddCampBoss'),
    path('campBossHome/', views.campBossHomeView, name='campBossHome'),
    path('campBossAddEmployee/', views.AddEmployee, name='campBossAddEmployee'),
    path('campBossAddCategory/', views.AddItemCategory, name='campBossAddCategory'),
    path('campBossHome/',views.campBossHomeView, name='campBossHome'),
   
    path('campBossAddEmployee/', views.AddEmployee, name='campBossAddEmployee'),
    path('EmployeeHome/', views.employee_home_view, name='EmployeeHome'),
    path('campBossEmployeeview/', views.campBossEmployeeview, name='campBossEmployeeview'),

    path('hrEmployeeLeaveStatus/', views.hrEmployeeLeaveStatus, name='hrEmployeeLeaveStatus'),
    path('messCaptainViewMessSchedule', views.messCaptainViewMessSchedule, name = "messCaptainViewMessSchedule"),
    path('employeeProfileView/', views.employeeProfileView, name='employee_profile_view'),
    path('messCaptainViewLeaveSchedule/', views.messCaptainViewLeaveSchedule, name = "messCaptainViewLeaveSchedule"),
    path('employeeViewBusSchedule/', views.employeeViewBusSchedule, name='employeeViewBusSchedule'),


    path('messCaptainHome/', views.mess_captain_home_view, name='messCaptainHome'), 
    path('hrCreateRoomType/', views.hrCreateRoomType, name="hrCreateRoomType"),
    path('hrAddRoom/', views.hrAddRoom, name = "hrAddRoom"),
    path('hrAddBed/', views.hrAddBed, name="hrAddBed"),
    path('hrAddFlat/', views.hrAddFlat, name = "hrAddFlat"),
    path('hrAddFloor/', views.hrAddFloor, name='hrAddFloor'),
    
    path('hrAddCampBoss/', views.add_camp_boss_view, name='hrAddCampBoss'),
     path('hrEmployeeView/', views.employeeProfileView, name='hrEmployeeView'),
     path('hrEmployeeProfileView',views.hrEmployeeProfileView,name='hrEmployeeProfileView'),
     path('hrViewComplaint',views.hrViewComplaint,name='hrViewComplaint'),
    path('hrLeaveRequestView',views.hrLeaveRequestView,name='hrLeaveRequestView'),
    path('approve/<int:request_id>/', views.approve_leave_request, name='approve_leave_request'),
    path('reject/<int:request_id>/', views.reject_leave_request, name='reject_leave_request'),
    path('employeeLeaveStatus', views.employeeLeaveStatus, name='employeeLeaveStatus'),
    path('employeemessview_schedule',views.employeemessview_schedule,name='employeemessview_schedule'),
    path('campbossviewmessschedule',views.campbossviewmessschedule,name='campbossviewmessschedule'),
    path('AllBusScheduleView',views.viewBusSchedule,name='AllBusScheduleView'),
     
]
