from django.contrib import admin
from django.urls import path, include

from blog.views import *

app_name = "blog"
urlpatterns = [
    path('', PostLV.as_view(), name='index'),
    path('post/', PostLV.as_view(), name='post_list'),
    path('post/<slug>', PostDV.as_view(), name='post_detail'),
    # archive path
    path('archive/', PostAV.as_view(), name='post_archive'),
    path('<int:year>/', PostYAV.as_view(), name='post_year_archive'),
    path('<int:year>/<month>/', PostMAV.as_view(), name='post_month_archive'),
    path('<int:year>/<month>/<int:day>/', PostDAV.as_view(), name='post_day_archive'),
    path('today/', PostTAV.as_view(), name='post_today_archive'),
    # tag path
    path('tag/', TagTV.as_view(), name="tag_cloud"),
    path('tag/<tag_name>/', PostTOL.as_view(), name='tagged_object_list'),
]
