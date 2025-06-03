# OLED Text Display on Raspberry Pi Pico W (CircuitPython)

This is a simple OLED text display project for the Raspberry Pi Pico W using CircuitPython and an SSD1306 128x64 display. It prints a wrapped, multiline quote to the screen using Adafruit’s libraries.

---

## 📦 Requirements

This project **requires CircuitPython** installed on your Raspberry Pi Pico W and the following **libraries** and **support files** placed in your `lib/` folder:

### ✅ Required Libraries
- `adafruit_ssd1306`
- `adafruit_display_text`
- `adafruit_cursorcontrol`
- `adafruit_gfx`
- `adafruit_framebuf.mpy`

### 📁 Required Files
- `font5x8.bin` (place this in the root of your CIRCUITPY drive or inside `lib/` if required/overridden by any of your other font functions)

### 🔲 Optional (for shapes and more visuals later)
- `adafruit_display_shapes`

All these can be downloaded from the [Adafruit CircuitPython Bundle](https://circuitpython.org/libraries).

---

## 🔧 Wiring (for Raspberry Pi Pico W)

| OLED Pin | Pico W Pin |
|----------|------------|
| **VCC**  | 3.3V       |
| **GND**  | GND        |
| **SDA**  | GP0        |
| **SCL**  | GP1        |

---

## 🧠 Code Summary

This program:
- Initializes the OLED via I2C using `adafruit_ssd1306`
- Wraps long text into multiple lines
- Displays it clearly using `display.text()`
- Ensures everything fits within the 128x64 screen

---

## 📝 How to Use

1. Flash CircuitPython to your Pico W from [circuitpython.org](https://circuitpython.org/board/raspberry_pi_pico_w/).
2. Copy the `.py` code file to your CIRCUITPY drive.
3. Add the required libraries and files to the required directories.
4. Plug in your OLED display with correct wiring.
5. Reboot or run the script via Thonny or auto `code.py`.