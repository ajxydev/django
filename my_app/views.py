from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from my_app.models import UserProfile,Blog
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def home(request):
   return render(request,'home.html')

def login_view(request):
    

    if request.method == "POST":

       username = request.POST['username']
       password = request.POST['password']

       user = authenticate(request, username=username, password=password)
       
       if user is not None:

            login(request,user)

            if user.is_superuser:
               return redirect('admin_home')

            else:
               return redirect('user_home')




    return render(request,'login.html')

def register(request):

    if request.method == "POST":

       name = request.POST['name']
       email = request.POST['email']
       phone = request.POST['phone']
       place = request.POST['place']
       username = request.POST['username']
       password = request.POST['password']

       user = User.objects.create_user(
           username=username,
           password=password,
           email=email
       )

       UserProfile.objects.create(
           USER=user,
           name=name,
           email=email,
           phone=phone,
           place=place
       )

       return redirect('login_view')

    return render(request,'register.html')

# def logout_view(request):

#    logout(request)

#    return redirect('login_view')

@never_cache
def logout_view(request):
    auth_logout(request)
    request.session.flush()

    response = redirect('login_view')
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response
@login_required
@never_cache
@csrf_exempt
def admin_home(request):
   return render(request,'admin_home.html')
@login_required
@never_cache
@csrf_exempt
def user_home(request):
   blogs = Blog.objects.all()

   return render(request,'user_home.html',{'blogs':blogs})
@login_required
@never_cache
@csrf_exempt
def view_users(request):
   users=UserProfile.objects.all()
   return render(request,'view_users.html',{'users':users})

@login_required
@never_cache
@csrf_exempt
def view_blogs_admin(request):
   blogs=Blog.objects.all()
   return render(request,'view_blogs_admin.html',{'blogs':blogs})

@login_required
@never_cache
@csrf_exempt
def add_blog(request):

   if request.method == "POST":

       title = request.POST['title']
       content = request.POST['content']
       image = request.FILES['image']

       Blog.objects.create(
           USER=request.user,
           title=title,
           content=content,
           image=image
       )

       

   return render(request,'add_blog.html')

@login_required
@never_cache
@csrf_exempt
def my_blogs(request):
   blogs=Blog.objects.filter(USER=request.user)
   return render(request,'my_blogs.html',{'blogs':blogs})

@login_required
@never_cache
@csrf_exempt
def edit_blog(request,id):
   blogs=Blog.objects.get(id=id)
   if request.method=="POST":
      blogs.title=request.POST['title']
      blogs.content=request.POST['content']
      if 'image' in request.FILES:
           blogs.image = request.FILES['image']

      blogs.save()
      return redirect('my_blogs')
   return render(request,"edit_blog.html",{'blogs':blogs})

@login_required
@never_cache
@csrf_exempt
def delete_blog(request,id):
   blogs=Blog.objects.get(id=id)
   blogs.delete()
   return redirect('my_blogs')

def forgot_password(request):
   if request.method=="POST":
      username=request.POST['username']
      email=request.POST['email']

   
      user = User.objects.filter(
            username=username,
            email=email
        ).first()

      if user:
            request.session['user_id'] = user.id
            return redirect('reset_password')

      return render(
            request,
            "forgot_password.html",
            {"error": "Invalid username or email"}
        )

   return render(request, "forgot_password.html")


def reset_password(request):

   if request.method=="POST":
      a=User.objects.get(id=request.session['user_id'])
      password=request.POST['password'] 
      confirm=request.POST['confirm_password']

      if confirm!=password:
         return render(
            request,
            "reset_password.html",
            {"error": "Incorrect password"}
        )
         
      a.set_password(password)
      a.save()

      del request.session['user_id']

      return redirect('login_view')   
         
      
     
     
   return render(request,"reset_password.html")
      
    



