from django.urls import path
from . import views
urlpatterns = [ 
    path('',views.home,name='home'),
    path('chinhsach',views.chinhsach,name='chinhsach'),
    path('blog',views.blog,name='blog'),
    path('blog/1',views.speblog,name='speblog'),
    path('blog/2',views.speblog2,name='speblog2'),
    path('blog/3',views.speblog3,name='speblog3'),
    path('tuyendung',views.tuyendung,name='tuyendung'),
    path('aboutus',views.aboutus,name='aboutus'),
]
