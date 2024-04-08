from django.urls import path

from . import views

urlpatterns = [
    path("streamlit/", views.streamlit_view, name="streamlit_view"),
]
