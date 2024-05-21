from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .auth_middleware import validate_token


@require_http_methods(["GET"])
@validate_token
def protected_endpoint(request):
    # This endpoint is protected and requires a valid access token
    # Access user information if needed
    user_id = request.user_id
    email = request.email
    return JsonResponse({"message": "Protected endpoint accessed successfully"})
