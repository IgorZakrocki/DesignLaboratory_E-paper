from display import *
import time
import json
import logging
import epd7in5bc

rain_next_hour = [["+10'", 0], ["+20'", 1], ["+30'", 1], ["+40'", 0], ["+50'", 0], ["+1h", 1]]

def main():
  
    ##################################################################################################################

    display.draw_black.rectangle((5, 5, 635, 379), fill=255, outline=0, width=2)
    #display.draw_black.line((350, 5, 350, 288), fill=0, width=1)
    #display.draw_black.line((5, 288, 635, 288), fill=0, width=1)
    #display.draw_black.line((5, 350, 795, 350), fill=0, width=1)

    ###################################################################################################################

    display.draw_icon(20, 30, "r", 75, 75,"drizzle")
    display.draw_black.text((120, 15), "5*C", fill=0, font=font48)
    display.draw_black.text((230, 15), "55%", fill=0, font=font48)
    display.draw_black.text((245, 65), "Humidity", fill=0, font=font12)
    display.draw_black.text((120, 75), "22km/h" + " " + "SE", fill=0, font=font24)

    display.draw_icon(120, 105, "b", 35, 35, "sunrise")
    display.draw_black.text((160, 110), "08:15", fill=0, font=font16)
    display.draw_icon(220, 105, "b", 35, 35, "sunset")
    display.draw_black.text((260, 110), "16:34", fill=0, font=font16)

    display.draw_black.text((20, 150), "Rain forecast for the next hour - " + time.strftime("%H:%M", time.localtime()), fill=0, font=font16)
    display.draw_black.rectangle((20, 175, 320, 195), fill=255, outline=0, width=1)
    
    for i in range(6):
            display.draw_black.line((20 + i * 50, 175, 20 + i * 50, 195), fill=0, width=1)
            display.draw_black.text((20 + i * 50, 195), rain_next_hour[i][0], fill=0, font=font16)
            if rain_next_hour[i][1] != 0:
                display.draw_red.rectangle((20 + i * 50, 175, 20 + (i + 1) * 50, 195), fill=0)

	###################################################################################################################

    display.draw_black.text((30, 227), "+3h", fill=0, font=font16)
    display.draw_black.text((150, 227), "+6h", fill=0, font=font16)
    display.draw_black.text((270, 227), "+12h", fill=0, font=font16)

    display.draw_icon(25, 245, "r", 50, 50, "snow")
    display.draw_black.text((25, 295), "snow", fill=0, font=font12)
    display.draw_black.text((35, 307), "0*C", fill=0, font=font16)
    display.draw_black.text((35, 323), "15%", fill=0, font=font16)

    display.draw_icon(145, 245, "r", 50, 50, "snow")
    display.draw_black.text((145, 295), "snow", fill=0, font=font12)
    display.draw_black.text((155, 307), "5*C", fill=0, font=font16)
    display.draw_black.text((155, 323), "33%", fill=0, font=font16)

    display.draw_icon(265, 245, "r", 50, 50, "snow")
    display.draw_black.text((265, 295), "snow", fill=0, font=font12)
    display.draw_black.text((275, 307), "2*C", fill=0, font=font16)
    display.draw_black.text((275, 323), "10%", fill=0, font=font16)

    
    ###################################################################################################################
 
    display.draw_black.text((360, 30), "Wednesday", fill=0, font=font16)
    display.draw_icon(400, 50, "r", 50, 50, "25_clouds")
    display.draw_black.text((465, 50), "0*C", fill=0, font=font14)
    display.draw_black.text((498, 50), "min", fill=0, font=font14)
    display.draw_black.text((465, 65), "2*C", fill=0, font=font14)
    display.draw_black.text((498, 65), "max", fill=0, font=font14)
    display.draw_black.text((465, 80), "82%", fill=0, font=font14)
    display.draw_black.text((498, 80), "humidity", fill=0, font=font14)

    display.draw_black.text((360, 105), "Thursday", fill=0, font=font16)
    display.draw_icon(400, 125, "r", 50, 50, "50_clouds")
    display.draw_black.text((465, 125), "-2*C", fill=0, font=font14)
    display.draw_black.text((498, 125), "min", fill=0, font=font14)
    display.draw_black.text((465, 140), "1*C", fill=0, font=font14)
    display.draw_black.text((498, 140), "max", fill=0, font=font14)
    display.draw_black.text((465, 155), "73%", fill=0, font=font14)
    display.draw_black.text((498, 155), "humidity", fill=0, font=font14)

    display.draw_black.text((360, 180), "Friday", fill=0, font=font16)
    display.draw_icon(400, 200, "r", 50, 50, "100_clouds")
    display.draw_black.text((465, 200), "-4*C", fill=0, font=font14)
    display.draw_black.text((498, 200), "min", fill=0, font=font14)
    display.draw_black.text((465, 215), "-1*C", fill=0, font=font14)
    display.draw_black.text((498, 215), "max", fill=0, font=font14)
    display.draw_black.text((465, 230), "85%", fill=0, font=font14)
    display.draw_black.text((498, 230), "humidity", fill=0, font=font14)

    display.draw_black.text((360, 255), "Saturday", fill=0, font=font16)
    display.draw_icon(400, 275, "r", 50, 50, "thunder")
    display.draw_black.text((465, 275), "2*C", fill=0, font=font14)
    display.draw_black.text((498, 275), "min", fill=0, font=font14)
    display.draw_black.text((465, 290), "5*C", fill=0, font=font14)
    display.draw_black.text((498, 290), "max", fill=0, font=font14)
    display.draw_black.text((465, 305), "89%", fill=0, font=font14)
    display.draw_black.text((498, 305), "humidity", fill=0, font=font14)

    ###################################################################################################################

    epd.display(epd.getbuffer(display.im_black), epd.getbuffer(display.im_red))
    time.sleep(2)
    
while True:   
	epd = epd7in5bc.EPD()
	print("Creating display")
	display = Display()
	epd.init()
	epd.Clear()
	print("Main program running...")
	main()
	print("Going to sleep...")
	epd.init()
	epd.sleep()
	print("Sleeping")
	print("Done")
	time.sleep(1800)
