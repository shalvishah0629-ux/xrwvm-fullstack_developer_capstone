
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'

urlpatterns = [
    # User login
    path(route='login', view=views.login_user, name='login'),

    # User logout (activate after implementing logout_request)
    # path(route='logout', view=views.logout_request, name='logout'),

    # User registration (activate after implementing registration)
    # path(route='register', view=views.registration, name='register'),

    # Dealership and review routes can be added here
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
