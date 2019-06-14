from django.urls import path

from . import views

app_name = 'polls' #sets the application name space so Django can differentiate between polls.detail or blog.detail
# we also go to the template and change from 'detail' to 'polls: detail'
urlpatterns = [
  path('', views.index, name='index'),
  path('<int:question_id>/', views.detail, name='detail'),
  path('<int:question_id>/results/', views.results, name='results'),
  path('<int:question_id>/vote/', views.vote, name='vote'),
]