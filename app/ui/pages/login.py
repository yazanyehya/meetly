from nicegui import ui

def login_page():
    @ui.page("/")
    def render():   
        with ui.row().style("position: absolute; top: 0; left: 0; width: 100%; height: 100%;"):
            ui.image('https://wallpapercave.com/wp/fMos4cr.jpg').style("width: 100%; height: 100%; object-fit: cover;")
        
        with ui.column().style("position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); padding: 20px; width: 400px; background: rgba(255, 255, 255, 0.8); border-radius: 8px; box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);"):
            ui.label("Welcome to Meetly").style("font-size: 1.5em; font-weight: bold; margin-bottom: 20px; text-align:center;")
            email = ui.input(label="Email").props('type="email"').style("margin-bottom: 10px;")
            password = ui.input(label="Password").props('type="password"').style("margin-bottom: 10px;")
            # async def handle_login():
            #     if email.value == "ironman@gmail.com" and password.value == "12345678":
            #         ui.notify("Login successfully ", type="positive")
            #         ui.open("/calendar")
            #     else:
            #         ui.notify("email or password is wrong ", type = "negative")

            ui.button("Login", on_click= lambda: ui.navigate.to("/calendar")).props("rounded").style("margin-bottom: 10px;")
            with ui.row():
                ui.label("Don't have an account?").style("margin-right: 5px;")
                ui.link("Sign Up", "/signup").style("color: blue; text-decoration: underline;")
