# This library is made by Ouchurui(YCTS研创工作室)
# Front library: st7735
# import st7735

'''
初始化：(必须设置)
setlcd(st7735的lcd设置)
st7735的lcd设置:st7735.ST7735(宽, 高, spi,dc=Pin(引脚号),cs=Pin(引脚号),rst=Pin(引脚号),rot=0,bgr=0)#rot为显示方向,bgr为初始化默认为0,即初始填充黑屏

打印在屏幕：
print_text(文本, 换行判断,text_color)
换行判断:是True就不换行,换行为False
text_color:颜色,0x0000

打印设置：
    坐标设置：
    set('屏幕高度','行高','Y起始坐标')
    颜色设置：
    settc(颜色)#例：0xFFFF
    字号设置：
    setsize(大于0的整数)














'''


#from cgitb import text

tsize = 10
bgc = 0x0000
text_color = 0xFFFF
lcdprint_text_y = 10
line_height = 10
lcd_y = 10
def set(y,lineheight, set_start_y):
    global lcdprint_text_y
    global line_height
    line_height = lineheight
    global lcd_y
    lcd_y = y
    global start_y
    start_y = set_start_y
    
    lcdprint_text_y = set_start_y

def setlcd(setlcd):#设置lcd
    global lcd
    lcd = setlcd

def settc(color):#文字色
    global text_color
    text_color = color

def setbc(bgcolor):#背景色
    global bgc
    bgc = bgcolor

def setsize(setsize):#字号
    global tsize
    tsize = setsize

def print_text(text, un_line_feed = False, text_color = 0xFFFF):#给定默认值以可以不传入参数
    try:

        global lcdprint_text_y
        text = str(text)
        if '\n' in text:
            textlist = text.split('\n')
            for i in range(0, len(textlist)):
                if un_line_feed is False:#换行，是True就不换行
                    if lcdprint_text_y + line_height > lcd_y:
                        lcd.fill(bgc)
                        lcdprint_text_y = start_y + line_height
                    else:
                        lcdprint_text_y += line_height
                    lcd.text(textlist[i],tsize,lcdprint_text_y,text_color)#打印
                else:
                    lcd.text(textlist[i],tsize,lcdprint_text_y,text_color)#打印
        else:
            if un_line_feed is False:#换行，是True就不换行
                if lcdprint_text_y + line_height > lcd_y:
                    lcdprint_text_y = start_y + line_height
                else:
                    lcdprint_text_y += line_height
            lcd.text(text,10,lcdprint_text_y,text_color)#打印
    except NameError:
        print('Uninitialized: use "setlcd(st7735.ST7735(width, height, spi, dc=Pin (pin number), cs=Pin (pin number), rst=Pin (pin number), rot=0, bgr=0))" for initialization')
        return 'Uninitialized: use "setlcd(st7735.ST7735(width, height, spi, dc=Pin (pin number), cs=Pin (pin number), rst=Pin (pin number), rot=0, bgr=0))" for initialization'
        



'''
print_text('bbb\naaa',False)
print('1')
'''
