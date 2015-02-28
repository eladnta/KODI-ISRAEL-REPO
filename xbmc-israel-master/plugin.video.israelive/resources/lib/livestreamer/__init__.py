"""Livestreamer extracts streams from various services.

The main compontent of Livestreamer is a command-line utility that
launches the streams in a video player.

An API is also provided that allows direct access to stream data.

Full documentation is available at http://livestreamer.tanuki.se/.

"""


__title__ = "livestreamer"
__version__ = "1.10.2"
__license__ = "Simplified BSD"
__author__ = "Christopher Rosell"
__copyright__ = "Copyright 2011-2014 Christopher Rosell"
__credits__ = [
    "Christopher Rosell", "Athanasios Oikonomou", "Gaspard Jankowiak",
    "Dominik Dabrowski", "Toad King", "Niall McAndrew", "Daniel Wallace",
    "Sam Edwards", "John Peterson", "Kacper", "Andrew Bashore",
    "Martin Panter", "t0mm0", "Agustin Carrasco", "Andy Mikhailenko",
    "unintended", "Moritz Blanke", "Jon Bergli Heier", "Stefan Breunig",
    "papplampe", "Brian Callahan", "Eric J", "Jan Tore Morken", "JOKer",
    "Max Nordlund", "yeeeargh", "Vitaly Evtushenko", "Che", "nixxquality",
    "medina", "Michael Cheah", "Jaime Marquinez Ferrandiz"
]

#import requests
from .api import streams
from .exceptions import (LivestreamerError, PluginError, NoStreamsError,
                         NoPluginError, StreamError)
from .session import Livestreamer
