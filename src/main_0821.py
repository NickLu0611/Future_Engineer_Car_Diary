import cv2
import pigpio
import numpy as np
from Motor_control_function import *
from compass_function import BNO055
import RPi.GPIO as GPIO
from Tool_function import *
import board
from TCS34725 import *
import threading
import time

#-----------------------------------------------------
Motor = Motor_control(23, 24, 25, 12) #定義馬達腳位(馬達前進腳位, 馬達後退腳位, 馬達速度控制腳位, 伺服馬達控制腳位)
GPIO.setwarnings(False)
GPIO.setmode (GPIO.BCM)
GPIO.setup (20,GPIO.OUT)#matrix 控制D3腳位(如果程式啟動，腳位輸出電力給matrix mini，告知程式已經開啟)
GPIO.setup (21,GPIO.IN) #matrix 控制D4腳位(如果程式啟動，matrix mini 按下按鈕，腳位讀取電力告知開始運行)
pi = pigpio.pi()
bno = BNO055()
i2c = board.I2C()
tcs34725 = TCS34725()
#-----------------------------------------------------


def get_m(x, x0, y, y0):
    return (y-y0)/(x-x0)

def get_x(m, x, y, y0):
    return (m(y-y0))+x

def gyro_convert(angle):
    gyro_value = bno.getVector(bno.VECTOR_EULER)
    error = angle - round(gyro_value) + 180
    if error >= 0:
        rel_gyro = error % 360 - 180
    else:
        rel_gyro = 359 - (-1 - error) % 360 - 180
    return int(rel_gyro)

def Color_Detect(imageFrame):
    red_x = -1
    green_x = -1
    red_y = -1
    green_y = -1
    red_area = 0
    green_area = 0
    hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)
    red_lower = np.array([0, 90, 0], np.uint8) #紅色積木判斷範圍的最小值
    red_upper = np.array([5, 255, 255], np.uint8)#紅色積木判斷範圍的最大值
    red_lower2 = np.array([170, 90, 0], np.uint8)#紅色積木判斷範圍的最小值
    red_upper2 = np.array([180, 255, 255], np.uint8)#紅色積木判斷範圍的最大值
    red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)
    red_mask2 = cv2.inRange(hsvFrame, red_lower2, red_upper2)
    red_mask = red_mask | red_mask2
    green_lower = np.array([50, 120, 85], np.uint8)#綠色積木判斷範圍的最小值
    green_upper = np.array([68, 255, 230], np.uint8) #綠色積木判斷範圍的最大值
    green_mask = cv2.inRange(hsvFrame, green_lower, green_upper)
    
    contours, hierarchy = cv2.findContours(red_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
    red_num = 0
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 150) and area > red_area: #紅色積木面積大於150的時候，表示看到紅色積木了
            red_num += 1
            red_area = area
            x, y, w, h = cv2.boundingRect(contour)
            red_x = x+w*2
            red_y = y+h
            imageFrame = cv2.rectangle(imageFrame,
                                       (x, y),
                                       (x + w, y + h),
                                       (0, 0, 255), 2)

    contours, hierarchy = cv2.findContours(green_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)

    green_num = 0
    for pic, contour in enumerate(contours):
        green_num += 1
        area = cv2.contourArea(contour)
        if(area > 150) and area > green_area: #綠色積木面積大於150的時候，表示看到綠色積木了
            green_area = area
            x, y, w, h = cv2.boundingRect(contour)
            green_x = x
            green_y = y+h
            imageFrame = cv2.rectangle(imageFrame, (x, y),
                                       (x + w, y + h),
                                       (0, 255, 0), 2)
            
            
    return imageFrame, red_x, red_y, green_x, green_y, red_area, green_area, red_num, green_num


def Draw_Line (img, red_x, red_y, green_x, green_y, gyro):
    R_LineToX = 0
    G_LineToX = 0
    L_x2 = int(mapping(constrain(-1*gyro, -35, 35), 0, 13, L_x1, 251))
    L_m = float(get_m(L_x, L_x2, 360, 0))
    #cv2.line(img, (L_x, L_y), (L_x2 , L_y1), (0, 0, 255), 2)
    R_x2 = int(mapping(constrain(-1*gyro, -35, 35), 0, 13, R_x1, 0))
    R_m = float(get_m(R_x, R_x2, 360, 0))
    #cv2.line(img, (R_x, R_y), (R_x2, R_y1), (0, 255, 0),2)
    #cv2.line(img, (240, 360), (int(mapping(gyro, 0, 20, 240, 320)), 180), (0, 255, 0), 4)
    cv2.circle(img, (green_x, green_y), 5, (200,255,200), -1)
    cv2.circle(img, (red_x, red_y), 5, (200,200,255), -1)
    if red_y > green_y:
        cv2.line(img, (0, red_y), (480, red_y), (0, 0, 255), 1)
        R_LineToX = int((-L_y + red_y + L_m * L_x)/L_m)
        cv2.circle(img, (R_LineToX, red_y), 5, (200,200,255), -1)
    if green_y > red_y:
        cv2.line(img, (0, green_y), (480, green_y), (0, 255, 0), 1)
        G_LineToX = int((-R_y + green_y + R_m * R_x)/R_m)
        cv2.circle(img, (G_LineToX, green_y), 5, (200,255,200), -1)
        
    return R_LineToX, G_LineToX

#--------------------------------------------------------
kp = 0.3 #P值
kd = 200 #D值
G_last_error = 0
R_last_error = 0
logic = 0
speed = 0
G_error = 0
R_error = 0
angle = 0
first_round = False
#--------------------------------------------------------
def car_control(img, red_x, red_y, red_area, green_x, green_y,
                green_area, red_num, green_num, R_wallX, G_wallX, gyro):
    
    global first_round, G_last_error, R_last_error, G_error, R_error, logic, Key, speed, angle
    if mode == False:
        if green_y > red_y and green_y < 330 and green_x > mapping(gyro, 20, 100, 0, 240) and green_x < mapping(gyro, -100, -10, 240, 480): #偵測到離機器最近的綠色積木的時候
            if green_y > constrain(mapping(green_x, 0, 220, 210, 230), 200, 220) and green_y < 250 and (abs(gyro) < 15 or logic == 1): #機器距離積木近且陀螺儀是正的時候
                logic = 1
                G_error = ((green_x - G_wallX) * kp) + (G_error - G_last_error) * kd
                Motor.Servo(constrain(G_error, -38, 38))
            elif green_y >= 250: #陀螺儀雖然沒有正，但是快撞到積木的時候
                logic = 1
                G_error = ((green_x - G_wallX) * kp) + (G_error - G_last_error) * kd
                Motor.Servo(constrain(G_error, -38, 38))
            elif green_y < 270 and gyro > 50 and gyro < 80: # 陀螺儀角度與積木目標差距太大的時候
                if Line_num == 0:
                    gyro_er = gyro_convert(0)
                else:
                    if car_angle:
                        gyro_er = gyro_convert((90*(((Line_num%2)+(Line_num//2)) - 1 ))%360)
                    else:
                        gyro_er = gyro_convert(-1*((90*(((Line_num%2)+(Line_num//2)) - 1))%360))
                logic = 0
                angle = gyro_er * 1.5
                Motor.Servo(constrain(angle, -38, 38))
            else: #看到綠色積木但沒還到達指定距離的時候
                angle = gyro * 1.5
                Motor.Servo(constrain(angle, -38, 38))
                logic = 0
        elif red_y > green_y and red_y < 360 and red_x > mapping(gyro, 20, 100, 0, 240) and red_x < mapping(gyro, -100, -20, 240, 480): #偵測到離機器最近的紅色積木的時候
            if red_y > 215 and red_y < 240 and (abs(gyro) < 25 or logic == 1): #機器距離積木近且陀螺儀是正的時候
                logic = 1
                R_error = ((red_x - R_wallX) * kp) + (R_error - R_last_error) * kd
                Motor.Servo(constrain(R_error, -38, 38))
            elif red_y >= 240: #陀螺儀雖然沒有正，但是快撞到積木的時候
                logic = 1
                R_error = ((red_x - R_wallX) * kp) + (R_error - R_last_error) * (kd*1.3)
                Motor.Servo(constrain(R_error, -38, 38))
            elif red_y < 300 and gyro < -50 and gyro > -110: # 陀螺儀角度與積木目標差距太大的時候
                if Line_num == 0:
                    gyro_er = gyro_convert(0)
                else:
                    if car_angle:
                        gyro_er = gyro_convert((90*(((Line_num%2)+(Line_num//2)) - 1 ))%360)
                    else:
                        gyro_er = gyro_convert(-1*((90*(((Line_num%2)+(Line_num//2)) - 1))%360))
                logic = 0
                angle = gyro_er * 1.5
                Motor.Servo(constrain(angle, -38, 38))
            else: # 看到紅色積木但還沒到達指定距離的時候
                logic = 0
                angle = gyro * 1.5
                Motor.Servo(constrain(angle, -38, 38))
        else: #沒有看到積木的時候
            logic = 0
            angle = gyro * 1.5
            Motor.Servo(constrain(angle, -35, 35))
    else:
        if Key == ord('i'):
            speed = speed + 70
            if speed > 70: speed = 70
        elif Key == ord('k'):
            speed = speed - 70
            if speed < -70: speed = -70
        Motor.DC(speed)
        if Key == ord('j'):
            angle = angle - 35
            if angle < -35: angle = -35
        elif Key == ord('l'):
            angle = angle + 35
            if angle > 35: angle = 35
            
        Motor.Servo(angle)
    G_last_error = G_error
    R_last_error = R_error
    
    if Start: #當matrix mini 按下按鈕後(開始運行後)
        if first_round == False:
            Motor.DC(80)
            time.sleep(0.1)
            first_round = True
        else:
            Motor.DC(constrain(mapping(abs(angle), 0, 20, 57, 53), 57, 53))
    elif mode == False:
        Motor.DC(0)
        
#--------------------------------------------------------
  #Motor.DC(0) 控制馬達前進後退
  #Motor.Servo(angle) 控制伺服馬達的角度
  #mapping(x, 300, 500, -200, 0)
  #constrain(x, -200, 0)
#--------------------------------------------------------



#--------------------------------------------------------
color_threshold = 15 #光感判斷的判斷數值
blue_orange_filter = 10
#--------------------------------------------------------
def Line_Detect():
    global Run, Line_num, car_angle, color_threshold, blue_orange_filter
    Line_num = 0
    last_time = 0
    sensor_lower = color_threshold
    print("[Color Sensor]: Color Sensor Start")
    try:
        while Run:
            #=========
            
            color = 100
            while color > color_threshold-1 and Run:
                color = tcs34725.readluminance()['c']
                time.sleep(0.001)
                
            #=======
            color = 0
            #while True:
            while color < color_threshold+1 and Run:
                color = tcs34725.readluminance()['c']
                if color < sensor_lower:
                    sensor_lower = color
                time.sleep(0.001)
            
            if sensor_lower > blue_orange_filter:
                print("[Drive_Mode]: Clockwise")
                car_angle = True
            else:
                print("[Drive_Mode]: Unclockwise")
                car_angle = False
                
            Line_num = Line_num+1
            print("[Color_Sensor]: Line_Count: {}".format(Line_num))
            while Line_num < 24 and Run:   #圈數設定
                color = tcs34725.readluminance()['c']
                time.sleep(0.001)
                while color < color_threshold+1 and Run:
                    last_time = time.time()
                    color = tcs34725.readluminance()['c']
                    time.sleep(0.001)
                while color > color_threshold-1 and Run:
                    color = tcs34725.readluminance()['c']
                    time.sleep(0.001)
                error_time = time.time()
                if Line_num%2 == 0 and error_time - last_time > 2.2:
                    Line_num = Line_num+1
                    print("[Color_Sensor]: Line_Count: {}".format(Line_num))
                elif Line_num%2 == 0 and error_time - last_time < 2.5:
                    print("[Color_Sensor]: no enough time")
                elif Line_num%2:
                    Line_num = Line_num+1
                    print("[Color_Sensor]: Line_Count: {}".format(Line_num))
                
            Run = False
        print("[Color_Sensor]: Sensor Stop")
    except KeyboardInterrupt:
        Run = False
        print("[Color_Sensor]: Sensor Stop")
                
def camera():
    global image, Start, Run, End
    print("[Camera]: Camera Start")
    try:
        while End:
            start = time.time()
            success, image = imcap.read()
            end = time.time()
            loop_speed = 1 / Hz 
            if end - start < loop_speed: # 控制鏡頭的刷新率，避免刷新率太高導致鏡頭顏色失正
                time.sleep(loop_speed-(end-start))
            end = time.time()
            FPS = str(1/(end - start))
        imcap.release()
        print("[Camera]: Camera Close")
    except KeyboardInterrupt: #如果按了Ctrl + C，就讓鏡頭關閉，避免下次無法正確讀取鏡頭的問題發生
        Run = False
        GPIO.output(20, False)
        imcap.release()
        print("[Camera]: Camera Close")
    
#------------------------------------------------------------------
Key = 0
L_x = 20
L_y = 360
R_x = 430
R_y = 360

L_x1 = 367
L_y1 = 0
R_x1 = 95
R_y1 = 0
mode = False
print("[Main]: Mode Selected")
car_angle = True # true 順時針 / false 逆時針
button_realease = True
imcap = cv2.VideoCapture(0)
imcap.set(cv2.CAP_PROP_BUFFERSIZE,1)
imcap.set(cv2.CAP_PROP_FPS, 40)
imcap.set(cv2.CAP_PROP_BRIGHTNESS, 60)
imcap.set(cv2.CAP_PROP_CONTRAST, 75)
imcap.set(3, 480) # set width as 640
imcap.set(4, 360) # set height as 480
print("[Main]: Camera Set Done")
bno.begin()
time.sleep(1)
bno.setExternalCrystalUse(True)
print("[Main]: Gyro Set Done")
Hz = 38 # 控制鏡頭的HZ數
t = threading.Thread(target = Line_Detect)
print("[Main]: Thread Color Sensor Part")
Cam = threading.Thread(target = camera, daemon=True)
print("[Main]: Thread Camera Part")
success, image = imcap.read()
Run = True
End = True
Start = False
t.start()
time.sleep(0.05)
Cam.start()
GPIO.output(20, True) #程式前置已經設定完成，輸出腳位20告知matrix mini程式已經開啟
print("[Main]: Matrix Mini Sented")
#------------------------------------------------------------------

while Run:

    start = time.time()
    
    roi_image = image.copy()
    roi_image[0:190, 0:480] = [0,0,0]#遮罩鏡頭畫面的範圍
    
    (Color_image, red_x, red_y, green_x, green_y, red_area,
     green_area, red_num, green_num) = Color_Detect(roi_image)
    
    if Line_num == 0:
        gyro = gyro_convert(0)
    else:
        if car_angle:
            gyro = gyro_convert((90*((Line_num%2)+(Line_num//2)))%360)
        else:
            gyro = gyro_convert(-1*((90*((Line_num%2)+(Line_num//2)))%360))    
    red_lineX, green_lineX= Draw_Line(roi_image, red_x, red_y, green_x,
                                       green_y, gyro)    
    
    car_control(roi_image, red_x, red_y, red_area, green_x, green_y, green_area,
                red_num, green_num, red_lineX, green_lineX, gyro)
    
    Key = cv2.waitKey(10)
    button = GPIO.input(21)
    
    if Key == ord('q'): #按下Q鍵停止程式
        Start = False
        End = False
        break
    if Key == ord('w'): #按下W鍵或按下matrix mini的按鈕汽車開始運行
        print("[Car]: Car Start Drive")
        Start = True
    if button:
        if first_round and button_realease:
            print("[Car]: Car Stop Drive")
            first_round = False
            Start = False
            button_realease = False
        elif button_realease:
            print("[Car]: Car Start Drive")
            Start = True
            button_realease = False
    else:
        if not button_realease:
            print("buttonRealease")
        button_realease = True
    if Key == ord('s'): #按下S鍵讓汽車暫停運行
        print("[Car]: Car Stop Drive")
        Start = False
    if Key == ord('m'):# 切換自動駕駛/遙控模式
        Start = False
        if mode:
            mode = False
            print("[Mode]: Auto Drive Mode")
        else:
            mode = True
            print("[Mode]: Manual Drive Mode")

    end = time.time()
    FPS = str(1/(end - start))
    cv2.putText(roi_image, "FPS:"+FPS, (0, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255,255,255), 2, cv2.LINE_AA) # 顯示FPS
    cv2.imshow('face_detect', roi_image)
    
s = time.time()
while time.time() - s < 2.1:#Run == False:
    roi_image = image.copy()
    roi_image[0:190, 0:480] = [0,0,0]#遮罩鏡頭畫面的範圍
    
    (Color_image, red_x, red_y, green_x, green_y, red_area,
     green_area, red_num, green_num) = Color_Detect(roi_image)
    
    if car_angle:
        gyro = gyro_convert((90*((Line_num%2)+(Line_num//2)))%360)
    else:
        gyro = gyro_convert(-1*((90*((Line_num%2)+(Line_num//2)))%360))
    
    red_lineX, green_lineX= Draw_Line(roi_image, red_x, red_y, green_x,
                                       green_y, gyro)
    
    car_control(roi_image, red_x, red_y, red_area, green_x, green_y, green_area,
                red_num, green_num, red_lineX, green_lineX, gyro)
    

Run = False
End = False
print("[Main]: Car Stop")
Motor.Servo(0)
Motor.DC(0)
time.sleep(0.1)
imcap.release()
Motor.ServoStop()
cv2.destroyAllWindows()
print("[Main]: Program Stop")#程式停止，關閉程式
GPIO.output(20, False)
