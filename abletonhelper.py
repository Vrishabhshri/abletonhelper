import socket
import requests
import mido
from mido import Message

# Set up UDP listener
UDP_IP = "127.0.0.1"  # Localhost (same machine)
UDP_PORT = 9000  # The port you used in Max for Live (same as `udpsend` port)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print(f"Listening on {UDP_IP}:{UDP_PORT}...")

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

def control_ableton_with_plugins(plugins):
    # Set up a MIDI output port (check your port names with mido.get_output_names())
    port = mido.open_output('Your MIDI Port Name')

    for plugin in plugins:
        # Example: Set a plugin parameter
        # Assuming plugins are dictionaries with 'name' and 'parameter'
        # Send a MIDI Control Change message
        control_change_message = Message('control_change', control=plugin['parameter'], value=plugin['value'])
        port.send(control_change_message)
        print(f"Sent control change: {plugin['parameter']} = {plugin['value']}")

while True:
    # Listen for incoming messages
    data, addr = sock.recvfrom(1024)  # Buffer size is 1024 bytes
    print(f"Received message: {data.decode()} from {addr}")

    # Call Gemini API or process the message here
    instrument_description = data.decode()
    print(f"Processing instrument description: {instrument_description}")

    # Example: Query Gemini API for Ableton plugin recommendations
    plugins = get_ableton_plugins_from_gemini(instrument_description)
    
    # Example: Send instructions to Ableton (you can use Ableton's MIDI remote script or OSC)
    control_ableton_with_plugins(plugins)