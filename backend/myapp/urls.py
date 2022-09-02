from django.urls import path
from .views import MyProfileListView, MyProfileDetailView, MyModelView

urlpatterns = [
    path('my-profile/', MyProfileListView.as_view(), name='my_profile_list'),
    path('my-profile/<int:pk>/', MyProfileDetailView.as_view(),
         name='my_profile_detail'),
    path('my-profile-new/', MyModelView.as_view(), name='my_profile_new'),
]
