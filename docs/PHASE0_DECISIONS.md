# MBOT — Fase 0: Decisiones de Arquitectura y Seguridad

## Objetivo
Construir un chatbot web multi-tenant (multi-cliente) con un solo código + una sola base de datos,
aislado por `client_id`, con dashboard interno (solo admin), lead capture, y evolución a n8n/WhatsApp Cloud API.

## Alcance (MVP)
- Widget web embebible por <script> con `client_id`
- API REST (FastAPI) para chat + lead capture + config del widget
- PostgreSQL multi-tenant (todo con `client_id`)
- Nginx reverse proxy (80/443 en el futuro)
- Sin login para clientes (solo dashboard interno admin)

## Stack (cerrado)
- Backend: Python + FastAPI
- DB: PostgreSQL
- Infra: AWS EC2 + Docker Compose + Nginx
- UI: Tailwind (NO Bootstrap)
- IA: OpenAI como fallback UX (no inventa datos)
- Observabilidad: logs estructurados + métricas básicas

## Multi-tenancy (regla central)
- Todo dato tiene `client_id`
- Toda query filtra por `client_id`
- Config por cliente en tabla `clients.settings`

## KB (Knowledge Base)
Fuente de verdad del chatbot por cliente:
- FAQ, productos, menú, promos, políticas, horarios, ubicación
La IA solo reformula/orienta cuando KB no tiene respuesta exacta.

## Add-ons (flags por cliente)
- enable_ai
- enable_whatsapp_click
- enable_whatsapp_cloud (futuro)
- enable_n8n (futuro)

## Seguridad (mínimo obligatorio)
- Secrets: nunca en repo, solo env vars (y luego secret manager)
- Admin dashboard protegido (auth fuerte + allowlist si aplica)
- Rate limiting por IP y por client_id en endpoints públicos
- Validación estricta de input
- Logs sin secretos, con request_id
- Backups DB (más adelante a S3)

## Pruebas (conceptos)
- Caja blanca: SAST, revisión permisos, pruebas unitarias
- Caja negra: DAST básico, pruebas de abuso (spam), carga ligera (Locust)

## Fuera de alcance (por ahora)
- Multi-cloud
- Microservicios
- Login para clientes
- WebSockets/GraphQL/gRPC

