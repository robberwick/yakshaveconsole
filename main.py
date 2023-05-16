from machine import Pin, I2C
import ssd1306
import time
import random

# time to sleep between checks
SLEEP_INTERVAL = 300
# random number will be between 0-255. if above this theshold, a yak will be shaved
YAK_SHAVE_THRESHOLD = 240

# using default address 0x3C
i2c = I2C(sda=Pin(4), scl=Pin(5))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

def get_count():
    file = open("count.txt", "r")
    count = int(file.read())
    file.close()
    return count
    
def write_count(num_yaks):
    file = open("count.txt", "w")
    file.write(str(num_yaks))
    file.close()

def update_display(num_yaks):
    display.fill(0)
    display.text('  Yak Console', 0, 0, 1)
    display.text('Number shaved:', 0, 20, 1)
    display.text(str(num_yaks), 0, 40, 1)
    display.show()

def yak_is_shaved():
    return random.getrandbits(8) > YAK_SHAVE_THRESHOLD

num_yaks = get_count()
update_display(num_yaks)

while True:
    time.sleep(SLEEP_INTERVAL)
    if yak_is_shaved():
        num_yaks = num_yaks + 1
        write_count(num_yaks)
        update_display(num_yaks)