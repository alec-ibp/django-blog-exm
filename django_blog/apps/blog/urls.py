from .views import home
from .views import general
from .views import technology
from .views import tutorials
from .views import contact

from django.urls import path


urlpatterns = [
    path("", home, name="home"),
    path("general/", general, name="general"),
    path("technology/", technology, name="technology"),
    path("contact/", contact, name="contact"),
    path("tutorials/", tutorials, name="tutorials"),
]
