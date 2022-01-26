#!/usr/bin/env python3

from _stitcher import Stitcher
from _util import base_command_help_creator, base_command

stitcher = Stitcher()

print("Processing...")
base_command(base_command_help_creator('stitch'), stitcher.stitch_action)

print("Writing CSV...")
stitcher.writeFile()

print("Done!")
print("")
