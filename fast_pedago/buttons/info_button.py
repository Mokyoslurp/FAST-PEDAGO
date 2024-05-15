# This file is part of FAST-OAD_CS23-HE : A framework for rapid Overall Aircraft Design of Hybrid
# Electric Aircraft.
# Copyright (C) 2022 ISAE-SUPAERO

import ipywidgets as widgets
import ipyvuetify as v

from IPython.display import display

# Create a withe box behind the info button
display(widgets.HTML("""<style>.white-vbox {background-color: white;}</style>"""))


def get_base_info_button():

    # Creating and instantiating an empty info button
    info_button = v.Tooltip(
        top = True, 
        max_width = "50%",

        v_slots = [{
            'name': 'activator',
            'variable': 'tooltip',
            'children': v.Html(
                tag="div", 
                v_on = 'tooltip.on',
                class_ = "d-inline-block",
                children=[v.Btn(
                    children = [v.Icon(children=["fa-info-circle"])],
                    icon = True,
                    disabled = True
                )]
            ),
        }], 
        children = ['']
    )

    return info_button


def get_main_menu_info_button():

    # Creating and instantiating an info button
    info_button = get_base_info_button()
    info_button.children[0] = (
        "Welcome to the training branch of FAST-OAD.\n This is the main menu which can lead you "
        "to the different activities to be performed. You'll also find some links to the source "
        "code of FAST-OAD and its plugins."
    )

    return info_button


def get_sensitivity_analysis_info_button():

    # Creating and instantiating an info button
    info_button = get_base_info_button()
    info_button.children[0] = (
        "This is the sensitivity analysis part of the training branch.\n"
        "In this part, you'll study the influence of a few select aircraft design "
        "parameters on the mass, aerodynamics and performances of the aircraft "
    )

    return info_button


def get_single_process_selection_info_button():

    # Creating and instantiating an info button
    info_button = get_base_info_button()
    info_button.children[0] = (
        "- Select a sizing process in the dropdown menu to make the corresponding display appear \n"
        '- Select "None" to clear the display'
    )

    return info_button


def get_multiple_process_selection_info_button():

    # Creating and instantiating an info button
    info_button = get_base_info_button()
    info_button.children[0] = (
        "- Select a sizing process in the dropdown menu to add the corresponding aircraft to the "
        "display  \n"
        '- Select "None" to clear the display'
    )

    return info_button
