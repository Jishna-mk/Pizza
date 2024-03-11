from django.urls import path
from .import views

urlpatterns=[
    path('add_food/',views.add_food_item,name='add_food'),
    path('view_food/',views.food_item_list,name='view_food'),
    path('admin_signin/',views.admin_signin,name='admin_signin'),
    path('admin_signout/',views.admin_signout,name='admin_signout'),

    
    path('admin_bookings/',views.admin_bookings,name="admin_bookings"),
    path('delete_food_item/<int:pk>/', views.delete_food_item, name='delete_food_item'),
    path('book_item/<int:food_id>/', views.book_item, name='book_item'),
    path('edit_food_item/<int:food_id>/', views.edit_food_item, name='edit_food_item'),
    # path('update_order_status/<int:order_id>/', views.update_order_status, name='update_order_status'),
    # path('delete_booked_item/<int:food_id>/', views.delete_booked_item, name='delete_booked_item'),
    path('feedback/',views.feedback,name="feedback"),
    path('admin_notifications/', views.admin_notifications, name='admin_notifications'),
    path('delete_notification/<int:notification_id>/delete/', views.delete_notification, name='delete_notification'),
    path('add_notification/',views.add_notification,name="add_notification"),
    path('delete_booking/<int:food_id>/', views.delete_booking, name='delete_booking'),
  
    

   

   
   

    
    
]