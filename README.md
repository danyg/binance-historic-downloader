# Binance Data Downloader

## Requirements

- pandas must be installed globally

## Usage

`dn_n_stitch.py [PAIR] [interval] [year_start] [month_start]`

It will download, SPOT data from binance, from year_start month_start until
today and then will generate a composite csv (archived as zip) of all that data

also each operation can be done separately

- `download.py [PAIR] [interval] [year_start] [month_start]`
- `stitch.py [PAIR] [interval] [year_start] [month_start]`
- `dn_n_stitch.py [PAIR] [interval] [year_start] [month_start]`

This works with Windows 10 PowerShell too just by
`.\dn_n_stitch.py BTCUSDT 1m 2019 1`

Once it finishes you'll find the stitched files in full-data and in raw-data
the files downloaded from binance, the idea is that in the future you get updated
data and use those to stitch them to the new downloaded data.

## How to use the stitched data

The intention is to use this data with pandas in the following format

```python
import pandas as pd

df = pd.read_csv(
  './full-data/BTCUSDT-1m.zip',
  compression='zip',
  date_parser=lambda x: pd.to_datetime(x, unit='s'),
  names=['Open', 'High', 'Low', 'Close', 'Volume']
)

print(df)

```

## arguments

Check this for more recent information
[binance-public-data Repo](https://github.com/binance/binance-public-data/)

### pair

All available symbols can be found [here](https://github.com/binance/binance-public-data/blob/master/data/symbols.txt)

### interval

`1m`, `3m`, `5m`, `15m`, `30m`, `1h`, `2h`, `4h`, `6h`, `8h`, `12h`, `1d`, `3d`, `1w`, `1mo`
`1mo` is used instead of `1M` to support non-case sensitive file systems.

### year_start

4 digit year

### month_start

1 or 2 digit month between 1 and 12
