## This code changes your Windows 10 Desktop Background on a daily basis (at 00:00 hours) using Windows Task Scheduler for an upcoming event to which you want to keep yourself motivated

## User custom inputs are to be changed only inside the quotes (" ")
year_of_event                = "2021"
month_of_the_event           = "9"
##          1      2      3      4      5      6       7      8      9     10     11      12
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
date_of_the_event            = "21"
font_color                   = "white"
background_color             = "black"
event                        = "exam"


##Importing necessary Libraries
from PIL import Image, ImageDraw, ImageFont
from os import getcwd, remove
from time import sleep
from ctypes import windll

##Fetching Screen Resolution
from win32api import GetSystemMetrics
resX = GetSystemMetrics(0)
resY = GetSystemMetrics(1)

## Choose any of your favorite font style from r"C:\Windows\Fonts" and set it below
days_num = ImageFont.truetype(r'COOPBL', 115)
days_left = ImageFont.truetype(r'COOPBL', 35)
image = Image.new(mode = "RGB", size = (resX, resY), color = background_color)
draw = ImageDraw.Draw(image)

#Creating the image
import datetime
interval = datetime.date(int(year_of_event), int(month_of_the_event), int(date_of_the_event)) - datetime.date.today()
cwd = getcwd()

#draw.text(resX/2 - (len(str(interval.days))/2), resX/2 - int(115/2), f'{interval.days}', font = days_num, fill=(255,255,255), align='center')
#draw.text(resX/2 - (len(str(interval.days))/2), resX/2 - int(25/2),"days  left  for  the  exam\n", font = days_left, fill=(255,255,255), align='center')
draw.text((610,220), f'{interval.days}', font = days_num, fill = font_color, align = 'center')
draw.text((460,340),"days  left  for  the  " + event, font = days_left, fill = font_color)
draw.text((530,340),"End = {0}/{1}/{2}".format(date_of_the_event, months[int(month_of_the_event)-1], year_of_event), font = days_left, fill = font_color)
image.save(cwd + r'\PyImage.png')

##Setting Desktop Background
windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER := 20, 0, cwd + r'\PyImage.png' , SPIF_UPDATEINIFILE := 0)
sleep(1)
remove(cwd + r'\PyImage.png')
