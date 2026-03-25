from django import forms
from .models import Event, Registration


class EventForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.setdefault("class", "form-control")

    class Meta:
        model = Event
        fields = [
            "title",
            "slug",
            "summary",
            "description",
            "event_type",
            "modality",
            "registration_link",
            "livestream_link",
            "starts_at",
            "ends_at",
            "capacity",
            "country_scope",
            "city_scope",
            "venue",
            "is_active",
        ]
        widgets = {
            "starts_at": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "ends_at": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }


class RegistrationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.setdefault("class", "form-control")

    class Meta:
        model = Registration
        fields = ["full_name", "email", "organization", "country", "city"]
