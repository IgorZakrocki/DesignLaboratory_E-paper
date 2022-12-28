import epd7in5bc
import time
print("Starting shut down")
epd = epd7in5bc.EPD()
epd.init()
time.sleep(1)
print("Clearing...")
epd.Clear()
time.sleep(2)
print("Exiting !")
exit()
