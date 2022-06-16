# Future_Engineer_Car_Diary
This is WRO2022 Future Engineers comtetion's Note. 

# Introduction

 * Hardware
  The car uses [Onshape](https://www.onshape.com/en/) design car's shape, then use Laser cutting machine cut the planks, planks with hexagonal column doing compartment, put hardware in compartment. the drawings are in `models`
  
  Hardware have:
  
    1. Wheel(Front):         Lego 62.4x20 wheel  x2
    2. Wheel(Rear):          Lego 43.2x14 wheel  x2
    4. controller:           Raspberry Pi 4B 8GB
    5. transmission:         1:34 Motor with plastic differential
    6. Steering mechanism:   Servo motor with LEGO Liftarm Thick(1*11), PCA9685
    7. Camera:               OV5647 Raspberry Pi Camera
  

 * Software

  The car uses [Donkey Car](https://www.donkeycar.com/) doing Self Driving Car Platform. [Donkey Car](https://www.donkeycar.com/)  is a high level self driving library written in [Python](https://www.python.org/). It is an Open Source Hardware design that makes it easy for you to build your own car. And use Raspberry Pi control the car to start driveing. The code are in `src` Folder.
  
# Diary

  Date: 2022/06/09(Thu)  06:13 p.m. 
  
  Member: LU-CHENG YU
  
  Content: 
    Today, we found a problem again. the motor's fixed mount are broke, we need to find a better solution. we redesign car's chassis, modified the design many times.   finally, the chassis was done, it can very strong to fixed the motor, and width reduced by 13%, we think this is very proud moment.
    
  紀錄時間: 2022/06/09(星期四)  06:13 p.m. 
  
  活動成員: 呂承諭
  
  工作內容: 
    今天，我們又發現了一個問題。電機的固定架壞了，我們需要尋找一個更好的解決方案。我們重新設計了汽車的底盤，多次修改設計。終於，底盤做好了，可以很結實的固定電機，寬度減少了13%，我們覺   得這是一個非常自豪的時刻。

  ----------
  Date: 2022/06/08(Wed)  02:53 p.m. 
  
  Member: LU-CHENG YU
  
  Content: 
    Today, we found a problem. the car's steering mechanism is unstable, we found it was caused by the voltage problem of the raspberry pi, so we use PCA9685 Control     Board to connect Servo motor and raspberry pi. The PCA9685 does not provide a 3.3v voltage like the raspberry pi, but independently supplies a 5V voltage to ensure     that the servo motor can work normally and stably.
    
  紀錄時間: 2022/06/08(星期三)  02:53 p.m. 
  
  活動成員: 呂承諭
  
  工作內容: 
      今天，我們發現了一個問題。汽車的轉向機構不穩定，我們發現是樹莓派的電壓問題，所以我們使用PCA9685控制板連接伺服電機和樹莓派。 PCA9685不像樹莓派那樣提供3.3v電壓，而是獨立提供5V電   壓，保證伺服電機正常穩定工作。
    
  ----------
  Date: 2022/06/07(Tue)  03:50 p.m. 
  
  Member: LU-CHENG YU
  
  Content: 
    Today, the car can drive with game controller. Then we just need Adjustment some value, train a model, the car should be drive self.
    
  紀錄時間: 2022/06/07(星期二)  03:50 p.m. 
  
  活動成員: 呂承諭
  
  工作內容: 
      今天車子已經可以透過遊戲搖桿控制了，接下來需要調整一些數值，然後開始訓練駕駛模型，之後汽車就可以自動駕駛了。
    
  ----------
  Date: 2022/05/30(Mon)  02:25 p.m. 
  
  Member: LU-CHENG YU
  
  Content: 
    Today, we set the hardware done, so now we're going setting software, we choose Donkey Car, because it is opensource code, it have detailed tutorial and it matched   for our needs.
    
  紀錄時間: 2022/05/30(星期一)  02:25 p.m. 
  
  活動成員: 呂承諭
  
  工作內容: 
      今天我們把硬體都裝好了，接下來要準備設定軟體，我們選擇了Donkey Car，因為它是一個開源的軟體，有詳細的教學，而且也剛好符合我們的需求。
      ![IMG_5362](https://user-images.githubusercontent.com/74124750/173970839-211c1968-0a9b-4ef1-9981-bc019f3c5eaf.jpg)
      ![IMG_5361](https://user-images.githubusercontent.com/74124750/173970905-e8be7777-8c8b-443b-864f-5a46e639d602.jpg)

  ----------
  Date: 2022/05/28(Sat)  04:00 p.m. 
  
  Member: LU-CHENG YU
  
  Content: 
    Today, we design the car's shape done. now we're going put the hardware in, and setting software, let car drive, the car will be done. 
    
  紀錄時間: 2022/05/30(星期六)  02:25 p.m. 
  
  活動成員: 呂承諭
  
  工作內容: 
    今天我們把我們設計好了車子的外型，接下來我們要選擇硬體，然後裝到車上，以及選擇、設定軟體，讓車子動起來，車子就大致上完成了。

  
     

