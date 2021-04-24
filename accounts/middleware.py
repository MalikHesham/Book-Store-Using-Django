# from django.http import HttpResponseForbidden
# class SimpleMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         # One-time configuration and initialization.

#     def __call__(self, request):

#         if not request.user.is_active:
#             return HttpResponseForbidden("Your are not an active user yet, please contact the administration")

#         return self.get_response(request)

