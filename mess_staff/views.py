from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, redirect, get_object_or_404
from .models import FoodItem
from .forms import FoodItemForm,AddNotificationForm
from mess_user.models import UserProfile,Feedback



# def food_item_list(request):
#     food_items = FoodItem.objects.all()
#     return render(request, 'staff/view_fooditems.html', {'food_items': food_items})
def food_item_list(request):
    food_items = FoodItem.objects.all()
    notifications = AdminNotification.objects.all().order_by('-created_at')
    total_notifications_count = notifications.count()
    return render(request, 'staff/view_fooditems.html', {'food_items': food_items, 'notifications': notifications, 'total_notifications_count': total_notifications_count})



def add_food_item(request):
    if request.method == 'POST':
        form = FoodItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_food')
    else:
        form = FoodItemForm()

    return render(request, 'staff/add_fooditems.html', {'form': form})

def edit_food_item(request, food_id):
    food_item = get_object_or_404(FoodItem, pk=food_id)
    
    if request.method == 'POST':
        form = FoodItemForm(request.POST, request.FILES, instance=food_item)
        if form.is_valid():
            form.save()
            return redirect('view_food')
    else:
        form = FoodItemForm(instance=food_item)
    
    return render(request, 'staff/edit_food.html', {'form': form, 'food_item': food_item})



def delete_food_item(request,pk):
    food = FoodItem.objects.get(food_id=pk) 
    food.delete()
    messages.info(request,"item deleted")
    return redirect("view_food")



def book_item(request, food_id):
    food_item = get_object_or_404(FoodItem, pk=food_id)

    if not hasattr(request.user, 'profile'):
        # Redirect to create profile page
        return redirect('create_profile')

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 0))
        if food_item.book_item(quantity, request.user):
            # Booking successful, you can proceed with your logic here
            return render(request, 'booking_success.html', {'food_item': food_item, 'quantity': quantity})
        else:
            # Quantity not available, handle accordingly (e.g., show an error message)
            return render(request, 'booking_error.html', {'food_item': food_item})

    return render(request, 'book_item.html', {'food_item': food_item})

# views.py
from django.shortcuts import redirect, get_object_or_404
from .models import FoodItem

from django.shortcuts import redirect, get_object_or_404
from .models import FoodItem

def delete_booking(request, food_id):
    
    food_item = get_object_or_404(FoodItem, pk=food_id)
 
    if food_item.booked_by == request.user:
      
        food_item.booked_by = None
        food_item.save()

    return redirect('user_bookings')



def admin_signin(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password)
        if user is not None:
            request .session["username"]=username
            request .session["password"]=password
            login(request,user)
            return redirect("view_food")
        else:
            
            messages.info(request,"username or password incorrect")
            return redirect("admin_signin")

    return render(request,"staff/staff_login.html")


def admin_signout(request):
    logout(request)
    return redirect("admin_signin")  

def admin_bookings(request):
    # Retrieve all booked items with user details
    booked_items = FoodItem.objects.filter(booked_by__isnull=False)
    booking_details = []

    for food_item in booked_items:
        total_price = food_item.price * food_item.quantity_booked
        user_profile = UserProfile.objects.get(user=food_item.booked_by)
        booking_details.append({
            'food_item_name': food_item.name,
            'price': food_item.price,
            'quantity_booked': food_item.quantity_booked,
            'total_price': total_price,  # Calculate total price
            'booked_by_username': food_item.booked_by.username,
            'booked_by_first_name': user_profile.first_name,
            'booked_by_last_name': user_profile.last_name,
            'address': user_profile.address,
            'phone_number': user_profile.phone_number,
            'booked_by_email': food_item.booked_by.email,
            'food_id': food_item.pk,
        })

    context = {'booking_details': booking_details}
    return render(request, 'staff/admin_bookings.html', context)
from django.http import JsonResponse

from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from django.shortcuts import redirect
from django.contrib import messages


from django.urls import reverse


# def delete_booked_item(request, food_id):
#     try:
#         # Ensure the food item is booked and exists
#         food_item = FoodItem.objects.get(pk=food_id, booked_by__isnull=False)
#         food_item.delete()
#         messages.info(request, "Booked item deleted successfully")
#     except FoodItem.DoesNotExist:
#         messages.error(request, "Booked item not found")
#     return redirect("admin_bookings")

def feedback(request):
    feedbacks = Feedback.objects.all().order_by('-time')
    return render(request, 'staff/feedbacks.html', {'feedbacks': feedbacks})


from django.shortcuts import render, redirect
from .models import AdminNotification

from django.db.models import Count
from django.db.models import Count
from django.http import JsonResponse

def admin_notifications(request):
    notifications = AdminNotification.objects.all().order_by('-created_at')
    total_notifications_count = notifications.count()  # Calculate total count
    return render(request, 'staff/notifications.html', {'notifications': notifications, 'total_notifications_count': total_notifications_count})


def delete_notification(request, notification_id):
    notification = AdminNotification.objects.get(pk=notification_id)
    notification.delete()
    return redirect('admin_notifications')


def add_notification(request):
    if request.method == 'POST':
        form = AddNotificationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_notifications')
    else:
        form = AddNotificationForm()
    return render(request, 'staff/add_notifications.html', {'form': form})