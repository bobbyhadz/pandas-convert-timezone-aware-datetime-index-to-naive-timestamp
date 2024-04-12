# Pandas: Convert timezone-aware DateTimeIndex to naive timestamp

import pandas as pd

dt_index = pd.date_range(
    start='2023-04-11 13:30:00',
    periods=2,
    freq='H',
    tz='US/Pacific',
)

# DatetimeIndex(['2023-04-11 13:30:00-07:00', '2023-04-11 14:30:00-07:00'], dtype='datetime64[ns, US/Pacific]', freq='H')
print(dt_index)

dt_index = dt_index.tz_localize(None)

# DatetimeIndex(['2023-04-11 13:30:00', '2023-04-11 14:30:00'], dtype='datetime64[ns]', freq=None)
print(dt_index)