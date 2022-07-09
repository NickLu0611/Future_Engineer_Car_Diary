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
Date: 2022/07/02 (Sat)6:10 p.m.

Member: LU-CHENG YU ,HU-YUN RUI

Content:
Today, we cut the car we designed yesterday with a laser cutter, and assemble the car according to the design drawing. After testing the accelerator, steering and AI automatic driving, we have completed the final appearance of the car.

日期：2022/07/02（星期六）下午 6:10

成員: 呂承諭、胡允瑞

內容：
  我們今天將昨天設計好的汽車，利用雷射切割機切割，並依照設計圖組裝車子，經測試油門、轉向以及AI自動駕駛沒問題後，完成了最終車子的模樣。
 
![S__7053319](https://user-images.githubusercontent.com/107915065/176983710-cd8c33e8-44e5-4ecb-ac09-79fb812805f9.jpg)
![S__7053321](https://user-images.githubusercontent.com/107915065/176983713-ccdfb8ac-6895-4294-bccf-6185cd3e4438.jpg)

![S__7053317](https://user-images.githubusercontent.com/107915065/176983433-68a16c13-5675-4098-87e5-b3bc1d5f1e50.jpg)
![S__7053315](https://user-images.githubusercontent.com/107915065/176983434-e8a8a640-afcb-4308-97b6-89ac4eb202c4.jpg)

-------
Date: 2022/06/28 (Tue) 5:21 p.m.

Member: LU-CHENG YU , HU-YUN RUI

Content: Today, we found that the redesigned vehicle a few days ago has asymmetry, which causes the vehicle to skew to the right when driving, so we changed the design drawing under the original architecture, changed the steering structure of the vehicle, and used Onshape's 3D simulation The function simulates the hardware and structure of the vehicle, so as to ensure that the vehicle design is feasible, and at the same time, it can better understand the poor design and make changes.

日期：2022/06/28（星期二）下午 5:21

成員: 呂承諭、胡允瑞

內容：
  今天我們發現前幾天重新設計的車輛有左右不對稱、導致車輛在駕駛時向右偏斜的問題，於是我們在原本架構下更改設計圖，並更改了車輛的轉向結構，並利用Onshape的3D模擬功能模擬車輛的硬體、結構，這麼一來可以確保車輛設計可行的同時，能夠更加清楚設計不良的地方，並進行更改。
  
![S__6782985](https://user-images.githubusercontent.com/107915065/176084864-9d2e627d-b3ea-483b-8955-026737042d58.jpg)
![S__6782989](https://user-images.githubusercontent.com/107915065/176084871-c184ea50-45ca-4aae-8420-8aa876a4881c.jpg)
-------

Date: 2022/06/27 (Mon) 4:08 p.m.

Member: LU-CHENG YU , HU-YUN RUI

Content: Today we found that the car will make a loud gear noise when driving. After asking the coach and testing, we found that the motor output gear and the differential gear are too densely engaged, so there is no gap between the gears, which causes the car to drive slowly and emit noise. Excessive noise, so we changed the fixed end of the motor to a distance-adjustable motor frame, which can directly adjust the gap between the motor and the differential.

日期：2022/06/27（星期一）下午 4:08

成員: 呂承諭、胡允瑞

內容：
  今天我們發現車子在駕駛的時候會發出很大聲的齒輪噪音，經過詢問教練以及測試發現馬達輸出齒輪與差速器的齒輪咬合過於密集，因此齒輪間因為沒有間隙而導致汽車駕駛速度慢和發出過大的噪音，因此我們將馬達固定端更改成可調距離式的馬達架，可以直接調整馬達與差速器的間隙
  
![S__6782984](https://user-images.githubusercontent.com/107915065/176074988-79a52a09-821f-4119-8751-fae4e5c00349.jpg)
![S__6782981](https://user-images.githubusercontent.com/107915065/176075008-d9f2c984-59aa-4350-90db-09374a0350fb.jpg)

-------
Date: 2022/06/24 (Fri) 3:18 p.m.

Member: LU-CHENG YU , HU-YUN RUI

Content: Today we redesigned the vehicle. Since the old vehicle structure is divided into three layers, and the height of each layer is about 4cm~5cm, the center of gravity of the vehicle is offset when turning at high speed, which will cause the vehicle to roll over during driving. Therefore, we let the car's The center of gravity becomes lower, and at the same time, the Raspberry Pi controller is changed from vertical to horizontal placement, which makes it easier to extract the SD card, and also allows more space to put down hardware components, reducing space waste. thereby reducing the body size.

日期：2022/06/24（星期五）下午 3:18

成員: 呂承諭、胡允瑞

內容：
  今天我們又重新設計了車輛，由於舊型車輛結構分成三層，且每一層的高度都大約4cm~5cm，在高速轉彎時車輛的重心偏移導致車輛行駛過程中會翻車，因此我們讓汽車的重心變得較低，同時也讓樹莓派控制器從縱向放置改為橫向放置，這麼一來能夠更方便的抽取SD卡，也能多出更多的空間放下硬體元件，減少空間浪費，進而縮小車體。
  
![IMG_5463](https://user-images.githubusercontent.com/107915065/175811033-9726ecef-ccfa-4a1e-8eb0-78ada401539a.JPG)
![IMG_5471](https://user-images.githubusercontent.com/107915065/175811037-695fe116-4e13-4e53-9b53-aa1ab75ed8d4.JPG)
![IMG_5444](https://user-images.githubusercontent.com/107915065/175439679-9b7dde9c-8680-42eb-b8e0-02b59bcc860e.JPG)

-------
Date: 2022/06/23 (Thu) 6:53 p.m.

Member: LU-CHENG YU , HU-YUN RUI

Content: 
    We have added an OLED to the model today.We connected it and installed the OLED display service, and the OLED can display the current IP address, battery, voltage and other information.In this way, when we need these data in the future, we don't have to write additional program instructions to find it, it can saves our time.

日期：2022/06/23（星期四）下午 6:53

成員: 呂承諭、胡允瑞

內容：
  我們今天在機型上增加了一個 OLED，將其接上並下命令安装OLED的顯示功能後，OLED便可以顯示當前的IP地址、电池和电壓等信息，如此一來，我們未來需要這些數據的時候，不必在額外下指令尋找，使我們節省時間。

![IMG_5440](https://user-images.githubusercontent.com/107915065/175439789-2ec1e98b-d52e-4027-a285-dc774abfe430.JPG)
-------

Date : 2022/06/22 (Wed) 1:52 p.m.

Member: LU-CHENG YU , HU-YUN RUI

Content: 
    Today we found out that the official website of donkey car has been updated. We used Linux system before, but now Windows system is added.Perhaps for us, the windows system can be more familiar and easy to use.
   
日期：2022/06/22（星期三）下午 1:52

成員: 呂承諭、胡允瑞

內容：
    今天我們發現 donkey car 的官網更新了，之前我們使用的是 Linux 系統，而現在新增了 Windows 系統，我們開始對其進行嘗試，或許對於我們來說 windows 會更熟悉，也更好上手。
![1](https://user-images.githubusercontent.com/107915065/174947403-794c4749-618e-499f-a587-691f4d45832a.png)

-------
Date: 2022/06/21 (Tue) 8:11 p.m.

Member: LU-CHENG YU , HU-YUN RUI

Content: 

日期：2022/06/21（週二）下午 8:11

成員：呂承諭、胡允瑞

內容：






-------
Date: 2022/06/20 (Mon) 5:19 p.m.

Member: LU-CHENG YU , HU-YUN RUI

Content: 

日期：2022/06/20 （週一）下午 5:19

成員：呂承諭、胡允瑞

內容：




-------

Date: 2022/06/18 (Sat) 4:28 p.m.

Member: LU-CHENG YU , HU-YUN RUI

Content: 


日期：2022/06/18（週六）下午 4:28

成員：呂承諭、胡允瑞

內容：



-------
Date: 2022/06/17 (Fri) 3:57 p.m.

Member: LU-CHENG YU , HU-YUN RUI

Content: 


日期：2022/06/17（週五）下午 3:57

成員：呂承諭、胡允瑞

內容：



-------
Date: 2022/06/16 (Thu) 7:41 p.m.

Member: LU-CHENG YU, HU-YUN RUI

Content: 


日期：2022/06/16（週四）下午 7:41

成員：呂承諭、胡允瑞

內容：

--------
Date: 2022/06/12 (Sun) 6:37 p.m.

Member: LU-CHENG YU

Content: 

日期：2022/06/12（週日）下午 6:37 

成員：呂承諭

內容：

--------
Date: 2022/06/11 (Sat) 4:18 p.m.

Member: LU-CHENG YU

Content: 



日期：2022/06/11（週六）下午 4:18

成員:呂承諭

內容：

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
  Date: 2022/05/28(Sat)  02:25 p.m. 
  
  Member: LU-CHENG YU
  
  Content: 
    Today, we design the car's shape done. now we're going put the hardware in, and setting software, let car drive, the car will be done. 
    
  紀錄時間: 2022/05/28(星期六)  02:25 p.m. 
  
  活動成員: 呂承諭
  
  工作內容: 
    今天我們設計好了車子的外型，接下來我們要選擇硬體，然後裝到車上，以及選擇、設定軟體，讓車子動起來，車子就大致上完成了
     
