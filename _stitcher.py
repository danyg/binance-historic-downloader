import pandas
from _util import base_command_help_creator, base_command, getZipFileName, Pair, Interval, Year, Month

COLUMNS = ["Open time", "Open", "High", "Low", "Close", "Volume", "Close time", "Quote asset volume", "Number of trades", "Taker buy base asset volume", "Taker buy quote asset volume", "Ignore"]
class Stitcher:
  _pair: Pair
  _interval: Interval
  _ohlcv: pandas.DataFrame = None

  def __init__(self) -> None:
      pass

  def stitch_action(self, pair: Pair, interval: Interval, year: Year, month: Month):
    print(f"\t{year}-{month}")
    self._pair = pair
    self._interval = interval
    zipFileName = getZipFileName(pair, interval, year, month)
    raw_data_file = './raw-data/' + zipFileName

    df = pandas.read_csv(raw_data_file, compression='zip', header=0, names=COLUMNS)
    # df['Open time'] = pandas.to_datetime(df['Open time'], unit='ms') # as there is no WAY to convert it to unix AFTER once is processed as being an index, then fu it you now
    df['Open time'] = pandas.to_datetime(df['Open time'], unit='ms').apply(lambda x: int(x.timestamp()))
    df = df.set_index('Open time')
    ohlcv = df[[
      # "Open Time",
      "Open",
      "High",
      "Low",
      "Close",
      "Volume"
    ]]
    self._stitch(ohlcv)

    # print(ohlcv)
    # quit()

  def _stitch(self, ohlcv: pandas.DataFrame):
    if self._ohlcv is None:
      self._ohlcv = ohlcv
    else:
      self._ohlcv = self._ohlcv.append(ohlcv)

  def writeFile(self):
    filename = f"{self._pair}-{self._interval}"
    compression_options = dict(method='zip', archive_name=f'{filename}.csv')
    self._ohlcv.to_csv(f"./full-data/{filename}.zip", header=False, date_format="%s", compression=compression_options)
