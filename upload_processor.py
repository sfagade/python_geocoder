# This is a sample Python script.
import pandas
from geopy.geocoders import Nominatim


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def process_geo_coder(file_name):
    # I'll make this part dynamic when i convert this to a flash app
    pandas_data = pandas.read_csv(file_name)
    pandas_data.columns = [x.lower() for x in pandas_data.columns]  # convert all headers to lowercase
    if 'address' in pandas_data.columns:  # we only want to continue if there is an address column in the file
        geo_locator = Nominatim(user_agent="example app")
        lon_data = []
        lat_data = []
        """geocode = RateLimiter(geo_locator.geocode, min_delay_seconds=1)
        pandas_data['location'] = pandas_data['address'].apply(geocode)"""
        for index, row in pandas_data.iterrows():
            address = row['address']+","+row['city']+","+row['state']+","+row['country']
            location = geo_locator.geocode(address).raw
            lon_data.append(location.get('lon'))
            lat_data.append(location.get('lat'))

        pandas_data.insert(len(pandas_data.columns),"lat", lat_data, True)
        pandas_data.insert(len(pandas_data.columns), "lon", lon_data, True)
        pandas_data.to_csv("output_data.csv")
        return pandas_data
    else:
        print('Address not found')
        return False

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
