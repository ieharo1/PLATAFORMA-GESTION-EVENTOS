# 🚀 Plataforma de Gestión de Eventos

<p align="center">
  <img src="https://img.icons8.com/color/200/000000/conference-call.png" alt="Event Platform Logo" width="200"/>
</p>

---

## 📱 Descripción

Plataforma full stack en **Django + PostgreSQL + Bootstrap 5** para gestionar eventos **virtuales, presenciales e híbridos** con enfoque escalable para:

- Webinars
- Conferencias
- Eventos multi-ciudad / multi-país
- Gestión de aforo
- Inscripción por enlace
- Certificados digitales verificables
- Ponentes, invitados especiales y moderadores

> Diseñada para operación real en organizaciones educativas, corporativas y comunidades tech con alto volumen de asistentes.

---

## ✨ Características

### Funcionalidades Implementadas ✅

- ✅ CRUD inicial de eventos (creación + dashboard + detalle)
- ✅ Definición de aforo y cálculo automático de cupos disponibles
- ✅ Soporte de modalidades: virtual, presencial e híbrida
- ✅ Alcance geográfico por países y ciudades
- ✅ Link de inscripción y link de streaming por evento
- ✅ Registro de asistentes por evento
- ✅ Prevención de sobrecupo
- ✅ Emisión automática de certificado digital por registro
- ✅ Validación criptográfica del certificado (token firmado)
- ✅ Gestión de asistencia (marcar asistió/no asistió)
- ✅ Panel responsive con Bootstrap 5 (sin CSS custom)

### Próximamente 🔄

- 🔄 Módulo avanzado de roles (staff, organizador, speaker)
- 🔄 Integración de correo transaccional (confirmaciones)
- 🔄 QR para check-in presencial
- 🔄 Exportación masiva (CSV/PDF)
- 🔄 Integración de pagos y tickets
- 🔄 API REST y Webhooks

---

## 🛠️ Stack Tecnológico

| Componente | Tecnología | Versión |
|------------|------------|---------|
| Backend | Python | 3.12 |
| Framework | Django | 5.1.7 |
| Base de datos | PostgreSQL | 16 |
| WSGI | Gunicorn | 23.0.0 |
| Frontend | Bootstrap | 5.3.3 |
| Contenedores | Docker + Compose | latest |

---

## 📁 Estructura del Proyecto

```bash
event_platform/
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── events/
│   ├── migrations/
│   │   └── 0001_initial.py
│   ├── templates/events/
│   │   ├── dashboard.html
│   │   ├── event_form.html
│   │   ├── event_detail.html
│   │   └── certificate_verify.html
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── utils.py
│   └── views.py
├── templates/
│   └── base.html
├── docker-compose.yml
├── Dockerfile
├── entrypoint.sh
├── requirements.txt
├── .dockerignore
├── .env.example
└── README.md
```

---

## 🚀 Cómo Ejecutar el Proyecto

### 1. Clonar el repositorio
```bash
git clone <tu-repo>
cd system-design-notes/event_platform
cp .env.example .env
```

### 2. Levantar con Docker
```bash
docker compose up --build
```

Aplicación disponible en: `http://localhost:8000`

### 3. Crear superusuario (opcional)
```bash
docker compose exec web python manage.py createsuperuser
```

### 4. Ejecutar en local sin Docker (opcional)
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
USE_SQLITE=1 python manage.py migrate
USE_SQLITE=1 python manage.py runserver
```

### 5. Generar ZIP del proyecto (si tu plataforma permite binarios)
```bash
cd ..
zip -r event_platform.zip event_platform
```

---

## 🎯 Flujo funcional

1. Crear evento con capacidad/aforo, modalidad y alcance geográfico.
2. Compartir link de inscripción pública.
3. Registrar asistentes (manual o desde formulario del evento).
4. Emitir certificado digital automáticamente.
5. Verificar autenticidad del certificado con token firmado.
6. Marcar asistencia para control post-evento.

---

## 🔐 Certificados digitales válidos

Los certificados se emiten con:
- Código único derivado por hash
- Token firmado criptográficamente con `django.core.signing`

La validación detecta alteraciones del token y marca certificados inválidos.

---

## 👨‍💻 Desarrollado por Isaac Esteban Haro Torres

**Ingeniero en Sistemas · Full Stack Developer · Automatización · Data**

### 📞 Contacto

- 📧 **Email:** zackharo1@gmail.com
- 📱 **WhatsApp:** [+593 988055517](https://wa.me/593988055517)
- 💻 **GitHub:** [ieharo1](https://github.com/ieharo1)
- 🌐 **Portafolio:** [ieharo1.github.io](https://ieharo1.github.io/portafolio-isaac.haro/)

---

## 📄 Licencia

© 2026 Isaac Esteban Haro Torres - Todos los derechos reservados.

---

⭐ Si te gustó el proyecto, ¡dame una estrella en GitHub!
