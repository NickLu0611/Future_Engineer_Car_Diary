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

  The car uses [Donkey Car](https://www.donkeycar.com/) doing Self Driving Car Platform. [Donkey Car](https://www.donkeycar.com/)  is a high level self driving library written in [Python](https://www.python.org/). It is an Open Source Hardware design that makes it easy for you to build your own car. And use Raspberry Pi control the car to start driving. The code are in `src` Folder.
  
# Diary

record time : 2022/06/22 (Wed) 1:52 p.m.

member: LU-CHENG YU , HU-YUN RUI

Content: 
    Today we found out that the official website of donkey car has been updated. We used Linux system before, but now Windows system is added.Perhaps for us, the           windows system can be more familiar and easy to use.

日期：2022/06/22（星期三）下午 1:52

成員: 呂承諭、胡允瑞

內容：
    今天我們發現 donkey car 的官網更新了，之前我們使用的是 Linux 系統，而現在新增了 Windows 系統，我們對其進行嘗試，或許對於我們來說 windows 可以更熟悉、上手。
![R](https://user-images.githubusercontent.com/74124750/174947269-32b844bd-e5ea-4833-af6e-6c1b487fbae6.jpg)

-------
Date: 2022/06/21 (Tue) 8:11 p.m.

member: LU-CHENG YU , HU-YUN RUI

Content: 






-------
Date: 2022/06/20 (Mon) 5:19 p.m.

member: LU-CHENG YU , HU-YUN RUI

Content: 






-------

Date: 2022/06/18 (Sat) 4:28 p.m.

member: LU-CHENG YU , HU-YUN RUI

Content: 






-------
Date: 2022/06/17 (Fri) 3:57 p.m.

member: LU-CHENG YU , HU-YUN RUI

Content: 






-------
Date: 2022/06/16 (Thu) 7:41 p.m.

member: LU-CHENG YU, HU-YUN RUI

Content: 


-------
Date: 2022/06/15 (Wed) 3:11 p.m.

member: LU-CHENG YU

Content: 



--------
Date: 2022/06/14 (Tue) 2:29 p.m

member: LU-CHENG YU

Content: 





--------
Date: 2022/06/12 (Sun) 6:37 p.m.

member: LU-CHENG YU

Content: 



--------
Date: 2022/06/11 (Sat) 4:18 p.m.

member: LU-CHENG YU

Content: 





 --------
  Date: 2022/06/09(Thu)  06:13 p.m. 
  
  Member: LU-CHENG YU
  
  Content: 
    Today, we found a problem again. the motor's fixed mount are broke, we need to find a better solution. we redesign car's chassis, modified the design many times.   finally, the chassis was done, it can very strong to fixed the motor, and chassis width reduced by 13%, we think this is very proud moment.

  紀錄時間: 2022/06/09(星期四)  06:13 p.m. 
  
  活動成員: 呂承諭
  
  工作內容: 
    今天，我們又發現了一個問題。電機的固定架壞了，我們需要尋找一個更好的解決方案。我們重新設計了汽車的底盤，多次修改設計。終於，底盤做好了，可以很結實的固定電機，底盤的寬度也減少了     13%，我們覺得這是一個非常自豪的時刻。
  ![IMG-5388 (2)](https://user-images.githubusercontent.com/74124750/173972789-331f9513-972e-4535-8c33-0f8a04b3ebf2.jpg)
  ![IMG-5387 (2)](https://user-images.githubusercontent.com/74124750/173972801-418694fb-034c-41c8-a7c3-cdd9fcb9ac72.jpg)
  ![IMG-5390 (2)](https://user-images.githubusercontent.com/74124750/173972809-647a51e6-f07b-4aae-87a1-40be9271bbcd.jpg)


  ----------
  Date: 2022/06/08(Wed)  02:53 p.m. 
  
  Member: LU-CHENG YU
  
  Content: 
    Today, we found a problem. the car's steering mechanism is unstable, we found it was caused by the voltage problem of the raspberry pi, so we use PCA9685 Control     Board to connect Servo motor and raspberry pi. The PCA9685 does not provide a 3.3v voltage like the raspberry pi, but independently supplies a 5V voltage to ensure     that the servo motor can work normally and stably.
    
  紀錄時間: 2022/06/08(星期三)  02:53 p.m. 
  
  活動成員: 呂承諭
  
  工作內容: 
      今天，我們發現了一個問題。汽車的轉向機構不穩定，我們發現是樹莓派的電壓問題，所以我們使用PCA9685控制板連接伺服電機和樹莓派。 PCA9685不像樹莓派那樣提供3.3v電壓，而是獨立提供5V電   壓，保證伺服電機正常穩定工作。
     ![IMG-5424](https://user-images.githubusercontent.com/74124750/173972904-891cb435-5bd0-48fd-9ce9-ac12c7344823.jpg)
 ![IMG-5425](https://user-images.githubusercontent.com/74124750/173972927-e116a1d2-66fd-4436-b1f1-8f15775d2779.jpg)

    
  ----------
  Date: 2022/06/07(Tue)  03:50 p.m. 
  
  Member: LU-CHENG YU
  
  Content: 
    Today, the car can drive with game controller. Then we just need Adjustment some value, train a model, the car should be drive self.
    
  紀錄時間: 2022/06/07(星期二)  03:50 p.m. 
  
  活動成員: 呂承諭
  
  工作內容: 
      今天車子已經可以透過遊戲搖桿控制了，接下來需要調整一些數值，然後開始訓練駕駛模型，之後汽車就可以自動駕駛了。
      ![IMG-5364](https://user-images.githubusercontent.com/74124750/173973037-9f2f6784-0326-44f7-a8cc-f0c6ddc3248b.jpg)

    
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
    今天我們把我們設計好了車子的外型，接下來我們要選擇硬體，然後裝到車上，以及選擇、設定軟體，讓車子動起來，車子就大致上完成了
     
