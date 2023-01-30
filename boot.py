import network
import urequests
import json
import max7219
from time import sleep


def connect_to_wifi(ssid, password):
    """Connect to the Wi-Fi network using the given SSID and password."""
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    wifi.connect(ssid, password)
    while not wifi.isconnected():
        pass
    return wifi


def display_subs(display, subs, last_string):
    """Display the given subscriber count on the SevenSegment display.
    Only update the display if the subscriber count has changed.
    """
    new_string = str(subs)
    if last_string == new_string:
        pass
    else:
        display.clear()
        display.number(subs)
    return new_string


def get_subs(api_key, channel_id):
    """Retrieve the subscriber count for the given channel using the YouTube API."""
    response = urequests.get(
        f"https://www.googleapis.com/youtube/v3/channels?part=statistics&id={channel_id}&key={api_key}"
    )
    data = json.loads(response.text)
    return int(data["items"][0]["statistics"]["subscriberCount"])


def main(wifi_ssid, wifi_password, api_key, channel_id, refresh_rate):
    """Main function to run the YouTube subscriber count display program."""
    last_string = ""
    wifi = connect_to_wifi(wifi_ssid, wifi_password)
    print(wifi.ifconfig())
    display = max7219.SevenSegment(cs=0, reverse=True)
    while True:
        subs = get_subs(api_key, channel_id)
        last_string = display_subs(display, subs, last_string)
        sleep(refresh_rate)


if __name__ == "__main__":
    wifi_ssid = ""
    wifi_password = ""
    api_key = ""
    channel_id = ""
    refresh_rate = 10  # in seconds
    main(wifi_ssid, wifi_password, api_key, channel_id, refresh_rate)
