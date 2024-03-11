from django.shortcuts import render,redirect
from .forms import UserAddForm,UserProfileForm
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from mess_staff.models import FoodItem,AdminNotification
from django.contrib.auth.decorators import login_required
from .models import UserProfile

# Create your views here.
def index(request):
    return render(request,"index.html")
def service(request):
    return render(request,"service.html")
def contact(request):
    return render(request,"contact.html")
def about(request):
    return render(request,"about.html")




def signup(request):
    if request.method == "POST":
        print("Form submitted:", request.POST)
    form = UserAddForm(request.POST)
    if form.is_valid():
        user = form.save()
        group = Group.objects.get(name='users')
        user.groups.add(group)
        login(request, user)
        messages.info(request, "User Created")
        return redirect('signin')
    else:
        print("Form errors:", form.errors)

    return render(request, "signup.html", {"form": form})




from django.shortcuts import render, redirect

def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect("view_fooditems")
        else:
            messages.info(request, "Username or password incorrect")
            
    # If the request is not POST or authentication fails, render the login page.
    return render(request, "signin.html")


def food_item_list(request):
    food_items = FoodItem.objects.all()
    return render(request, 'view_fooditems.html', {'food_items': food_items})

def signout(request):
    logout(request)
    return redirect('signin')



@login_required
def create_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('view_profile')  
    else:
        form = UserProfileForm()

    return render(request, 'create_profile.html', {'form': form})


@login_required
def view_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    return render(request, 'view_profile.html', {'user_profile': user_profile})


@login_required
def user_bookings(request):
    # Retrieve all booked items for the current user
    booked_items = FoodItem.objects.filter(booked_by=request.user)

    # Calculate total price for each item
    for item in booked_items:
        item.total_price = item.price * item.quantity_booked

    context = {
        'booked_items': booked_items,
    }
    return render(request, 'user_bookings.html', context)


from django.shortcuts import render, redirect
from .models import Feedback
from .forms import FeedbackForm

def submit_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.save()
            return redirect('view_feedbacks')
    else:
        form = FeedbackForm()
    return render(request, 'submit_feedback.html', {'form': form})

def view_feedbacks(request):
    feedbacks = Feedback.objects.all().order_by('-time')
    return render(request, 'view_feedbacks.html', {'feedbacks': feedbacks})


def view_notification(request):
    notifications = AdminNotification.objects.all().order_by('-created_at')
    return render(request, 'notice.html', {'notifications': notifications})