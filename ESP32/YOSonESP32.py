#YOS-V2.2 BY OCR -----YCTS

import gc
from machine import Pin,SPI,UART#,free_ram
#from st7735 import ST7735
from time import sleep
from os import listdir
import lcdprint as lcdp
import _thread
#import bluetooth


# 初始化蓝牙UART对象
Bluetooth_uart = UART(2, baudrate=9600, rx=35,tx=32,timeout=10)

system_is_alive = True
#==========================================底层函数加载
def shell_output(text):
    print('\n' + text)
    #其他输出方式如：UART
    Bluetooth_uart.write('\n'+text)


# 用于存储输入的变量
command = None
#input_lock = _thread.allocate_lock()

print('loading system underlying functions')
# 处理输入的函数
def shell_input():
    print('shell_input function has been called ')
    global shell_input_thread_alive
    global command
    shell_input_thread_alive = True
    user_input = input("command:\n>>>")  # 用户输入
    command = user_input
    sleep(0.1)
    command = None#只保持0.1秒
    shell_input_thread_alive = False
    _thread.exit()

def Bluetooth_uart_input():
    print('\nBluetooth_uart_input function has been called ')
    global command
    #Bluetooth_uart.write("\ncommand:\n>>>")
    while command == None or command == '':
        
        if Bluetooth_uart.any():
            # 如果有数据 读入一行数据返回数据为字节类型
            # 例如  b'hello 1\n'
            bin_data = Bluetooth_uart.readline()
            command = bin_data.decode().strip()
            print('Bluetooth:>' + command + '<')
# 设为守护线程
#_thread.daemon = True


print('loading system')
def mainloop(lcd):#================================================系统
    global shell_input_thread_alive
    global command

        
    #初始化引脚
    LED = Pin(2,Pin.OUT)
    Buzzer = Pin(14,Pin.OUT)
    switch = Pin(33,Pin.IN, Pin.PULL_UP)
    lcdBL = Pin(5,Pin.OUT)
    lcdBL.value(0)#先熄灭屏幕背光以免看到屏幕初始化
    
    # 初始化SPI
    #spi=SPI(2, baudrate=40000000, polarity=0, phase=0, sck=Pin(18), mosi=Pin(23))已移至boot
    # 初始化LCD  rot 是显示方向，bgr是默认显示的颜色
    #lcd=ST7735(170, 200, spi,dc=Pin(21),cs=Pin(4),rst=Pin(22),rot=0,bgr=0)已移至boot

    lcdp.setlcd(lcd)#初始化lcdprinter
    lcdp.set(200,10,10)
    lcd.fill(0x0000)#填充黑屏
    Buzzer.value(1)
    sleep(0.1)
    Buzzer.value(0)
    sleep(0.05)
    Buzzer.value(1)
    
    lcdBL.value(1)#再点亮屏幕
    sleep(0.2)
    Buzzer.value(0)

    # 打印标题
    text = '   YOS on ESP32\n'
    lcdp.print_text(text,False)
    lcd.show()

    shell_output('Welcome to YOS  [version:1.2.2]\nYCTS All rights reserved.\nMade By OCR\n')






    #==================================================================函数加载

        #关机
    def shutdown_prompt():
        global system_is_alive
        Buzzer.value(1)
        lcdp.print_text('Shutdown!!!')
        shell_output('Shutdown!!!')
        lcd.show()
        lcd.fill(0x0000)
        sleep(1)
        lcdBL.value(0)
        Buzzer.value(0)
        system_is_alive = False


    #电源键
    def power_off():
        global system_is_alive
        while system_is_alive is True:
            sleep(0.3)
            if switch.value() == 0:
                sleep(3)#长按3秒
                if switch.value() == 0:
                    shutdown_prompt()

    power_off_thread = _thread.start_new_thread(power_off, ())#启动线程


    def EA_test(freq_input = None):
        
        lcdp.print_text('Initializing...')
        shell_output('Initializing...')
        lcd.show()
        SWave = Pin(12,Pin.OUT)
        lcdp.print_text('Test Electrical \nadjustment on Pin12')
        shell_output('Test Electrical adjustment on Pin12')
        lcd.show()
        
        while True:
            sleep(0.21)#command有效时间持续0.1s,防止串台
            #freq = input('freq:')
            if freq_input is None:
                _thread.start_new_thread(shell_input, ())#启动后台shell_input线程
                Bluetooth_uart.write("\nfreq:")
                Bluetooth_uart_input()#蓝牙输入循环阻断主进程，直到后台shell_input或蓝牙接收到消息跳出循环
                freq = command
            else:
                freq = freq_input

            try:#检测输入是否有效
                freq = float(freq)
                
            except:
                if freq != '' and freq is not None:#防止故意退出时的误报
                    shell_output('square_wave:Value error')
                    lcdp.settc(0xFF00)
                    lcdp.print_text('square_wave:Value \nerror')
                    lcdp.settc(0xFFFF)
                break
            

            lcdp.print_text('start output square\nwave\nFrequency:' + str(freq) + '\n')
            shell_output('start output square wave Frequency:' + str(freq) + '\n')
            
            lcd.show()
            if freq > 0:
                period =1/freq#周期
                #dtime = period/2#半个周期
                
                lcdp.print_text('Press the button to\nenter the next stage',text_color = 0xFF00)
                lcdp.print_text('Output Max throttle',text_color = 0x00FF)
                lcd.show()
                Duty_cycle = 0.3
                high_level = period*Duty_cycle
                low_level = period-high_level
                while switch.value() != 0:#按钮未按下
                    SWave.value(1)
                    sleep(high_level)
                    SWave.value(0)
                    sleep(low_level)
                
                lcdp.print_text('Output Min throttle',text_color = 0x00FF)
                lcd.show()
                sleep(0.5)
                Duty_cycle = 0.1
                high_level = period*Duty_cycle
                low_level = period-high_level
                while switch.value() != 0:#按钮未按下
                    SWave.value(1)
                    sleep(high_level)
                    SWave.value(0)
                    sleep(low_level)

                lcdp.print_text('Output medium throttle',text_color = 0x00FF)
                lcd.show()
                sleep(0.5)
                Duty_cycle = 0.2
                high_level = period*Duty_cycle
                low_level = period-high_level
                while switch.value() != 0:#按钮未按下
                    SWave.value(1)
                    sleep(high_level)
                    SWave.value(0)
                    sleep(low_level)
                
                freq = None
            else:
                break




    def dir():
        lcd.fill(0x0000)#屏幕填充
        lcdp.set(200,10,10)
        #获得文件信息
        dirlist = listdir()
        lcdp.print_text('dir:')
        shell_output('dir:')
        lcd.show()
        for i in range(len(dirlist)):
            shell_output(' |-'+str(dirlist[i]))
            lcdp.print_text(' |-'+str(dirlist[i]))
        lcdp.print_text('')
        lcd.show()

    def LED_test():
        lcdp.settc(0x0000FF)
        lcdp.print_text('Test LED at pin 2')
        shell_output('Test LED at pin 2')
        LED.value(1)
        sleep(1)
        LED.value(0)


    def sys_sleep():
        Buzzer.value(1)
        sleep(0.5)
        Buzzer.value(0)
        lcdp.print_text('Close the YOS and screen')
        shell_output('Close the YOS and screen')
        lcd.show()
        sleep(1)
        lcdBL.value(0)

    def square_wave(f,dc):
        lcdp.print_text('Initializing...')
        shell_output('Initializing...')
        lcd.show()
        SWave = Pin(12,Pin.OUT)
        lcdp.print_text('Output square wave\non Pin12')
        shell_output('Output square wave on Pin12')
        lcd.show()
        while True:
            if f != None and dc != None:#判断是否有参数
                freq = f
                Duty_cycle = dc
            else:#没有则输入
                freq = input('freq:')
                Duty_cycle = input('Duty cycle(%):')


            try:#检测输入是否有效
                freq = float(freq)
                Duty_cycle = int(Duty_cycle)/100
            except:
                if freq != '' and freq is not None and Duty_cycle != '' and Duty_cycle is not None:#防止故意退出时的误报
                    shell_output('square_wave:Value error')
                    lcdp.settc(0xFF00)
                    lcdp.print_text('square_wave:Value \nerror')
                    lcdp.settc(0xFFFF)
                break

            lcdp.print_text('start output square\nwave\nFrequency:' + str(freq) + 'Hz\nDuty cycle:' + str(Duty_cycle*100) + '%\n')
            shell_output('start output square wave\nFrequency:' + str(freq) + 'Hz\nDuty cycle:' + str(Duty_cycle*100) + '%\n')
            lcd.show()
            if freq > 0:
                period =1/freq#周期
                #dtime = period/2#半个周期
                high_level = period*Duty_cycle
                low_level = period-high_level
                while switch.value() != 0:#按钮未按下
                    SWave.value(1)
                    sleep(high_level)
                    SWave.value(0)
                    sleep(low_level)
            else:
                dc = None
                f = None#防止死循环
                break
            dc = None
            f = None#重置

    def easter_egg_2024():
        sleep(3)
        lcdp.print_text('   2',True)
        sleep(0.8)
        lcd.show()
        lcdp.print_text('    0',True)
        sleep(0.8)
        lcd.show()
        lcdp.print_text('     2',True)
        sleep(0.8)
        lcd.show()
        lcdp.print_text('      4',True)
        sleep(0.8)
        lcd.show()
        sleep(1)
        lcd.fill(0x0000)#屏幕填充
        lcd.show()
        text2023 = 'Goodbye,2023'
        text2024 = 'Hello,2024!!!'
        lcdp.set(200,20,34)
        lcdp.setsize(20)
        lcdp.print_text('     ')
        lcd.show()
        for i in range(len(text2023)):
            lcdp.print_text('   '+' '*i+text2023[i],True)
            lcd.show()
            sleep(0.3)

        lcdp.set(200,20,74)
        
        for i in range(len(text2024)):
            lcdp.print_text('   '+' '*i+text2024[i],True)
            lcd.show()
            sleep(0.3)
        sleep(3)
        lcd.fill(0x0000)
        lcdp.set(200,10,10)
        lcdp.setsize(10)


    shell_input_thread_alive = False
    command = None
    while system_is_alive == True:#主循环
        gc.collect ()#清理内存
        lcdp.print_text('command:\n>>>')
        lcd.show()
        #command = input('command:\n>>>')
        if shell_input_thread_alive is False:#进程是否存活
            shell_input_thread = _thread.start_new_thread(shell_input, ())#启动线程
            lcdp.print_text('command:\n>>>')
            lcd.show()
        '''if shell_input_thread_alive is False:#进程是否存活
            shell_input_thread = _thread.start_new_thread(shell_input, ())#启动shell线程'''
        Bluetooth_uart.write("\ncommand:\n>>>")
        Bluetooth_uart_input()#蓝牙输入循环阻断主进程，直到后台shell_input或蓝牙接收到消息跳出循环
        
        if command != None:
            print(command)
            lcdp.print_text('   ' + command,True)#不换行打印
            lcd.show()
            command = command.split(' ')
            if command[0] == 'dir':
                dir()
            elif command[0] == 'shutdown':
                shutdown_prompt()
                
            elif command[0] == 'sleep':
                sys_sleep()
                break
            elif command[0] == 'LED':
                LED_test()
            elif command[0] == '2024':
                easter_egg_2024()
            elif command[0] == 'square_wave' or command[0] == 'square':#两种写法
                if len(command) == 3 and command[0] == 'square_wave':#写法1：square_wave
                    square_wave(command[1],command[2])
                elif len(command) == 4 and command[0]+command[1] == 'squarewave':#写法2：square wave
                    square_wave(command[2],command[3])
                else:
                    square_wave(None,None)
            elif command[0] == 'EA_test':#电调测试
                if len(command) > 1:
                    EA_test(command[1])
                else:
                    EA_test()
            elif command[0] == 'cls':
                lcd.fill(0x0000)
            elif command[0] == 'RAM':
                total_ram = gc.mem_alloc() + gc.mem_free()
                free_ram = gc.mem_free()
                lcdp.print_text('Total RAM:' + str(round(total_ram/1024,3)) + 'KB')
                shell_output('Total RAM:' + str(round(total_ram/1024,3)) + 'KB')
                lcdp.print_text('Free RAM:' + str(round(free_ram/1024,3)) + 'KB')
                shell_output('Free RAM:' + str(round(free_ram/1024,3)) + 'KB')
                lcd.show()
            elif command[0] == 'cleanRAM':
                gc.collect ()
            elif command[0] == '' or None:
                pass
            else:
                shell_output('no command name:' + str(command[0]))
            command = None
        
    if system_is_alive == False:
        return 'shutdown'