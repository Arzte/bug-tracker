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
from myuser.models import MyUser


@login_required
def create_ticket_view(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.created_by = request.user
            new_form.save()
            breakpoint()
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
    return render(request, 'index.html', {
        'tickets_new': tickets_new,
        'tickets_in_progress': tickets_in_progress,
        'tickets_done': tickets_done,
        'tickets_invalid': tickets_invalid
    })


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


@login_required
def ticket_detail(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    return render(request, 'ticket_detail.html', {'ticket': ticket})


@login_required
def assign_user_to_ticket(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    ticket.assigned_to = request.user
    ticket.completed_by = None
    ticket.status_choices = Ticket.TicketStatus.IN_PROGRESS
    ticket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def mark_ticket_invalid(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    ticket.status_choices = Ticket.TicketStatus.INVALID
    ticket.assigned_to = None
    ticket.completed_by = None
    ticket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def mark_ticket_done(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    ticket.status_choices = Ticket.TicketStatus.DONE
    ticket.assigned_to = None
    ticket.completed_by = request.user
    ticket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def edit_ticket_view(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()

        return HttpResponseRedirect(reverse('ticket_detail',
                                            kwargs={'ticket_id': ticket_id}))

    form = TicketForm(instance=ticket)
    return render(request, 'generic_form.html', {'form': form})


@login_required
def user_detail_view(request, user_id):
    user = MyUser.objects.get(id=user_id)
    assigned_tickets = Ticket.objects.filter(assigned_to=user)
    created_tickets = Ticket.objects.filter(created_by=user)
    completed_tickets = Ticket.objects.filter(completed_by=user)
    return render(request, 'user_detail.html', {
        'user': user,
        'assigned_tickets': assigned_tickets,
        'created_tickets': created_tickets,
        'completed_tickets': completed_tickets,
    })
