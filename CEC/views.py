from django.shortcuts import render, redirect
import pyrebase

config = {
    "apiKey": "AIzaSyDbAn-fvmY7MDxmbwQNrJkKn175WWxrh30",
    "authDomain": "carbon-guard-52ed1.firebaseapp.com",
    "databaseURL": "https://carbon-guard-52ed1-default-rtdb.firebaseio.com/",
    "projectId": "carbon-guard-52ed1",
    "storageBucket": "carbon-guard-52ed1.appspot.com",
    "messagingSenderId": "565640798929",
    "appId": "1:565640798929:web:db11d89014c922f191dbf0",
    "measurementId": "G-4GGDBDWZDM"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
database = firebase.database()

def home(request):
    return render(request, 'home.html', {})

def login(request):
    return render(request, 'login.html', {})

def signup(request):
    return render(request, 'signup.html', {})

def calculator(request):
    return render(request, 'calculator.html', {})

def about(request):
    return render(request, 'about.html', {})
def profile(request):
    return render(request, 'profile.html', {})

def postsign(request):
    email = request.POST.get('email')
    passw = request.POST.get('password')

    try:
        user = auth.sign_in_with_email_and_password(email, passw)
        request.session['firebase_uid'] = user['localId']  # Store Firebase UID in session
        return redirect('welcome', firebase_uid=user['localId'])  # Redirect to welcome page with UID
    except:
        message = "Invalid Credentials"
       
        return render(request, "login.html", {"messg": message})

def presign(request):
    email = request.POST.get('email')
    passw = request.POST.get('password')

    user = auth.create_user_with_email_and_password(email, passw)

    print("Success...")
    
    
    return render(request, 'login.html', {'e': email})

def welcome(request, firebase_uid):
    if firebase_uid:
        # Retrieve user data from Firebase Realtime Database using the Firebase UID
        user_data = database.child('users').child(firebase_uid).get().val()
        return render(request, 'welcome.html', {'user_data': user_data})
    else:
        # Handle case when user is not logged in or UID is not provided
        return redirect('login')

    



    


