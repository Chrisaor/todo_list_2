from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('crossoff/<int:item_id>', views.crossoff, name='crossoff'),
    path('uncross/<int:item_id>', views.uncross, name='uncross'),
    path('crossoff_index/<int:item_id>', views.crossoff_index, name='crossoff_index'),
    path('uncross_index/<int:item_id>', views.uncross_index, name='uncross_index'),
    path('detail/<int:item_id>', views.detail, name='detail'),
    path('delete/<int:item_id>', views.delete, name='delete'),
    path('edit/<int:item_id>', views.edit, name='edit'),
]
