from django.shortcuts import redirect
from django.contrib.auth import get_user_model

User = get_user_model()


def admin_only(view_func):

    def wrapper(request, *args, **kwargs):

        # ยังไม่ได้ login
        if not request.user.is_authenticated:
            return redirect('login')

        # ไม่ใช่ admin
        if not request.user.is_superuser and request.user.users_role != 'admin':
            return redirect('home')

        return view_func(request, *args, **kwargs)

    return wrapper