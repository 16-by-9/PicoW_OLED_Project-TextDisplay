import board
import busio
import adafruit_ssd1306

# Message
msg = "A Pig without 9.89 is equal to 3.14, but a Pig without 3.14 is equal to 9.89..!"

# Setup I2C (SDA=GP0, SCL=GP1)
i2c = busio.I2C(scl=board.GP1, sda=board.GP0)

# Create the SSD1306 OLED class (128x64 display)
WIDTH = 128
HEIGHT = 64
display = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C)

# Clear display
display.fill(0)
display.show()

# --- Text wrapping helper ---
def wrap_text(text, max_chars):
    return [text[i:i + max_chars] for i in range(0, len(text), max_chars)]

# Wrap the text for ~21 characters per line (128px / 6px)
lines = wrap_text(msg, 21)

# Draw each line (8px high per line)
for i, line in enumerate(lines):
    if i * 8 >= HEIGHT:
        break
    display.text(line, 0, i * 8, 1)

# Show the result
display.show()