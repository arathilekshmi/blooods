from  django.urls import path
from . import views
app_name='blood'
urlpatterns =[
    path('',views.demo,name="demo"),
    path('login/',views.login,name="login"),
    path('login/reg/',views.register,name="register"),
    path('login/donor/',views.donor_registration,name="donor_registration"),
    path('logout',views.logout,name='logout'),
    path('ajax/load-center/', views.load_center, name='ajax_load_center')

]