from django.contrib import messages
from django.db.models import Count
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .forms import EventForm, RegistrationForm
from .models import Event, Registration
from .utils import build_certificate, verify_certificate_token


def dashboard(request: HttpRequest) -> HttpResponse:
    events = Event.objects.annotate(total_registrations=Count("registrations")).order_by("starts_at")
    stats = {
        "total_events": events.count(),
        "active_events": events.filter(is_active=True).count(),
        "upcoming_events": events.filter(starts_at__gte=timezone.now()).count(),
        "registrations": Registration.objects.count(),
    }
    return render(request, "events/dashboard.html", {"events": events, "stats": stats})


def event_create(request: HttpRequest) -> HttpResponse:
    form = EventForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Evento creado correctamente.")
        return redirect("dashboard")
    return render(request, "events/event_form.html", {"form": form})


def event_detail(request: HttpRequest, slug: str) -> HttpResponse:
    event = get_object_or_404(Event, slug=slug)
    form = RegistrationForm(request.POST or None)

    if request.method == "POST":
        if event.seats_left <= 0:
            messages.error(request, "No hay cupos disponibles para este evento.")
            return redirect("event_detail", slug=event.slug)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.event = event
            registration.save()
            certificate = build_certificate(registration)
            messages.success(
                request,
                f"Inscripción confirmada. Código de certificado: {certificate.code}",
            )
            return redirect("event_detail", slug=event.slug)

    return render(
        request,
        "events/event_detail.html",
        {
            "event": event,
            "form": form,
            "registrations": event.registrations.select_related("certificate").order_by("-created_at"),
        },
    )


def attendance_toggle(request: HttpRequest, registration_id: int) -> HttpResponse:
    registration = get_object_or_404(Registration, id=registration_id)
    registration.attended = not registration.attended
    registration.save(update_fields=["attended"])
    messages.info(request, "Asistencia actualizada.")
    return redirect("event_detail", slug=registration.event.slug)


def certificate_verify(request: HttpRequest) -> HttpResponse:
    token = request.GET.get("token", "")
    payload = verify_certificate_token(token) if token else None
    return render(request, "events/certificate_verify.html", {"payload": payload, "token": token})
