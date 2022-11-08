from django.urls import include, re_path
#from django.conf.urls import url
from  .import views
from django.urls import path
app_name = 'registration'
urlpatterns = [
    re_path('reg', views.reg,name='reg'),
    re_path('otpvalidation',views.otpvalidation),
    re_path('login/',views.login),
    re_path('my_logout/',views.my_logout),
    re_path (r'^cart/$', views.cart, name='cart'),
    re_path(r'^addcart/', views.addcart, name='addcart'),
    re_path(r'^insertcart/', views.insertcart, name='insertcart'),
    re_path(r'^viewcart', views.viewcart, name='viewcart'),
    re_path(r'^deletecart/', views.deletecart, name='deletecart'),
    re_path(r'^modifycart/', views.modifycart, name='modifycart'),
    re_path(r'^modifiedcart/', views.modifiedcart, name='modifiedcart'),
    re_path(r'^track/$', views.track, name='track'),
    re_path(r'^cancel/$',views.cancel, name='cancel'),
]