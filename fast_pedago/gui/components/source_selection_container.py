# This file is part of FAST-OAD_CS23-HE : A framework for rapid Overall Aircraft Design of Hybrid
# Electric Aircraft.
# Copyright (C) 2022 ISAE-SUPAERO

import os.path as pth

import ipyvuetify as v

from fast_pedago.gui.resources import Slide
from fast_pedago.processes import PathManager
from fast_pedago.utils import _image_from_path

# Image files
FAST_OAD_LOGO = "logo_fast_oad_main_menu.jpg"

INPUTS_GIF = "inputs.gif"
LAUNCH_GIF = "launch.gif"
N2_GIF = "n2.gif"
OUTPUTS_GIF = "outputs.gif"


class SourceSelectionContainer(v.Col):
    """
    An container that contains explanations on the app and a source file
    selector to start using the app.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self._load_images()
        self._build_layout()
    

    def _build_layout(self):
        """
        Builds the container layout.
        """
        self.class_ = "pa-8"

        # This reference file should always be there and is always taken as reference
        self.source_data_file_selector = v.Select(
            outlined=True,
            hide_details=True,
            label="Select a reference file",
            items=PathManager.list_available_reference_file(),
        )
        
        tutorial_carousel = v.Carousel(
            height="58vh",
            width="70vw",
            hide_delimiters=True,
            children=[
                v.CarouselItem(
                    children=[
                        v.Row(
                            justify="center",
                            align="center",
                            children=[
                                v.Html(
                                    tag="div",
                                    children=[Slide.Introduction.WELCOME],
                                ),
                            ],
                        ),
                        v.Row(
                            justify="center",
                            align="center",
                            children=[self.fast_oad_logo],
                        ),
                        v.Row(
                            class_="px-12",
                            justify="center",
                            align="center",
                            children=[
                                v.Html(
                                    tag="div",
                                    children=[Slide.Introduction.SELECTION],
                                ),
                            ],
                        ),
                        v.Row(
                            class_="px-12",
                            justify="center",
                            align="center",
                            children=[
                                v.Html(
                                    tag="div",
                                    children=[Slide.Introduction.NOTA],
                                ),
                            ],
                        ),
                    ],
                ),
                v.CarouselItem(
                    children=[
                        v.Row(
                            justify="center",
                            align="top",
                            children=[
                                v.Col(cols=2, lg=3),
                                v.Col(
                                    cols=4,
                                    lg=3,
                                    children=[
                                        v.Html(
                                            class_="mb-6",
                                            style_="font-size: 25px;",
                                            tag="div",
                                            children=[Slide.Inputs.EXPLANATIONS],
                                        ),
                                        v.Html(tag="div", children=[Slide.Inputs.DASH_1]),
                                        v.Html(tag="div", children=[Slide.Inputs.DASH_2]),
                                        v.Html(tag="div", children=[Slide.Inputs.DASH_3]),
                                        v.Html(tag="div", children=[Slide.Inputs.DASH_4]),
                                    ],
                                ),
                                v.Col(
                                    cols=5,
                                    lg=4,
                                    children=[self.inputs_gif],
                                ),
                                v.Col(),
                            ],
                        ),
                    ],
                ),
                v.CarouselItem(
                    children=[
                        v.Row(
                            class_="pb-5 px-12 mx-12",
                            justify="center",
                            align="center",
                            children=[Slide.Launch.EXPLANATIONS]
                        ),
                        v.Row(
                            justify="center",
                            align="center",
                            children=[self.launch_gif],
                        ),
                    ],
                ),
                v.CarouselItem(
                    children=[
                        v.Row(
                            class_="pb-5 px-12 mx-12",
                            justify="center",
                            align="center",
                            children=[Slide.Configuration.EXPLANATIONS]
                        ),
                        v.Row(
                            justify="center",
                            align="center",
                            children=[self.n2_gif],
                        ),
                    ],
                ),
                v.CarouselItem(
                    children=[
                        v.Row(
                            class_="pb-5 px-12 mx-12",
                            justify="center",
                            align="center",
                            children=[Slide.Outputs.SELECTION]
                        ),
                        v.Row(
                            justify="center",
                            align="center",
                            children=[self.outputs_gif],
                        ),
                        v.Row(
                            class_="pt-2 px-12 mx-12",
                            justify="center",
                            align="center",
                            children=[
                                v.Html(
                                    style_="font-size: 14px; color: red;",
                                    tag="div",
                                    children=[Slide.Outputs.WARNING]
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        )
        
        self.children=[
            v.Row(
                justify="center",
                children=[
                    tutorial_carousel,
                ],
            ),
            v.Row(
                class_="mt-10",
                justify="center",
                children=[
                    self.source_data_file_selector,
                ],
            ),
        ]


    def _load_images(self):
        """
        Loads tutorial images and gifs as instance variables to call them during
        the layout building.
        """
        self.fast_oad_logo = _image_from_path(
            pth.join(PathManager.resources_path, FAST_OAD_LOGO), max_height="40vh")
        
        self.inputs_gif = _image_from_path(
            pth.join(PathManager.tutorial_resources_path, INPUTS_GIF), max_height="70vh")
        self.launch_gif = _image_from_path(
            pth.join(PathManager.tutorial_resources_path, LAUNCH_GIF), max_height="50vh")
        self.n2_gif = _image_from_path(
            pth.join(PathManager.tutorial_resources_path, N2_GIF), max_height="50vh")
        self.outputs_gif = _image_from_path(
            pth.join(PathManager.tutorial_resources_path, OUTPUTS_GIF), max_height="35vh")

        