from datetime import datetime
import sys
from typing import Callable

HelpRenderer = Callable[[],None]
Pair = str
Interval = str
Year = str
Month = str
ActionPerMonth = Callable[[Pair,Interval,Year,Month],None]

def base_command_help_creator(command_name: str) -> HelpRenderer:
  def help():
    print(f"{command_name} [PAIR] [INTERVAL] [START-YEAR] [START-MONTH]")
    print(f"{command_name} BTCUSDT 5m 2019 01")
  return help

def toyyyymm(y: int, m: int):
  return int(f"{y}{str(m).zfill(2)}")

def getZipFileName(pair: Pair,interval: Interval,year: Year,month: Month) -> str:
  return f"{pair}-{interval}-{year}-{month}.zip"

def base_command(help: HelpRenderer, action: ActionPerMonth) -> (Pair, Interval, Year, Month):
  PAIR = sys.argv[1]
  INTERVAL = sys.argv[2]
  YEAR_START = sys.argv[3]
  MONTH_START = sys.argv[4]

  if (not PAIR) or (not INTERVAL) or (not YEAR_START) or (not MONTH_START):
    help()
    quit()

  yearStart = int(YEAR_START)
  monthStart = int(MONTH_START)

  currentMonth = datetime.now().month
  currentYear = datetime.now().year
  currentyyyymm = toyyyymm(currentYear, currentMonth)

  if currentyyyymm < toyyyymm(yearStart, monthStart):
    print("Start Year and Month in the future")
    quit()


  years = range(yearStart-1, currentYear)
  for intyear in years:
    year = str(intyear+1)

    endMonth = currentMonth if (intyear+1) == currentYear else 12
    months = range(monthStart-1, endMonth)

    for intmonth in months:
      month = str(intmonth+1).zfill(2)

      if toyyyymm(year, month) == currentyyyymm:
        break; # current month is not created

      action(PAIR, INTERVAL, year, month)

    monthStart=1 # next years starts in jan

  return PAIR, INTERVAL, YEAR_START, MONTH_START
