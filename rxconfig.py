import reflex as rx

config = rx.Config(
    app_name="password_strength_checker",
    frontend_port=3000,
    backend_port=8000,
    env=rx.Env.DEV,
)