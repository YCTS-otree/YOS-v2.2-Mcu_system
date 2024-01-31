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
import yos22
from st7735 import ST7735

LED = Pin(2,Pin.OUT,value=0)#初始化引脚
Buzzer = Pin(14,Pin.OUT)
switch = Pin(33,Pin.IN, Pin.PULL_UP)
lcdBL = Pin(5,Pin.OUT)
lcdBL.value(0)#先熄灭屏幕背光以免看到屏幕初始化

#初始化spi
spi=SPI(2, baudrate=40000000, polarity=0, phase=0, sck=Pin(18), mosi=Pin(23))
# 初始化LCD  rot 是显示方向，bgr是默认显示的颜色
lcd=ST7735(170, 200, spi,dc=Pin(21),cs=Pin(4),rst=Pin(22),rot=0,bgr=0)
print('Successfully initialized screen SPI')

#import BLE1
print('boot success')
while True:
    if switch.value() == 0:
        sleep(1)#长按一秒
        if switch.value() == 0:
            flash_num = 0
            while True:
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
                    sys = yos22.mainloop(lcd)#启动系统
                    if sys == 'shutdown':
                        LED.value(0)
                        break
                    #ecom.com()
        else:
            break#急停
    sleep(0.5)


