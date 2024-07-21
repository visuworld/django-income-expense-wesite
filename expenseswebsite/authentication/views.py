from django.shortcuts import render
from django.views.generic import View

# Create your views here.


class RegistrationView(View):
    def get(self, request):
        return render(request, 'authentication/register.html')