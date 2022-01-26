import os
import time
from _util import getZipFileName, Pair, Interval, Year, Month

def download(pair: Pair, interval: Interval, year: Year, month: Month):
  zipFile = getZipFileName(pair, interval, year, month)
  cmd = [
    'wget',
    f'"https://data.binance.vision/data/spot/monthly/klines/{pair}/{interval}/{zipFile}"',
    f'-O ./raw-data/{zipFile}'
  ]

  print(f"Downloading {pair} {interval} {year}-{month}...", end=" ")
  # subprocess.call(cmd)
  os.system(" ".join(cmd))
  time.sleep(1)
  print(f"Done!")
