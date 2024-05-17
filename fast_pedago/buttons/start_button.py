# This file is part of FAST-OAD_CS23-HE : A framework for rapid Overall Aircraft Design of Hybrid
# Electric Aircraft.
# Copyright (C) 2022 ISAE-SUPAERO

import ipywidgets as widgets
import ipyvuetify as v


def get_start_button():

    # Create a green button which spans almost the full width of the interface
    layout_button = widgets.Layout(
        width="80%",
        height="95%",
        border="4px solid black",
    )

    # Slight note, if you add two numbers after the hexadecimal code, you can make it transparent
    start_button = v.Btn(
        block = True,
        color = "#33caff99",
        children = ["Get started!"],
        # layout=layout_button,
        #     font_weight="bold",
        #     font_size="20px",
        # ),
    )

    return start_button
