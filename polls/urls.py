from django.urls import path
from polls import views
from django.contrib import admin
from django.urls import path, include
app_name = 'polls'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/', admin.site.urls),
    path('polls/<int:question_id>/', views.detail, name='detail'),
    path('polls/<int:question_id>/vote/', views.vote, name='vote'),
    path('polls/<int:question_id>/results/', views.results, name='result'),
]