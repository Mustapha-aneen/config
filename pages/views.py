from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect,get_object_or_404
# Create your views here.
from django.contrib.auth import authenticate , login
from pages.forms import LoginForms,CreateForms
import json as json_data
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from pages.models import Post, Users,Json

profile = "block"
check = "hidden"
user_name = "User"
display = "none"
log_dis = "grid"
user = ""
context = {}
def login(requests):
    global display,log_dis, profile, check ,  user_name,context
    
    items = Post.objects.all()
    if requests.method == "POST":
        form = LoginForms(requests.POST)
        
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
           
            if (Users.objects.filter(email=email,password=password).exists()):
                user = Users.objects.get(email=email,password=password)
                user = Users.objects.get(email=email,password=password)
                profile = "none"
                user_name = user.username
                context["usr"]=user.username
                display = "block"
                log_dis = "none"
                return HttpResponseRedirect(reverse("pages:home")) 
            else:
                check = "visible"
                return HttpResponseRedirect(reverse("pages:login"))
                if check == "password incorrect":
                  check = ""
    else:
      pass
    forms = LoginForms()
   
    context["forms"]=forms
    context["check"]=check
    return render (requests ,'login.html',context)
def home(requests):
    global check
    check = "hidden"
    items = Post.objects.all()
    paginator = Paginator(items,3)
    page = requests.GET.get("page")
    try:
      posts = paginator.page(page)
    except PageNotAnInteger as e:
      posts = paginator.page(1)
    except EmptyPage as e:
      posts = paginator.page(paginator.num_pages)
    context = {
      
    'log_dis':log_dis, 
    'display':display, 
    'username':user_name,
    'profile':profile,
    'items':posts,
      
    }
    return render(requests, 'home.html',context)
def post_details (request,year,month,day,url):
  post = get_object_or_404(Post,
                  slug=url,
                  uptions="public",
                  publish__year=year,
                  publish__month=month,
                  publish__day = day)
  return render (request,"details.html",{"post":post})
def About(requests):
    return HttpResponse("<h1>About Us")
def create_account(request):
    if request.method == "POST":
      form = CreateForms(request.POST)
      if form.is_valid():
        username = form.cleaned_data["username"]
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password"]
        send = Users(username=username,email=email,password=password)
        send.save()
        return HttpResponseRedirect(reverse("pages:login"))
    forms = CreateForms()
    return render (request, "create_account.html",{"forms":forms})
def json(request):
  p = Post.objects.all()
  pos_data = []
  for data in p:
    pos_data.append({
      "title":data.title,
      "image":data.image.url,
    })
  
  return JsonResponse(pos_data , safe=False)

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate


@csrf_exempt
def create(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = Users(username=username, password=password,email=email)
        if Users.objects.filter(email=email,username=username,password=password).exists():
          return JsonResponse({"message":"user has unready exists"})
        elif Users.objects.filter(username=username).exists():
          return JsonResponse({"message":"username has unready use by someone"})
        elif Users.objects.filter(password=password).exists():
          return JsonResponse({"message":"password has unready use by someone"})
          
        else:
          user.save()
          return JsonResponse({"message":"create account successful"})
    return JsonResponse({'message': 'Invalid request method'})
