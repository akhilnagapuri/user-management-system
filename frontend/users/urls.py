from django.urls import path

from .views import (
    login_page,
    dashboard,
    users_list,
    create_user_page,
    logout,
    edit_user_page,
    delete_user_page,
    restore_user_page,
    logout_page
)
from .views import (
    trash_users
)

urlpatterns = [

    path(
        "",
        login_page,
        name="login"
    ),

    path(
        "dashboard/",
        dashboard,
        name="dashboard"
    ),

    path(
        "users/",
        users_list,
        name="users_list"
    ),

    path(
        "create-user/",
        create_user_page,
        name="create_user"
    ),
    path(
    "logout/",
    logout,
    name="logout"
),

path(
    "edit-user/<str:user_id>/",
    edit_user_page,
    name="edit_user"
),
path(
    "delete-user/<str:user_id>/",
    delete_user_page,
    name="delete_user"
),
path(
    "trash/",
    trash_users,
    name="trash_users"
),
path(
    "restore-user/<str:user_id>/",
    restore_user_page,
    name="restore_user"
),
path(
    "logout/",
    logout_page,
    name="logout"
),

]