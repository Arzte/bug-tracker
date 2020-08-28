from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import reverse

from homepage.forms import LoginForm


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('homepage'))
