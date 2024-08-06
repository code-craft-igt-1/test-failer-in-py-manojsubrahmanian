import unittest
from weatherreport import report, WeatherSensorStub

class TestWeatherReport(unittest.TestCase):

    def test_sunny_day(self):
        sensor_stub = WeatherSensorStub(50, 10, 30, 55)
        weather_report = report(sensor_stub)
        self.assertEqual(weather_report, 'Sunny day')

    def test_rainy_day(self):
        sensor_stub = WeatherSensorStub(50, 70, 30, 55)
        weather_report = report(sensor_stub)
        self.assertEqual(weather_report, 'Alert: Stormy with heavy rain')
        

if __name__ == '__main__':
    unittest.main()