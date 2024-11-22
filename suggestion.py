weather_suggestions = {
    "thunderstorm with light rain": "Expect some lightning and light rain. Stay indoors and keep safe!",
    "thunderstorm with rain": "Thunder and rain combo! A good day to cozy up with a book inside.",
    "thunderstorm with heavy rain": "Heavy rain and thunderstorm ahead. Avoid going out unless necessary!",
    "light thunderstorm": "A mild thunderstorm is brewing. Keep an umbrella handy just in case.",
    "thunderstorm": "Thunderstorms are rolling through. Stay indoors and unplug sensitive electronics.",
    "heavy thunderstorm": "A strong storm is on the way. Avoid open areas and stay prepared.",
    "ragged thunderstorm": "Unpredictable weather ahead. Take shelter and avoid travel.",
    "thunderstorm with light drizzle": "Thunder and a light drizzle make it a moody day. Perfect for indoor relaxation.",
    "thunderstorm with drizzle": "Expect occasional rumbles of thunder with drizzles. Stay cautious.",
    "thunderstorm with heavy drizzle": "A stormy drizzle day—best to stay indoors.",
    "light intensity drizzle": "A gentle drizzle is in the air. A light jacket should do the trick.",
    "drizzle": "It's drizzling. A good time for a calm walk with an umbrella.",
    "heavy intensity drizzle": "A heavier drizzle is expected. Keep your raincoat handy!",
    "light intensity drizzle rain": "A mix of light rain and drizzle—don’t forget an umbrella!",
    "drizzle rain": "It's raining lightly with some drizzle. Stay dry!",
    "heavy intensity drizzle rain": "A wet day with heavy drizzle rain. Be prepared if you're heading out.",
    "shower rain and drizzle": "Short bursts of rain and drizzle. Perfect for a cozy day indoors.",
    "heavy shower rain and drizzle": "Heavy rain and drizzle showers. Avoid outdoor activities if possible.",
    "shower drizzle": "Drizzle showers are here. Keep an umbrella nearby!",
    "light rain": "Light rain is falling. Enjoy the soothing weather with a raincoat.",
    "moderate rain": "Moderate rain, carry an umbrella and enjoy the fresh air!",
    "heavy intensity rain": "Heavy rain ahead. Avoid going out unless necessary.",
    "very heavy rain": "Downpour alert! Stay indoors and keep warm.",
    "extreme rain": "Extreme rain expected. Be cautious and avoid travel.",
    "freezing rain": "Slippery conditions due to freezing rain. Wear appropriate footwear.",
    "light intensity shower rain": "A light rain shower refreshing but wet. Carry an umbrella!",
    "shower rain": "Expect periodic rain showers. A good day to stay cozy indoors.",
    "heavy intensity shower rain": "Heavy rain showers on the way. Keep an umbrella and stay safe.",
    "ragged shower rain": "Unpredictable rain showers. Stay prepared for wet conditions.",
    "light snow": "Light snow is falling. A magical day to enjoy outdoors.",
    "snow": "It's snowing! Dress warmly and enjoy the winter wonderland.",
    "heavy snow": "Heavy snow expected. Travel with caution and bundle up.",
    "sleet": "Icy sleet is falling. Be extra careful while walking or driving.",
    "light shower sleet": "Light sleet showers. Stay warm and cautious outdoors.",
    "shower sleet": "Sleet showers—perfect weather for a warm drink indoors.",
    "light rain and snow": "A mix of rain and snow. Stay warm and avoid slippery areas.",
    "rain and snow": "Rain and snow together! Dress warmly and carry waterproof gear.",
    "light shower snow": "Light snow showers. A beautiful sight to enjoy safely.",
    "shower snow": "Snow showers are here. Stay cozy and keep your feet dry.",
    "heavy shower snow": "Heavy snow showers. Limit travel and stay warm.",
    "mist": "Low visibility due to mist. Drive carefully and carry a light.",
    "smoke": "Smoky conditions. Avoid prolonged outdoor exposure.",
    "haze": "Hazy weather today. Stay indoors if you have allergies.",
    "sand/dust whirls": "Dusty conditions outside. Protect your eyes and face.",
    "fog": "Foggy weather ahead. Drive slowly and use fog lights.",
    "sand": "Sandy conditions. Wear protective gear and avoid long exposure.",
    "dust": "Dust is in the air. Use a mask and avoid outdoor activities.",
    "volcanic ash": "Volcanic ash in the air. Stay indoors and avoid exposure.",
    "squalls": "Windy squalls expected. Secure outdoor items and stay cautious.",
    "tornado": "Tornado warning! Seek shelter immediately and stay safe.",
    "clear sky": "It's a sunny day! Don't forget your sunglasses and sunscreen.",
    "few clouds": "A few clouds in the sky. A great day to be outdoors.",
    "scattered clouds": "Partly cloudy skies. Perfect weather for a walk or picnic.",
    "broken clouds": "Cloudy skies but still pleasant. Consider carrying a light jacket.",
    "overcast clouds": "Overcast skies ahead. A good day to stay indoors and relax.",
}


class Suggestion:
    def __init__(self, description, temperature):
        self.description = description
        self.temperature = temperature
        self.suggestion = self.get_suggestion()

    def get_suggestion(self):
        suggestion_on_condition = weather_suggestions.get(
            self.description, "Enjoy the day!"
        )
        temp_suggestion = self.get_temperature_suggestion()

        if "jacket" in suggestion_on_condition and "jacket" in temp_suggestion:
            temp_suggestion = temp_suggestion.replace("jacket", "another layer")
        if (
            "stay warm" in suggestion_on_condition.lower()
            and "stay warm" in temp_suggestion.lower()
        ):
            temp_suggestion = ""

        return f"{suggestion_on_condition} {temp_suggestion}".strip()

    def get_temperature_suggestion(self):
        if self.temperature < 0:
            return "It's freezing outside, dress warmly!"
        elif 0 <= self.temperature <= 15:
            return "It's chilly, consider wearing a jacket."
        elif 15 < self.temperature <= 30:
            return "The weather is pleasant, enjoy your day!"
        else:
            return "It's hot outside, stay hydrated!"
