
# This is a stub for a weather sensor. For the sake of testing
# we create a stub that generates weather data and allows us to
# test the other parts of this application in isolation
# without needing the actual Sensor during development

class WeatherSensorStub:
    def __init__(self, humidity, precipitation, temperature_in_celsius, windspeed_in_kmph):
        self._humidity = humidity
        self._precipitation = precipitation
        self._temperature_in_celsius = temperature_in_celsius
        self._windspeed_in_kmph = windspeed_in_kmph

    def humidity(self):
        return self._humidity

    def precipitation(self):
        return self._precipitation

    def temperature_in_celsius(self):
        return self._temperature_in_celsius

    def windspeed_in_kmph(self):
        return self._windspeed_in_kmph


def report(sensor):
    precipitation = sensor.precipitation()
    report_out = 'Sunny day'
    if sensor.temperature_in_celsius() > 25:
        if precipitation > 20 and precipitation < 60:
            report_out = 'Partly cloudy'
        elif sensor.windspeed_in_kmph() > 50:
            report_out = 'Alert: Stormy with heavy rain'
    return report_out
