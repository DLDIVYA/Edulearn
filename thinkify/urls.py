from django.urls import path
from .import views

app_name='thinkify'
urlpatterns =[
    path('',views.home.as_view(),name='Home'),
    path('loginPage', views.LoginPage.as_view(), name='loginPage'),
    path('registerPage',views.registerPage.as_view(),name='registerPage'),
    path('exams',views.exams,name='exams'),
    path('home',views.homeNext.as_view(),name='homeNext'),
    path('scholarship',views.scholarship,name='scholarship'),
    path('logout',views.Logout.as_view(),name='logout'),
    path('resources',views.resources.as_view(),name='resources'),
    path('persona', views.persona, name='persona'),
    # path('listing',views.listing,name='listing'),
    # path('per_content',views.per_content,name='per_content'),
    path('perspage',views.Personalisation.as_view(),name="perspage"),
    path('filter',views.Filter.as_view(),name='filter'),
    path('newhome',views.newhome,name = "newhome")

]

# path('process_checkbox/', views.process_checkbox, name='process_checkbox'),