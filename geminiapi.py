import requests

def get_ableton_plugins_from_gemini(instrument_description):
    # Make a request to Gemini API (example)
    gemini_url = "https://api.gemini.com/v1/plugins"
    response = requests.post(gemini_url, json={"description": instrument_description})

    if response.status_code == 200:
        plugins = response.json()
        print(f"Received plugins from Gemini: {plugins}")
        return plugins
    else:
        print(f"Error fetching plugins: {response.status_code}")
        return []