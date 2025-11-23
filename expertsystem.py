# Rule-Based Expert System: Weather Prediction System

def predict_weather(data):
    rules = [
        {
            "conditions": ["high_humidity", "dark_clouds"],
            "result": "Prediction: High chance of rain."
        },
        {
            "conditions": ["low_temperature", "high_humidity"],
            "result": "Prediction: Foggy weather possible."
        },
        {
            "conditions": ["high_temperature", "clear_sky"],
            "result": "Prediction: Hot and sunny day."
        },
        {
            "conditions": ["moderate_temperature", "windy"],
            "result": "Prediction: Cool and breezy weather."
        },
        {
            "conditions": ["dark_clouds", "windy"],
            "result": "Prediction: Thunderstorm likely."
        },
        {
            "conditions": ["clear_sky"],
            "result": "Prediction: Pleasant weather."
        }
    ]

    for rule in rules:
        match = all(condition in data for condition in rule["conditions"])
        if match:
            return rule["result"]

    return "Prediction: Unable to determine weather with given conditions."



print("WEATHER PREDICTION EXPERT SYSTEM\n")
print("Enter conditions such as:")
print("high_humidity, low_humidity, dark_clouds, clear_sky, windy, high_temperature, low_temperature, moderate_temperature")

user_input = input("\nEnter conditions separated by commas: ")


conditions = [c.strip().lower() for c in user_input.split(",")]

result = predict_weather(conditions)

print("\n" + result)
