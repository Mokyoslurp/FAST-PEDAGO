import ipywidgets as widgets
import ipyvuetify as v


def get_back_home_button():

    back_home_button = widgets.Button(description="")
    back_home_button.icon = "fa-home"
    back_home_button.layout.width = "auto"
    back_home_button.layout.height = "auto"

    back_home_button = v.Btn(
        children = [v.Icon(children=["fa-home"])],
        icon = True
    )

    return back_home_button
