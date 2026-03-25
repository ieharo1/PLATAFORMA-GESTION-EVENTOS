import hashlib
from django.core import signing
from .models import Certificate, Registration


def build_certificate(registration: Registration) -> Certificate:
    raw = f"{registration.event_id}:{registration.email}:{registration.created_at.isoformat()}"
    code = hashlib.sha256(raw.encode()).hexdigest()[:16].upper()
    payload = {
        "code": code,
        "event": registration.event.title,
        "email": registration.email,
        "full_name": registration.full_name,
    }
    token = signing.dumps(payload, salt="event-certificate")
    certificate, _ = Certificate.objects.update_or_create(
        registration=registration,
        defaults={"code": code, "signed_token": token},
    )
    return certificate


def verify_certificate_token(token: str) -> dict | None:
    try:
        return signing.loads(token, salt="event-certificate", max_age=None)
    except signing.BadSignature:
        return None
