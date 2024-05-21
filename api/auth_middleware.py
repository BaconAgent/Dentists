from auth0.authentication import GetToken
from django.conf import settings
from functools import wraps
from django.http import JsonResponse


def validate_token(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        # Extract access token from request headers
        auth_header = request.headers.get("Authorization", None)
        if not auth_header:
            return JsonResponse(
                {"error": "Authorization header is missing"}, status=401
            )

        token = auth_header.split(" ")[1]

        # Validate access token using Auth0 SDK
        get_token = GetToken(settings.AUTH0_DOMAIN)
        try:
            # Introspect token to validate and extract user information
            decoded_token = get_token.introspect(token, settings.API_IDENTIFIER)

            # Extract user information from decoded token
            user_id = decoded_token.get("sub")
            email = decoded_token.get("email")

            # Pass user information to view function if needed
            request.user_id = user_id
            request.email = email

        except Exception as e:
            return JsonResponse({"error": "Invalid token"}, status=401)

        return view_func(request, *args, **kwargs)

    return wrapper
