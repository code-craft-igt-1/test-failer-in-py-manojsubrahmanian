import unittest
from weatherreport import report, WeatherSensorStub

class TestWeatherReport(unittest.TestCase):

    def test_rainy(self):
        sensor_stub = WeatherSensorStub(5, 7, 3, 160)
        weather_report = report(sensor_stub)
        print(weather_report)
        self.assertIn('rain', weather_report)

    def test_high_precipitation_and_low_windspeed(self):
        sensor_stub = WeatherSensorStub(50, 70, 30, 40)
        weather_report = report(sensor_stub)
        self.assertGreater(len(weather_report), 0)

if __name__ == '__main__':
    unittest.main()
