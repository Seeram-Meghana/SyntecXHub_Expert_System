# Rule-Based Expert System: Weather Prediction System

def forward_chain(facts, rules):
    inferred = set(facts)
    log = []
    changed = True

    while changed:
        changed = False
        for rule in rules:
            conditions = rule["conditions"]
            result = rule["result"]

            # Check if rule conditions are satisfied
            if all(cond in inferred for cond in conditions):
                if result not in inferred:
                    inferred.add(result)
                    log.append(f"Rule applied: {conditions} → {result}")
                    changed = True

    return inferred, log


def predict_weather(data):
    
    rules = [
        {"conditions": ["high_humidity", "dark_clouds"], "result": "rain"},
        {"conditions": ["low_temperature", "high_humidity"], "result": "fog"},
        {"conditions": ["high_temperature", "clear_sky"], "result": "hot_day"},
        {"conditions": ["moderate_temperature", "windy"], "result": "breezy"},
        {"conditions": ["dark_clouds", "windy"], "result": "thunderstorm"},

       
        {"conditions": ["rain"], "result": "wet_ground"},
        {"conditions": ["thunderstorm"], "result": "power_cut_warning"}
    ]

    
    explanations = {
        "rain": "Prediction: High chance of rain.",
        "fog": "Prediction: Foggy weather possible.",
        "hot_day": "Prediction: Hot and sunny day.",
        "breezy": "Prediction: Cool and breezy weather.",
        "thunderstorm": "Prediction: Thunderstorm likely.",
        "wet_ground": "Inference: Rain may cause wet ground.",
        "power_cut_warning": "Inference: Thunderstorm may lead to a power cut."
    }

   
    final_facts, logs = forward_chain(data, rules)

    return final_facts, logs, explanations



# ---------------- USER INTERFACE ----------------

print("WEATHER PREDICTION EXPERT SYSTEM\n")
print("Enter conditions such as:")
print("high_humidity, low_humidity, dark_clouds, clear_sky, windy,")
print("high_temperature, low_temperature, moderate_temperature")

user_input = input("\nEnter conditions separated by commas: ")


conditions = [c.strip().lower() for c in user_input.split(",")]


final_facts, log_steps, explanations = predict_weather(conditions)


print("\n--- INFERENCE LOG ---")
if log_steps:
    for step in log_steps:
        print(step)
else:
        print("No rules were triggered.")


print("\n--- FINAL WEATHER OUTPUT ---")
found = False
for fact in final_facts:
    if fact in explanations:
        print(explanations[fact])
        found = True

if not found:
    print("Prediction: Unable to determine weather with given conditions.")
    print("\n")
