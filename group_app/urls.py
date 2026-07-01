from django.urls import path
from . import views

urlpatterns = [
    path('base/', views.base, name='base'),
    path('', views.index, name='index'),
    # for popup form
    path('save-demo-request/', views.save_demo_request, name='save_demo_request'),
    path('about/<slug:section>/', views.about, name='about_section'),
    path('contact/', views.contact, name='contact'),
    path('industries/', views.industries, name='industries'),
    path('industries/<slug:section>/', views.industries, name='industries_section'),

    path('office_form/', views.office_form, name='office_form'),
    path('career/', views.career, {'section': 'banner'}, name='career'),
    path('career/<slug:section>/', views.career, name='career_section'),

    path('foundation/', views.foundation, name='foundation'),
    path('foundation/<slug:section>/', views.foundation, name='foundation_section'),
    path('thanks/', views.thanks, name='thanks'),
    path('blog/', views.blog, name='blog'),
    path('blog/<slug:section>/', views.blog, name='blog_section'),
    path('terms/', views.terms, name='terms'),
    path('legal_disclaimer/', views.legal_disclaimer, name='legal_disclaimer'),
    path('career_form/<int:job_id>/', views.career_form, name='career_form'),


    path('api/jobs/', views.jobs_api, name='jobs_api'),
]
