import cmd
import requests

from config import BASE_URL, API_KEY
from utils import tempurature, check_city_humidity, sunset_sunrise
from art import print_art



class WeatherCli(cmd.Cmd):
    prompt = "Prompt🧭>> "
    intro = f"{print_art('WeatherCli')}\nTo get started type 'hi'\nType 'help' for available commands\nType 'exit' to exit the cli\n"
    city = None
    data = None

    def do_hi(self, line):
        """Greet the WeatherCli and start the weather data retrieval process."""
        print(f"Using WeatherCli and it works ;)\n")
        try:
            WeatherCli.city = input("City's Name: ")
            parameters = {
                "q": WeatherCli.city,
                "appid": API_KEY,
                "units": "metric",
            }
            response = requests.get(BASE_URL, params=parameters)
            response.raise_for_status()
            WeatherCli.data = response.json()

            values = tempurature(city=WeatherCli.city, data=WeatherCli.data)
            print()
            print(values[-1])
            print()
            print(check_city_humidity(data=WeatherCli.data), sep="\n")
            print()
            sunset, sunrise = sunset_sunrise(data=WeatherCli.data)
            print(f"Sunrise in {WeatherCli.city} at {sunrise}, local time.")
            print(f"Sunset in {WeatherCli.city} at {sunset}, local time.")
        except requests.exceptions.HTTPError as e:
            if response.status_code == 404:
                print("City not found. Enter a valid city")
            else:
                print("Error occured while retrieving weather data\n", e)

    def do_tempurature(self, line):
        """
        Retrieve and display the current temperature for the specified city.
        Usage: tempurature
        """
        print_art("Tempurature")
        if WeatherCli.city is None or WeatherCli.data is None:
            WeatherCli.city = input("City's Name: ")
            parameters = {
                "q": WeatherCli.city,
                "appid": API_KEY,
                "units": "metric",
            }
            response = requests.get(BASE_URL, params=parameters)
            response.raise_for_status()
            WeatherCli.data = response.json()
        values = tempurature(city=WeatherCli.city, data=WeatherCli.data)
        print(values[-1])

    def do_humidity(self, line):
        """
        Retrieve and display the current humidity for the specified city.
        Usage: humidity
        """
        print_art("Humidity")
        if WeatherCli.city is None or WeatherCli.data is None:
            WeatherCli.city = input("City's Name: ")
            parameters = {
                "q": WeatherCli.city,
                "appid": API_KEY,
                "units": "metric",
            }
            response = requests.get(BASE_URL, params=parameters)
            response.raise_for_status()
            WeatherCli.data = response.json()
        print(check_city_humidity(WeatherCli.data))
    
    def do_suninfo(self, line):
        """
        Retrieve and display the sunrise and sunset times for the specified city.
        Usage: suninfo
        """
        print_art("SunInfo")
        if WeatherCli.city is None or WeatherCli.data is None:
            WeatherCli.city = input("City's Name: ")
            parameters = {
                "q": WeatherCli.city,
                "appid": API_KEY,
                "units": "metric",
            }
            response = requests.get(BASE_URL, params=parameters)
            response.raise_for_status()
            WeatherCli.data = response.json()
        sunset, sunrise = sunset_sunrise(WeatherCli.data)
        print(f"Sunrise in {WeatherCli.city} at {sunrise}, local time.")
        print(f"Sunset in {WeatherCli.city} at {sunset}, local time.")

    def do_art(self, line):
        """Generate ASCII art from text
        Usage: art <text> [--font <font_name>]
        Example: art Hello --font slant
        """
        if not line:
            print("Please provide text to generate art")
            return
        
        # Parse font from command line if provided
        if '--font' in line:
            parts = line.split('--font')
            text = parts[0].strip()
            font = parts[1].strip()
        else:
            text = line
            font = 'standard'
        
        print_art(text, font=font)
        
    def help_art(self):
        print("Generate ASCII art from text")
        print("Usage: art <text> [--font <font_name>]")
        print("Example: art Hello --font slant")
        print("Available fonts: standard, slant, script, etc.")
        print("Install pyfiglet for more font options")

    def postcmd(self, stop, line):
        # Default value for stop is False
        print()
        return stop
    
    def do_exit(self, line):
        """Exit the WeatherCli."""
        print("Exiting WeatherCli...")
        return True

    def do_quit(self, line):
        print("Exiting WeatherCli...")
        return True
    
if __name__ == "__main__":
    WeatherCli().cmdloop()
