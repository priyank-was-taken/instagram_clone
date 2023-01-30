from django.urls import path
from .views import *


urlpatterns = [
    path('<str:user>/', profile, name="profile"),
    path('saved/', user_saved, name="user-saved"),
    # path('<user>/saved/', user_saved, name="user-saved"),
    path('tagged/', user_tagged, name="user-tagged"),
    path('<user>/friend-requests/', friendrequest, name="friend-requests"),
    path('requests/<int:pk>/', accept_friend_request, name="accept-requests"),
    path('send_request/<str:receiver>/', send_friend_request, name="send-requests"),
    path('account/edit/', account_edit, name="account-edit"),
    path('change_password/', change_password, name="change_password"),
]