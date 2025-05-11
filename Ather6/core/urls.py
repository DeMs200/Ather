from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('form1/', views.form1, name='form1'),
    path('form2/', views.form2, name='form2'),
    path('form3/', views.form3, name='form3'),
    path('form4/', views.form4, name='form4'),
    path('form5/', views.form5, name='form5'),
    path('form6/', views.form6, name='form6'),
    path('form7/', views.form7, name='form7'),
    path('form8/', views.form8, name='form8'),
    path('form9/', views.form9, name='form9'),
    path('form10/', views.form10, name='form10'),
    path('form11/', views.form11, name='form11'),
    path('ideas/', views.ideas, name='ideas'),
    path('ideas/<int:index>/edit/', views.edit_idea, name='edit_idea'),
    path('funders/', views.funders, name='funders'),
    path('export-pdf/', views.export_pdf, name='export_pdf'),
] 