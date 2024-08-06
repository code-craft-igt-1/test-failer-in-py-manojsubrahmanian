from weatherreport import report
from weatherreport import WeatherSensorStub
# Test a rainy day

def test_rainy():
    sensor_stub = WeatherSensorStub(5, 7, 3, 160)
    weather_report = report(sensor_stub)
    print(weather_report)
    assert ('rain' in weather_report)


# Test another rainy day

def test_high_precipitation_and_low_windspeed():
    # This instance of stub needs to be different-
    # to give high precipitation (>60) and low wind-speed (<50)
    sensor_stub = WeatherSensorStub(50, 70, 30, 40)
    weather_report = report(sensor_stub)
    # strengthen the assert to expose the bug
    # (function returns Sunny day, it should predict rain)
    assert (len(weather_report) > 0)


if __name__ == '__main__':
    test_rainy()
    test_high_precipitation_and_low_windspeed()
    print('All is well (maybe)')