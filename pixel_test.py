# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel


# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 32

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False,
                           pixel_order=ORDER)

def wipe(dir=0, speed=1, color=(0,0,0), pos=0, qty=num_pixels):
    for p in range(qty):
        if dir != 0:
            pixels[(p+pos) % num_pixels] = (0,0,0)
        else:
            pixels[(num_pixels-p-pos) % num_pixels - 1] = color
        pixels.show()
        time.sleep(.1/speed)

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos*3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos*3)
        g = 0
        b = int(pos*3)
    else:
        pos -= 170
        r = 0
        g = int(pos*3)
        b = int(255 - pos*3)
    return (r, g, b) if ORDER == neopixel.RGB or ORDER == neopixel.GRB else (r, g, b, 0)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)

try:
	while True:
	    # Comment this line out if you have RGBW/GRBW NeoPixels
	    #pixels.fill((255, 0, 0))
	    # Uncomment this line if you have RGBW/GRBW NeoPixels
	    # pixels.fill((255, 0, 0, 0))
	    #pixels.show()
	    wipe(color=(255,0,0))
	    time.sleep(3)
	    wipe(speed = 2, color=(0,255,0), pos = 16)

	    # Comment this line out if you have RGBW/GRBW NeoPixels
	    #pixels.fill((0, 255, 0))
	    # Uncomment this line if you have RGBW/GRBW NeoPixels
	    # pixels.fill((0, 255, 0, 0))
	    #pixels.show()
	    time.sleep(3)
	    wipe(speed=4,color=(0,0,255))

	    # Comment this line out if you have RGBW/GRBW NeoPixels
	    #pixels.fill((0, 0, 255))
	    # Uncomment this line if you have RGBW/GRBW NeoPixels
	    # pixels.fill((0, 0, 255, 0))
	    #pixels.show()
	    time.sleep(3)
	    wipe(speed = 8,dir=0, color=(255,255,255))

	    #pixels.fill((255, 255, 255))
	    #pixels.show()
	    time.sleep(3)
	    for w in range(int(num_pixels / 2)):
	        wipe(speed=4, color=(0,139,139), qty=1, pos=w)
	        wipe(speed=4, color=(75,0,130), pos=w + int(num_pixels / 2) , qty=1)
	    time.sleep(10)

	    for s in range(5):
	        for p in range(num_pixels):
	            pixels[p] = (75,0,130)
	            pixels[num_pixels - p - 1] = (0,139,139)
	            try:
	                pixels[p - 1] = (0,0,0)
	                pixels[num_pixels-p] = (0,0,0)
	            except:
	                pass
	            pixels.show()
	            time.sleep(.05)


	    for i in range(10):
	        rainbow_cycle(0.001)    # rainbow cycle with 1ms delay per step
except KeyboardInterrupt:
    wipe()
