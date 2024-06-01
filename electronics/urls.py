from django.urls import path
from . import views

urlpatterns = [
    path('electronics/', views.ElectronicsListView.as_view(), name='electronics'),
    path('electronics/<int:id>/', views.DetailElectronicsView.as_view(), name='detail_electronics'),
    path('old_age_elect/', views.OldAgeListView.as_view(), name='retirees'),
    path('young_age_elect/', views.YoungAgeListView.as_view(), name='younger'),
    path('create_comment/', views.create_comment_view, name='comments'),

]