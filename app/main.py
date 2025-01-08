from fastapi import FastAPI
from nicegui import ui
from app.auth.routes import router as auth_router
from app.db import engine, Base

# Create all tables
Base.metadata.create_all(bind=engine)


app = FastAPI()

# Include authentication routes
app.include_router(auth_router, prefix="/api/auth")

from nicegui import ui

# Add global styles
ui.add_head_html("""
<style>
    body {
        background: url('https://source.unsplash.com/1920x1080/?office,desk') no-repeat center center fixed;
        background-size: cover;
        font-family: Arial, sans-serif;
    }
    .center-card {
        max-width: 400px;
        margin: auto;
        padding: 20px;
        text-align: center;
        background: rgba(255, 255, 255, 0.9);
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
</style>
""")

@ui.page("/")
def login_page():
    with ui.card().classes('center-card'):
        ui.label("Welcome to Meetly").style("font-size: 1.5em; font-weight: bold; margin-bottom: 20px;")
        email = ui.input(label="Email").props('type="email"').style("margin-bottom: 10px;")
        password = ui.input(label="Password").props('type="password"').style("margin-bottom: 10px;")
        ui.button("Login", on_click=lambda: print(f"Logging in with {email.value}")).props("rounded").style("margin-bottom: 10px;")
        ui.link("Don't have an account? Sign Up here", "/signup").style("color: blue; text-decoration: underline;")


@ui.page("/signup")
def signup_page():
    with ui.card().classes('center-card'):
        ui.label("Create Your Account").style("font-size: 1.5em; font-weight: bold; margin-bottom: 20px;")
        name = ui.input(label="Name").style("margin-bottom: 10px;")
        email = ui.input(label="Email").props('type="email"').style("margin-bottom: 10px;")
        password = ui.input(label="Password").props('type="password"').style("margin-bottom: 10px;")
        ui.button("Sign Up", on_click=lambda: print(f"Signing up {name.value}")).props("rounded").style("margin-bottom: 10px;")
        ui.button("Back to Login", on_click=lambda: ui.run_javascript('window.location.href="/"')).props("outline").style("margin-bottom: 10px;")


ui.run_with(app, title="Meetly")
