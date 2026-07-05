import requests

from django.shortcuts import (
    render,
    redirect
)


def login_page(request):

    error_message = None

    if request.method == "POST":

        payload = {

            "email": request.POST.get(
                "email"
            ),

            "password": request.POST.get(
                "password"
            )

        }

        response = requests.post(
            "http://127.0.0.1:8000/auth/login",
            json=payload
        )

        data = response.json()

        if data.get("success"):

            request.session["token"] = data[
                "access_token"
            ]

            request.session["role"] = data[
                "role"
            ]

            return redirect(
                "dashboard"
            )

        else:

            error_message = data.get(
                "message",
                "Login Failed"
            )

    return render(
        request,
        "login.html",
        {
            "error_message": error_message
        }
    )

def dashboard(request):

    token = request.session.get(
        "token"
    )

    if not token:

        return redirect(
            "login"
        )

    response = requests.get(
        "http://127.0.0.1:8000/auth/me",
        headers={
            "Authorization":
            f"Bearer {token}"
        }
    )

    user = response.json()

    return render(
        request,
        "dashboard.html",
        {
            "user": user
        }
    )


def users_list(request):

    token = request.session.get(
        "token"
    )

    if not token:

        return redirect(
            "login"
        )

    search_query = request.GET.get(
        "search",
        ""
    )

    if search_query:

        response = requests.get(
            f"http://127.0.0.1:8000/users/search?query={search_query}",
            headers={
                "Authorization":
                f"Bearer {token}"
            }
        )

    else:

        response = requests.get(
            "http://127.0.0.1:8000/users/",
            headers={
                "Authorization":
                f"Bearer {token}"
            }
        )

    users = response.json()

    return render(
        request,
        "users.html",
        {
            "users": users,
            "role": request.session.get(
                "role"
            ),
            "search_query": search_query
        }
    )

def create_user_page(request):

    token = request.session.get(
        "token"
    )

    if not token:

        return redirect(
            "login"
        )

    if request.method == "POST":

        payload = {

            "username": request.POST.get(
                "username"
            ),

            "email": request.POST.get(
                "email"
            ),

            "mobile_number": request.POST.get(
                "mobile_number"
            ),

            "domain": request.POST.get(
                "domain"
            ),

            "password": request.POST.get(
                "password"
            ),

            "role": request.POST.get(
                "role"
            )

        }

        response = requests.post(
            "http://127.0.0.1:8000/users/",
            json=payload,
            headers={
                "Authorization":
                f"Bearer {token}"
            }
        )

        print(response.status_code)
        print(response.text)

        return redirect(
            "users_list"
        )

    return render(
        request,
        "create_user.html"
    )


def logout(request):

    request.session.flush()

    return redirect(
        "login"
    )

def edit_user_page(
    request,
    user_id
):

    token = request.session.get(
        "token"
    )

    if not token:

        return redirect(
            "login"
        )

    if request.method == "POST":

        payload = {

            "username": request.POST.get(
                "username"
            ),

            "email": request.POST.get(
                "email"
            ),

            "mobile_number": request.POST.get(
                "mobile_number"
            ),

            "domain": request.POST.get(
                "domain"
            ),

            "role": request.POST.get(
                "role"
            ),

            "password": request.POST.get(
                "password"
            )

        }
        

        response = requests.put(
            f"http://127.0.0.1:8000/users/{user_id}",
            json=payload,
            headers={
                "Authorization":
                f"Bearer {token}"
            }
        )

        print(
            response.status_code
        )

        print(
            response.text
        )

        return redirect(
            "users_list"
        )

    response = requests.get(
        f"http://127.0.0.1:8000/users/{user_id}",
        headers={
            "Authorization":
            f"Bearer {token}"
        }
        
    )
    
    
    user = response.json()

    return render(
        request,
        "edit_user.html",
        {
            "user": user
        }
    )


def delete_user_page(
    request,
    user_id
):

    token = request.session.get(
        "token"
    )

    if not token:
        return redirect(
            "login"
        )

    response = requests.delete(
        f"http://127.0.0.1:8000/users/{user_id}",
        headers={
            "Authorization":
            f"Bearer {token}"
        }
    )

    print(response.status_code)
    print(response.text)

    return redirect(
        "users_list"
    )

def trash_users(request):

    token = request.session.get(
        "token"
    )

    if not token:

        return redirect(
            "login"
        )

    response = requests.get(
        "http://127.0.0.1:8000/users/trash",
        headers={
            "Authorization":
            f"Bearer {token}"
        }
    )

    deleted_users = response.json()

    return render(
        request,
        "trash.html",
        {
            "users": deleted_users
        }
    )

def restore_user_page(
    request,
    user_id
):

    token = request.session.get(
        "token"
    )

    if not token:

        return redirect(
            "login"
        )

    response = requests.put(
        f"http://127.0.0.1:8000/users/restore/{user_id}",
        headers={
            "Authorization":
            f"Bearer {token}"
        }
    )

    print(
        response.status_code
    )

    print(
        response.text
    )

    return redirect(
        "trash_users"
    )

def logout_page(request):

    request.session.flush()

    return redirect(
        "login"
    )