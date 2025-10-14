import reflex as rx

config = rx.Config(
    app_name="password_strength_checker",
    frontend_port=5000,
    backend_port=9000,
    env=rx.Env.DEV,
    disable_plugins=["reflex.plugins.sitemap.SitemapPlugin"]
)