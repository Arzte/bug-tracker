from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import reverse

from homepage.forms import LoginForm
from homepage.forms import TicketForm
from homepage.models import Ticket


@login_required
def create_ticket_view(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.created_by_id = request.user
            form.save()
            form.save_m2m()
            return HttpResponseRedirect(reverse("homepage"))

    form = TicketForm()
    return render(request, 'generic_form.html', {'form': form})


@login_required
def homepage_view(request):
    tickets_new = Ticket.objects.filter(
        status_choices=Ticket.TicketStatus.NEW).all()
    tickets_in_progress = Ticket.objects.filter(
        status_choices=Ticket.TicketStatus.IN_PROGRESS).all()
    tickets_done = Ticket.objects.filter(
        status_choices=Ticket.TicketStatus.DONE).all()
    tickets_invalid = Ticket.objects.filter(
        status_choices=Ticket.TicketStatus.INVALID).all()
    return render(request, 'index.html', {'tickets_new': tickets_new, 'tickets_in_progress': tickets_in_progress, 'tickets_done': tickets_done, 'tickets_invalid': tickets_invalid})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        data = request.POST
        user = authenticate(request, username=data.get(
            'username'), password=data.get('password'))
        if user:
            login(request, user)
            return HttpResponseRedirect(
                request.GET.get('next', reverse("homepage"))
            )

    form = LoginForm()
    return render(request, 'generic_form.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login_view'))
