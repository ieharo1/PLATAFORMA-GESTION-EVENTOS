from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Event",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=180)),
                ("slug", models.SlugField(unique=True)),
                ("summary", models.TextField()),
                ("description", models.TextField()),
                ("event_type", models.CharField(choices=[("webinar", "Webinar"), ("conference", "Conferencia"), ("workshop", "Workshop"), ("meetup", "Meetup")], max_length=20)),
                ("modality", models.CharField(choices=[("virtual", "Virtual"), ("in_person", "Presencial"), ("hybrid", "Híbrida")], max_length=20)),
                ("registration_link", models.URLField(blank=True)),
                ("livestream_link", models.URLField(blank=True)),
                ("starts_at", models.DateTimeField()),
                ("ends_at", models.DateTimeField()),
                ("capacity", models.PositiveIntegerField(default=100)),
                ("country_scope", models.CharField(help_text="País o países separados por coma", max_length=160)),
                ("city_scope", models.CharField(help_text="Ciudades separadas por coma", max_length=255)),
                ("venue", models.CharField(blank=True, max_length=200)),
                ("is_active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name="Speaker",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("full_name", models.CharField(max_length=120)),
                ("role", models.CharField(max_length=120)),
                ("bio", models.TextField(blank=True)),
                ("is_moderator", models.BooleanField(default=False)),
                ("is_special_guest", models.BooleanField(default=False)),
                ("linkedin", models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name="Registration",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("full_name", models.CharField(max_length=120)),
                ("email", models.EmailField(max_length=254)),
                ("organization", models.CharField(blank=True, max_length=150)),
                ("country", models.CharField(max_length=100)),
                ("city", models.CharField(max_length=100)),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("attended", models.BooleanField(default=False)),
                ("event", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="registrations", to="events.event")),
            ],
            options={"unique_together": {("event", "email")}},
        ),
        migrations.CreateModel(
            name="Flyer",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=120)),
                ("image_url", models.URLField()),
                ("event", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="flyers", to="events.event")),
            ],
        ),
        migrations.CreateModel(
            name="EventSpeaker",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("event", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="event_speakers", to="events.event")),
                ("speaker", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="speaker_events", to="events.speaker")),
            ],
            options={"unique_together": {("event", "speaker")}},
        ),
        migrations.CreateModel(
            name="Certificate",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("code", models.CharField(max_length=64, unique=True)),
                ("signed_token", models.TextField()),
                ("issued_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("registration", models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name="certificate", to="events.registration")),
            ],
        ),
    ]
