from django.urls import path

from . import views

app_name = 'polls' #sets the application name space so Django can differentiate between polls.detail or blog.detail
# we also go to the template and change from 'detail' to 'polls: detail'
urlpatterns = [
  path('', views.IndexView.as_view(), name='index'),
  path('<int:pk>/', views.DetailView.as_view(), name='detail'),
  path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
  path('<int:question_id>/vote/', views.vote, name='vote'),
]