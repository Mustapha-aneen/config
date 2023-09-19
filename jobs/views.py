from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from jobs.models import PostJob
from jobs.forms import JobForm,CommentForm
from django.urls import reverse
from jobs.models import Applicant
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.
def edit_email(request,url):
  posts = get_object_or_404(PostJob,slug=url)
  is_exist = ""
  if(request.method == "POST"):
    old_email = request.POST.get("old_email")
    new_email = request.POST.get("new_email")
    exists = Applicant.objects.filter(email=old_email).exists()
    if(exists):
      discover = Applicant.objects.get(email=old_email)
      discover.email = new_email
      is_exist = old_email+" changed to "+new_email
      discover.save()
    else:
      is_exist = "Email not exit try again"
  return render(request,"jobs/edit_email.html",{"posts":posts,"exists":is_exist})
def job_submit(request,url):
  posts = get_object_or_404(PostJob,slug=url)
  if request.method == "POST":
    forms = JobForm(request.POST)
    if forms.is_valid():
      fname = forms.cleaned_data["firstname"]
      lname = forms.cleaned_data["lastname"]
      job = forms.cleaned_data["job"]
      email = forms.cleaned_data["email"]
      exists = Applicant.objects.filter(email=email).exists();
      if( not exists):
        Applicant(firstname=fname,lastname=lname,job=job,email=email).save();
      else:
        return HttpResponseRedirect(reverse("jobs:jobs_form_view",args=[posts.slug]))
  context = {
    "posts":posts,
    "email":email,
    "job":job,
    "firstname":fname,
  }
  return render(request,"jobs/job_submitted.html",context)
def jobs_form_view(request,url):
  posts = get_object_or_404(PostJob,slug=url)
  form = JobForm()
  return render(request ,"jobs/jobs_form.html",{"forms":form,"posts":posts,"request":request})
def jobs_list(request):
  object_list = PostJob.objects.all()
  
  paginator = Paginator(object_list,5)
 
  page = request.GET.get("page")
  
  try:
    posts = paginator.page(page)
  except PageNotAnInteger as e:
    posts = paginator.page(1)
  except EmptyPage as e:
    posts = paginator.page(paginator.num_pages)
  
  return render(request, 
        "jobs/jobs_display_list.html",
        {"posts":posts}
        )
def job_comment_page(request,url):
  post = get_object_or_404(PostJob,slug=url)
  comments = post.comments.filter(active=True)
  new_comment = None
  if(request.method == "POST"):
    form = CommentForm(request.POST)
    if(form.is_valid()):
      new_comment = form.save(commit=False)
      new_comment.job = post
      new_comment.save()
      
  else:
    form = CommentForm()
  complex = {
    "post":post,
    "form":form,
    "comments":comments,
    "new_comment":new_comment,
  }
  return render (request, "jobs/comment.html",complex)