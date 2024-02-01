# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()
#import test.py


#import yos
#import ecom
import gc
from machine import Pin, SPI
from time import sleep
from st7735 import ST7735

print('Initializing Pins')
LED = Pin(13,Pin.OUT,value=0)#初始化引脚
Buzzer = Pin(21,Pin.OUT)
switch = Pin(38,Pin.IN, Pin.PULL_UP)
lcdBL = Pin(15,Pin.OUT)
lcdBL.value(0)#先熄灭屏幕背光以免看到屏幕初始化

#初始化spi
print('Initializing screen SPI')
spi=SPI(2, baudrate=20000000, polarity=0, phase=0, bits=8, firstbit=SPI.MSB, sck=Pin(12), mosi=Pin(14), miso=Pin(47))#不能没有miso！！！！！！！！！！！！会卡死
# 初始化LCD  rot 是显示方向，bgr是默认显示的颜色
print('Initializing LCD')
lcd=ST7735(width=320, height=240,spi=spi ,dc=Pin(11), cs=Pin(10), rst=Pin(4), rot=0, bgr=0)


#import BLE1
print('boot success')
while True:
    if switch.value() == 0:
        sleep(0.7)#长按0.7秒
        if switch.value() == 0:
            flash_num = 0
            while True:
                import yos23
                print('sleeping')
                flash_num = flash_num + 1
                if flash_num <= 5:
                    LED.value(1)
                else:
                    LED.value(0)
                if flash_num > 10:
                    flash_num = 0
                
                sleep(0.2)
                #print(switch.value())
                if switch.value() == 0:
                    print('Start up!')
                    LED.value(0)
                    Buzzer.value(1)
                    sleep(0.3)
                    LED.value(1)
                    Buzzer.value(0)
                    
                    gc.collect ()#清理内存
                    sys = yos23.mainloop(lcd)#启动系统
                    if sys == 'shutdown':
                        LED.value(0)
                        break
                    #ecom.com()
        else:
            break#急停
    sleep(0.5)


