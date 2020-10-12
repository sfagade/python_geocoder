from turtle import pd

import pandas
from geopy.extra.rate_limiter import RateLimiter
from geopy.geocoders import Nominatim


df = pandas.read_csv("static/sample.csv")
locator = Nominatim(user_agent="example app")
# 1 - conveneint function to delay between geocoding calls
geocode = RateLimiter(locator.geocode, min_delay_seconds=1)
# 2- - create location column
df['location'] = df['Address'].apply(geocode)
# 3 - create longitude, laatitude and altitude from location column (returns tuple)
df['point'] = df['location'].apply(lambda loc: tuple(loc.get('lat')) if loc else None)
print(df)
# 4 - split point column into latitude, longitude and altitude columns
df[['latitude', 'longitude', 'altitude']] = pd.DataFrame(df['point'].tolist(), index=df.index)

print(df)