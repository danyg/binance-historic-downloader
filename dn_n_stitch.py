#!/usr/bin/env python3

from _stitcher import Stitcher
from _download import download
from _util import base_command_help_creator, base_command,Pair, Interval, Year, Month

stitcher = Stitcher()

def downloadAndStitch(pair: Pair, interval: Interval, year: Year, month: Month):
  download(pair, interval, year, month)
  stitcher.stitch_action(pair, interval, year, month)


print("Starting...")
base_command(base_command_help_creator('dn_n_stitch'), downloadAndStitch)

print("Writing CSV...")
stitcher.writeFile()

print("Done!")
print("")
