
from django.urls import path
from jobs.views import (
  jobs_list,
  jobs_form_view,
  job_submit,
  edit_email,
  job_comment_page
  )

app_name = 'jobs'

urlpatterns = [
  path('',jobs_list,name='jobs_list'),
  path('<slug:url>/',jobs_form_view,name="jobs_form_view"),
  path("<slug:url>/job-comments",job_comment_page,name="job_comment_page"),
  path('<slug:url>/job-submit',job_submit,name="job_submit"),
  path('<slug:url>/edit-email',edit_email,name="edit_email"),
]