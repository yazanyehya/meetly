from nicegui import ui

@ui.page("/calendar")
def calendar_page():
    with ui.column().style("padding: 20px;"):
        ui.label("Calendar Page").style("font-size: 1.5em; font-weight: bold; margin-bottom: 20px;")
