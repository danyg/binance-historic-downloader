#!/usr/bin/env python3

from _download import download
from _util import (base_command, base_command_help_creator)

base_command(base_command_help_creator('download'), download)

