from django.http import HttpResponse
from django.shortcuts import render


def streamlit_view(request):
    return render(request, "streamlit_view.html")
