from django.db import models
from django.utils import timezone


class Event(models.Model):
    class EventType(models.TextChoices):
        WEBINAR = "webinar", "Webinar"
        CONFERENCE = "conference", "Conferencia"
        WORKSHOP = "workshop", "Workshop"
        MEETUP = "meetup", "Meetup"

    class Modality(models.TextChoices):
        VIRTUAL = "virtual", "Virtual"
        IN_PERSON = "in_person", "Presencial"
        HYBRID = "hybrid", "Híbrida"

    title = models.CharField(max_length=180)
    slug = models.SlugField(unique=True)
    summary = models.TextField()
    description = models.TextField()
    event_type = models.CharField(max_length=20, choices=EventType.choices)
    modality = models.CharField(max_length=20, choices=Modality.choices)
    registration_link = models.URLField(blank=True)
    livestream_link = models.URLField(blank=True)
    starts_at = models.DateTimeField()
    ends_at = models.DateTimeField()
    capacity = models.PositiveIntegerField(default=100)
    country_scope = models.CharField(max_length=160, help_text="País o países separados por coma")
    city_scope = models.CharField(max_length=255, help_text="Ciudades separadas por coma")
    venue = models.CharField(max_length=200, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)

    @property
    def seats_taken(self) -> int:
        return self.registrations.count()

    @property
    def seats_left(self) -> int:
        return max(self.capacity - self.seats_taken, 0)

    def __str__(self) -> str:
        return self.title


class Speaker(models.Model):
    full_name = models.CharField(max_length=120)
    role = models.CharField(max_length=120)
    bio = models.TextField(blank=True)
    is_moderator = models.BooleanField(default=False)
    is_special_guest = models.BooleanField(default=False)
    linkedin = models.URLField(blank=True)

    def __str__(self) -> str:
        return self.full_name


class EventSpeaker(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="event_speakers")
    speaker = models.ForeignKey(Speaker, on_delete=models.CASCADE, related_name="speaker_events")

    class Meta:
        unique_together = ("event", "speaker")


class Flyer(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="flyers")
    title = models.CharField(max_length=120)
    image_url = models.URLField()

    def __str__(self) -> str:
        return f"{self.event.title} - {self.title}"


class Registration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="registrations")
    full_name = models.CharField(max_length=120)
    email = models.EmailField()
    organization = models.CharField(max_length=150, blank=True)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    attended = models.BooleanField(default=False)

    class Meta:
        unique_together = ("event", "email")

    def __str__(self) -> str:
        return f"{self.full_name} ({self.event.title})"


class Certificate(models.Model):
    registration = models.OneToOneField(Registration, on_delete=models.CASCADE, related_name="certificate")
    code = models.CharField(max_length=64, unique=True)
    signed_token = models.TextField()
    issued_at = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.code
