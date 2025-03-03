import cmd
import requests
from config import BASE_URL, API_KEY
from utils import temperature, check_city_humidity, sunset_sunrise
from art import print_art


class WeatherCli(cmd.Cmd):
    prompt = "Prompt🧭>> "
    intro = f"{print_art('WeatherCli')}\nTo get started, type 'hi'\nType 'help' for available commands\nType 'exit' to exit the CLI\n"
    city = None
    data = None

    def get_weather_data(self, city):
        """Fetch weather data from OpenWeatherMap API."""
        if not API_KEY:
            print("❌ Error: API key is missing. Please set it in config.py.")
            return None

        parameters = {
            "q": city,
            "appid": API_KEY.strip(),  # Remove unnecessary spaces
            "units": "metric",
        }

        try:
            response = requests.get(BASE_URL, params=parameters)
            response.raise_for_status()  # Raise error for non-200 responses
            return response.json()

        except requests.exceptions.HTTPError as e:
            if response.status_code == 401:
                print("❌ Error: Unauthorized. Check if your API key is correct.")
            elif response.status_code == 404:
                print("❌ City not found. Enter a valid city name.")
            else:
                print(f"❌ Error occurred while retrieving weather data:\n{e}")
        except requests.exceptions.RequestException as e:
            print(f"❌ Network error: {e}")

        return None

    def do_hi(self, line):
        """Greet the WeatherCli and start the weather data retrieval process."""
        print(f"Using WeatherCli and it works ;)\n")
        WeatherCli.city = input("🌍 City's Name: ").strip()

        WeatherCli.data = self.get_weather_data(WeatherCli.city)
        if not WeatherCli.data:
            return

        values = temperature(city=WeatherCli.city, data=WeatherCli.data)
        print("\n" + values[-1] + "\n")
        print(check_city_humidity(data=WeatherCli.data), sep="\n")
        print()
        sunset, sunrise = sunset_sunrise(data=WeatherCli.data)
        print(f"🌅 Sunrise in {WeatherCli.city} at {sunrise}, local time.")
        print(f"🌇 Sunset in {WeatherCli.city} at {sunset}, local time.")

    def do_temperature(self, line):
        """Retrieve and display the current temperature for the specified city."""
        print_art("Temperature")
        if not WeatherCli.city:
            WeatherCli.city = input("🌍 City's Name: ").strip()

        WeatherCli.data = self.get_weather_data(WeatherCli.city)
        if not WeatherCli.data:
            return

        values = temperature(city=WeatherCli.city, data=WeatherCli.data)
        print(values[-1])

    def do_humidity(self, line):
        """Retrieve and display the current humidity for the specified city."""
        print_art("Humidity")
        if not WeatherCli.city:
            WeatherCli.city = input("🌍 City's Name: ").strip()

        WeatherCli.data = self.get_weather_data(WeatherCli.city)
        if not WeatherCli.data:
            return

        print(check_city_humidity(WeatherCli.data))

    def do_suninfo(self, line):
        """Retrieve and display the sunrise and sunset times for the specified city."""
        print_art("SunInfo")
        if not WeatherCli.city:
            WeatherCli.city = input("🌍 City's Name: ").strip()

        WeatherCli.data = self.get_weather_data(WeatherCli.city)
        if not WeatherCli.data:
            return

        sunset, sunrise = sunset_sunrise(WeatherCli.data)
        print(f"🌅 Sunrise in {WeatherCli.city} at {sunrise}, local time.")
        print(f"🌇 Sunset in {WeatherCli.city} at {sunset}, local time.")

    def do_art(self, line):
        """Generate ASCII art from text.
        Usage: art <text> [--font <font_name>]
        Example: art Hello --font slant
        """
        if not line:
            print("⚠️ Please provide text to generate ASCII art.")
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
        """Show help for the 'art' command."""
        print("🎨 Generate ASCII art from text")
        print("Usage: art <text> [--font <font_name>]")
        print("Example: art Hello --font slant")
        print("Available fonts: standard, slant, script, etc.")
        print("Install 'pyfiglet' for more font options.")

    def postcmd(self, stop, line):
        """Adds a blank line after every command for better readability."""
        print()
        return stop

    def do_exit(self, line):
        """Exit the Weather CLI."""
        print("👋 Exiting WeatherCli...")
        return True

    def do_quit(self, line):
        """Exit the Weather CLI (alternative command)."""
        print("👋 Exiting WeatherCli...")
        return True


if __name__ == "__main__":
    WeatherCli().cmdloop()
