from django.urls import path
from snippets import views

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
    path('history', views.history_list),
    path('account/create/', views.EmployeesCreateViewSet.as_view()),
    path('list/', views.EmployeesListViewSet.as_view()),
    path('account/detail/<int:pk>/', views.EmployeesDetailViewSet.as_view()),
    path('personal/', views.PersonalViewSet.as_view()),
    path('device/', views.DeviceViewSet.as_view()),
    path('device/create/', views.DeviceCreateViewSet.as_view()),
    path('device/detail/<int:pk>/', views.DeviceDetailViewSet.as_view())
]
