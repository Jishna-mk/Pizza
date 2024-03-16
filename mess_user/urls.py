from django.urls import path
from .import views

urlpatterns=[
    path('',views.index,name="index"),
    path('service',views.service,name="service"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    path('signup/',views.signup,name="signup"),
    path('signin/',views.signin,name="signin"),
    path('signout/',views.signout,name="signout"),
    path('view_fooditems/',views.food_item_list,name='view_fooditems'),
    path('create_profile/',views.create_profile,name='create_profile'),
    path('view_profile/',views.view_profile,name='view_profile'),
    path('user_bookings/',views.user_bookings,name='user_bookings'),
    path('submit_feedback/', views.submit_feedback, name='submit_feedback'),
    path('view_feedbacks/', views.view_feedbacks, name='view_feedbacks'),
    path('view_notification/', views.view_notification, name='view_notification'),
    path('edit_profile/<int:user_id>/', views.edit_profile, name='edit_profile'),
    
    

]