
# YouTube Subscriber Count Display for D1 mini and 7-Segment Display

This is a simple script written in MicroPython to display your YouTube channel's subscriber count on a 7-segment 8-digit display. It is designed to work with a D1 mini microcontroller and the [`micropython-max7219` library](https://github.com/Andrew-Mullane/micropython-max7219) for controlling the 7-segment display.

## Requirements

- D1 mini microcontroller
- 7-segment 8-digit display
- MicroPython firmware installed on the D1 mini
- `micropython-max7219` library
- A YouTube API key and the ID of the channel you want to display the subscriber count for

## Usage

1. Clone this repository to your computer
2. Connect the 7-segment display to your D1 mini as described in the `micropython-max7219` library documentation
3. Copy `max7219.py` and `seven_segment_ascii.py` from the `micropython-max7219` library
4. Update the `wifi_ssid`, `wifi_password`, `api_key`, and `channel_id` variables in the code with your own values
5. Update the `refresh_rate` variable with the desired time interval in seconds for updating the subscriber count
6. Copy the code to your D1 mini
7. Run the code on the D1 mini and watch the subscriber count update on the 7-segment display!

## Video Tutorial

Check out the video tutorial for this project on YouTube: https://youtu.be/JOlrW2QbCfg

## Contributing

This code is provided as-is and any contributions or improvements are welcome. Feel free to create a pull request or open an issue on GitHub.
