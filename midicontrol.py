import mido
from mido import Message

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