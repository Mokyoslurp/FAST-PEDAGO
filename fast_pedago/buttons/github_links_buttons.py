# This file is part of FAST-OAD_CS23-HE : A framework for rapid Overall Aircraft Design of Hybrid
# Electric Aircraft.
# Copyright (C) 2022 ISAE-SUPAERO

import ipywidgets as widgets
import ipyvuetify as v

import webbrowser

GITHUB_FAST_CORE = "https://github.com/fast-aircraft-design/FAST-OAD"
GITHUB_FAST_CS25 = "https://github.com/fast-aircraft-design/FAST-OAD_CS25"
GITHUB_FAST_CS23 = "https://github.com/supaero-aircraft-design/FAST-GA"

# Base functions to get a standard button opening a git page

def open_github(widget, event, data):
    if widget.tag == "core":
        webbrowser.open_new_tab(GITHUB_FAST_CORE)
    elif widget.tag == "cs25":
        webbrowser.open_new_tab(GITHUB_FAST_CS25)
    elif widget.tag == "cs23":
        webbrowser.open_new_tab(GITHUB_FAST_CS23)

def get_base_git_button():
    git_button = v.Btn(
        tag = "",
        children = [
            v.Icon(
                class_ = "me-2",
                children = ["fa-github"])
        ]
    )

    git_button.on_event("click", open_github)

    return git_button


# Personnalized git buttons

def get_fast_oad_core_git_button():

    fast_core_git_button = get_base_git_button()
    fast_core_git_button.children.append("FAST-OAD_core")
    fast_core_git_button.tag = "core"

    return fast_core_git_button


def get_fast_oad_cs25_git_button():

    fast_cs25_git_button = get_base_git_button()
    fast_cs25_git_button.children.append("FAST-OAD_cs25")
    fast_cs25_git_button.tag = "cs25"

    return fast_cs25_git_button


def get_fast_oad_cs23_git_button():

    fast_cs23_git_button = get_base_git_button()
    fast_cs23_git_button.children.append("FAST-OAD_cs23")
    fast_cs23_git_button.tag = "cs23"

    return fast_cs23_git_button
