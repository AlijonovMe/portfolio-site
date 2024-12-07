from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('about/', about),
    path('skills/', skills),
    path('portfolio/', portfolio),
    path('contact/', contact),
    path('send-message/', send_message, name='send_message'),
]