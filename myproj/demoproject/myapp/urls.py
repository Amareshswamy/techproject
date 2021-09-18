from django.urls import path
from . import views
urlpatterns=[
	path('',views.index,name='index'),
    path('dashboard',views.dashboard,name='dashboard'),
	path('newstudent',views.newstudent,name='newstudent'),
	path('register',views.register,name='register'),
    path('deletestudent',views.deletestudent,name='deletestudent'),
    path('delete',views.delete,name='delete'),
    path('verify',views.verify,name='verify'),
    path('viewstudent',views.viewstudent,name="viewstudent"),
    path('viewindividual',views.viewindividual,name="viewindividual"),
    path('individual',views.individual,name="individual"),
    path('update',views.update,name="update"),
    path('showdetails',views.showdetails,name="showdetails"),
    path('updated_details',views.updated_details,name="updated_details"),    
]    
