from django.shortcuts import redirect
from django.contrib.auth import login, get_user_model
from social_core.exceptions import AuthForbidden

from .models import User


# def auth_callback(request):
#     # This is just an example, replace with your actual Auth0 callback handling
#     auth0_user_id = request.user.social_auth.get(provider='auth0').uid
#     email = request.user.email
#     name = request.user.name
#
#     # Create the user if they do not exist
#     user, created = User.objects.get_or_create(id=auth0_user_id, defaults={'email': email, 'name': name})
#
#     # Perform login
#     login(request, user)
#     return redirect('/')


User = get_user_model()


def save_profile(backend, user, response, *args, **kwargs):
    if backend.name == 'auth0':
        user_id = response.get('sub')
        email = response.get('email')
        name = response.get('name', response.get('first_name'))  # Use first_name if available

        if not user_id or not email or not name:
            raise AuthForbidden(backend)

        user, created = User.objects.get_or_create(
            id=user_id,
            defaults={'email': email, 'name': name}
        )

        if not created:
            user.email = email
            user.name = name
            user.save()