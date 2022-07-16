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
Date: 2022/07/16 (Sat) 7 p.m.

Member:LU-CHENG YU ,HU-YUN RUI

Content: 



日期：2022/07/15（星期Sat）下午 7:00

成員:呂承諭、胡允瑞

工作內容：
-------
Date: 2022/07/15 (Fri) 2 p.m.

Member:LU-CHENG YU ,HU-YUN RUI

Content:
    Recently, we have been using different venues for simulation training one by one, and on a stable basis, we have tried to increase the speed as much as possible.
日期：2022/07/15（星期五）下午 2:00

成員:呂承諭、胡允瑞

工作內容：

  近期，我們都在用不同的場地一個一個進行模擬訓練，在穩定的基礎下，盡可能地提升速度。
![292426670_721458525608140_8170895943032731616_n](https://user-images.githubusercontent.com/107915065/179328676-5a601962-8304-4549-980c-77439c8e09ba.jpg)
![292446841_276317078044899_1677936645027783075_n](https://user-images.githubusercontent.com/107915065/179328698-d3dd5201-cfe4-43b3-b603-f22893578bd2.jpg)

------

Date: 2022/07/13 (Wed)5:17 p.m.

Member:LU-CHENG YU ,HU-YUN RUI

Content: 

    During training, we always encounter a collision with the wall, which also causes the front part of the car body to be easily smashed. In order to improve the problem of the car being damaged, we chose foam and cut it out with a laser cutter. Match the shape that our body needs, because we can't find the power of cutting foam on the Internet, so we have to try again and again, and finally find the correct and successful cutting!
    
日期：2022/07/13（星期三）下午 5:17

成員:呂承諭、胡允瑞

工作內容：

  在訓練時，總是會遇到撞牆的時候，也導致車體前方的部分，很容易就被撞爛了，為了改善車子被破壞的問題，我們選擇了泡棉，用雷射切割機切出搭配我們機體所需要的形狀，因為在網上我們都找不到關於切割泡棉的功率，所以只好一次一次的嘗試，最後終於找到正確的成功切割!
![290919207_1275377122868448_247899751621901739_n](https://user-images.githubusercontent.com/107915065/178660379-4c182cda-e9be-409e-b5f5-4d4be84431a4.jpg)
![292425380_749280279729904_804669233689923045_n](https://user-images.githubusercontent.com/107915065/178660399-a7005807-f52c-45ab-bcdf-291254f26ba7.jpg)
![291783913_908370227223952_6910427142751155816_n](https://user-images.githubusercontent.com/107915065/178660412-4f9cc762-78b5-4b16-abbf-1d76c5f576b9.jpg)
![292285327_1369770923515741_1475278518503013676_n](https://user-images.githubusercontent.com/107915065/178660428-e2679098-0f72-48ca-9fcf-7f5fc01b3252.jpg)
![image](https://user-images.githubusercontent.com/107915065/178672578-dcccc685-37bf-4c56-b287-e0474aef5d5e.png)
![292980452_1496467854143506_1979140512332814259_n](https://user-images.githubusercontent.com/107915065/179328692-c9fa4f67-53ea-4bb8-bb84-290ea2a0261d.jpg)


-------
Date: 2022/07/10 (Mon)6p.m.

Member:LU-CHENG YU ,HU-YUN RUI

Content: We started to change different field tasks to test, in continuous training, to make it as stable as possible, and the situation we encountered was when turning, there was still a delay problem.

日期：2022/07/10（星期一）下午 6:00

成員:呂承諭、胡允瑞

工作內容：

    我們開始變換不同的場地任務進行測試，在不斷的訓練中，盡可能地使其穩定，而遇到的情況則是在轉彎時，仍會有延遲的問題。

![291701755_808423143480659_4410612983174338014_n](https://user-images.githubusercontent.com/107915065/178636395-28c018a6-f0e5-4f26-b3e9-2c2399ed2601.jpg)

-------
Date: 2022/07/06 (Wed)4:19 p.m.

Member:HU-YUN RUI

Content:  Today we found the problem. If the comparison and selection of Cuda and cuDNN on versions are wrong, the results presented will also be problematic, so we found the corresponding correct version, and related the previously downloaded version. The file was removed, and the steps of downloading miniconda were restarted. Finally, the GPU was successfully used instead of the CPU for environmental training. The speed can be significantly improved.


日期：2022/07/06（星期四）下午 4:19

成員:胡允瑞

工作內容：

    今天我們發現了問題所在，Cuda 和 cuDNN 如果在版本上的對照及選擇是錯誤的，那呈現出來的結果也會是有問題的，所以我們找到了相對應的正確版本，並將之前下載的相關檔案移除，從下載miniconda的步驟從頭來過，終於成功使用 GPU 代替 CPU 進行環境訓練，在速度上便可以明顯感覺提升。

![擷取](https://user-images.githubusercontent.com/107915065/178141468-6875d742-733a-445a-8483-1719e7ac97e7.PNG)
![image](https://user-images.githubusercontent.com/107915065/178394437-661a746a-c290-4cf8-a97a-0e2229103fa1.png)

-------
Date: 2022/07/06 (Wed)4:19 p.m.

Member:HU-YUN RUI

Content: Today, we downloaded and installed Cuda and configured cuDNN to achieve high performance GPU acceleration, but the test results were wrong after loading.

日期：2022/07/06（星期四）下午 4:19

成員:胡允瑞

工作內容：

    今天，我們下載和安裝了Cuda並配置cuDNN 來實現高性能 GPU 加速，但載入後的測試結果卻是有錯誤的。
![擷取1](https://user-images.githubusercontent.com/107915065/178140944-e84123df-35f4-4768-82f0-07c49dccfd74.PNG)
![image](https://user-images.githubusercontent.com/107915065/178141075-5d7dd9a7-65b8-40c1-9b5c-3101a5e6ac45.png)

--------
Date: 2022/07/04 (Mon)3:18 p.m.

Member:HU-YUN RUI

Content:  When we practice the training environment, it always takes a lot of time to wait, so we have been looking for a better alternative. We chose to use the Windows-Python3.7 system we studied before to extend the discussion, found a lot of information on the Internet, and start tounderstand conda more deeply.


日期：2022/07/04（星期一）下午 3:18

成員:胡允瑞

工作內容：

    我們在練習訓練環境時，因為總是需要花費大量時間等待，所以我們一直在找更好的代替方案，我們選擇用之前研究的Windows-Python3.7系統延伸探討，上網找了很多資料，並開始更深度的了解conda。
![擷取](https://user-images.githubusercontent.com/107915065/178139969-f525fb6c-480f-4cc0-bf23-e84dbdb2fca8.PNG)
![擷取](https://user-images.githubusercontent.com/107915065/178140175-5dc454ed-2118-4609-ad36-1c0a29cd98d4.PNG)

------

Date: 2022/07/02 (Sat)6:10 p.m.

Member: LU-CHENG YU ,HU-YUN RUI

Content:Today, we cut the car we designed yesterday with a laser cutter, and assemble the car according to the design drawing. After testing the accelerator, steering and AI automatic driving, we have completed the final appearance of the car.

日期：2022/07/02（星期六）下午 6:10

成員: 呂承諭、胡允瑞

工作內容：

  我們今天將昨天設計好的汽車，利用雷射切割機切割，並依照設計圖組裝車子，經測試油門、轉向以及AI自動駕駛沒問題後，完成了最終車子的模樣。
 
![S__7053319](https://user-images.githubusercontent.com/107915065/176983710-cd8c33e8-44e5-4ecb-ac09-79fb812805f9.jpg)
![S__7053321](https://user-images.githubusercontent.com/107915065/176983713-ccdfb8ac-6895-4294-bccf-6185cd3e4438.jpg)
![image](https://user-images.githubusercontent.com/107915065/178391074-b6a51db0-b286-4e87-b0dd-f2e461bc49ac.png)


-------
Date: 2022/06/28 (Tue) 5:21 p.m.

Member: LU-CHENG YU , HU-YUN RUI

Content: Today, we found that the redesigned vehicle a few days ago has asymmetry, which causes the vehicle to skew to the right when driving, so we changed the design drawing under the original architecture, changed the steering structure of the vehicle, and used Onshape's 3D simulation The function simulates the hardware and structure of the vehicle, so as to ensure that the vehicle design is feasible, and at the same time, it can better understand the poor design and make changes.

日期：2022/06/28（星期二）下午 5:21

成員: 呂承諭、胡允瑞

工作內容：

  今天我們發現前幾天重新設計的車輛有左右不對稱、導致車輛在駕駛時向右偏斜的問題，於是我們在原本架構下更改設計圖，並更改了車輛的轉向結構，並利用Onshape的3D模擬功能模擬車輛的硬體、結構，這麼一來可以確保車輛設計可行的同時，能夠更加清楚設計不良的地方，並進行更改。
  
![S__6782985](https://user-images.githubusercontent.com/107915065/176084864-9d2e627d-b3ea-483b-8955-026737042d58.jpg)
![S__6782989](https://user-images.githubusercontent.com/107915065/176084871-c184ea50-45ca-4aae-8420-8aa876a4881c.jpg)
-------

Date: 2022/06/27 (Mon) 4:08 p.m.

Member: LU-CHENG YU , HU-YUN RUI

Content:
    Today we found that the car will make a loud gear noise when driving. After asking the coach and testing, we found that the motor output gear and the differential gear are too densely engaged, so there is no gap between the gears, which causes the car to drive slowly and emit noise. Excessive noise, so we changed the fixed end of the motor to a distance-adjustable motor frame, which can directly adjust the gap between the motor and the differential.

日期：2022/06/27（星期一）下午 4:08

成員: 呂承諭、胡允瑞

工作內容：

  今天我們發現車子在駕駛的時候會發出很大聲的齒輪噪音，經過詢問教練以及測試發現馬達輸出齒輪與差速器的齒輪咬合過於密集，因此齒輪間因為沒有間隙而導致汽車駕駛速度慢和發出過大的噪音，因此我們將馬達固定端更改成可調距離式的馬達架，可以直接調整馬達與差速器的間隙
  
![S__6782984](https://user-images.githubusercontent.com/107915065/176074988-79a52a09-821f-4119-8751-fae4e5c00349.jpg)
![S__6782981](https://user-images.githubusercontent.com/107915065/176075008-d9f2c984-59aa-4350-90db-09374a0350fb.jpg)

-------
Date: 2022/06/24 (Fri) 3:18 p.m.

Member: LU-CHENG YU , HU-YUN RUI

Content: 

    Today we redesigned the vehicle. Since the old vehicle structure is divided into three layers, and the height of each layer is about 4cm~5cm, the center of gravity of the vehicle is offset when turning at high speed, which will cause the vehicle to roll over during driving. Therefore, we let the car's The center of gravity becomes lower, and at the same time, the Raspberry Pi controller is changed from vertical to horizontal placement, which makes it easier to extract the SD card, and also allows more space to put down hardware components, reducing space waste. thereby reducing the body size.

日期：2022/06/24（星期五）下午 3:18

成員: 呂承諭、胡允瑞

工作內容：

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

工作內容：
  我們今天在機型上增加了一個 OLED，將其接上並下命令安装OLED的顯示功能後，OLED便可以顯示當前的IP地址、電池和電壓等信息，如此一來，我們未來需要這些數據的時候，不必在額外下指令尋找，讓我們更節省時間。

![IMG_5440](https://user-images.githubusercontent.com/107915065/175439789-2ec1e98b-d52e-4027-a285-dc774abfe430.JPG)
-------

Date : 2022/06/22 (Wed) 1:52 p.m.

Member: LU-CHENG YU , HU-YUN RUI

Content: 
    Today we found out that the official website of donkey car has been updated. We used Linux system before, but now Windows system is added.Perhaps for us, the windows system can be more familiar and easy to use.
   
日期：2022/06/22（星期三）下午 1:52

成員: 呂承諭、胡允瑞

工作內容：
    今天我們發現 donkey car 的官網更新了，之前我們使用的是 Linux 系統，而現在新增了 Windows 系統，我們開始對其進行嘗試，或許對於我們來說 windows 會更熟悉，也更好上手。
![1](https://user-images.githubusercontent.com/107915065/174947403-794c4749-618e-499f-a587-691f4d45832a.png)

-------
Date: 2022/06/21 (Tue) 8:11 p.m.

Member: LU-CHENG YU , HU-YUN RUI

Content: 

日期：2022/06/21（週二）下午 8:11

成員：呂承諭、胡允瑞

工作內容：






-------
Date: 2022/06/20 (Mon) 5:19 p.m.

Member: LU-CHENG YU , HU-YUN RUI

Content: 

日期：2022/06/20 （週一）下午 5:19

成員：呂承諭、胡允瑞

工作內容：




-------

Date: 2022/06/18 (Sat) 4:28 p.m.

Member: LU-CHENG YU , HU-YUN RUI

Content: 


日期：2022/06/18（週六）下午 4:28

成員：呂承諭、胡允瑞

工作內容：



-------
Date: 2022/06/17 (Fri) 3:57 p.m.

Member: LU-CHENG YU , HU-YUN RUI

Content: 


日期：2022/06/17（週五）下午 3:57

成員：呂承諭、胡允瑞

工作內容：



-------
Date: 2022/06/16 (Thu) 7:41 p.m.

Member: LU-CHENG YU, HU-YUN RUI

Content: 


日期：2022/06/16（週四）下午 7:41

成員：呂承諭、胡允瑞

工作內容：
![image](https://user-images.githubusercontent.com/107915065/178392251-3e1bc79a-578a-4369-b4c0-321f631acf03.png)

--------
Date: 2022/06/12 (Sun) 6:37 p.m.

Member: LU-CHENG YU

Content: 

Yesterday's training results are quite unstable for the vehicle, so we re-trained around the field to find the cause of the problem, because for the detection of the vehicle, whether it is the speed or the detection is not normal. Objects will still appear abnormal after the training is completed later.

日期：2022/06/12（週日）下午 6:37 

成員：呂承諭

工作內容：

昨天的訓練結果對於車輛來說，還算是很不穩定的，因次我們重新繞場訓練，找尋問題的原因，因為對於車子的偵測來說，不管是速度還是偵測到不屬於正規的的物體，都會在後面訓練完成後，依然出現非正常情況。
![image](https://user-images.githubusercontent.com/107915065/178390050-2902192c-73a1-428f-b63a-4669c89bdce2.png)

--------
Date: 2022/06/11 (Sat) 4:18 p.m.

Member: LU-CHENG YU

Content: 
We finished designing the hardware and structure of the car! So we started to control the car by joystick, let the camera of the car record the route of the field and the control of the car, let the car sprint at full power in the straight line, avoid the black wall in the opposite direction when it meets the wall, and let the car turn right or left according to the current driving direction (clockwise or counterclockwise) when it comes to the turn, but after the training was completed, our model in some cases However, after the training, our model could not complete 3 laps as usual in some cases, even the vehicle can easily get out of control.

日期：2022/06/11（週六）下午 4:18

成員:呂承諭

工作內容：
我們把車輛的硬體和結構設計完成了！於是我們開始透過搖桿控制汽車，讓汽車的攝影鏡頭錄製場地的路線以及汽車的控制，讓汽車在直線的地方全力衝刺，在遇到黑色的牆時會以牆的反方向避開，而到了轉彎處，讓汽車能夠依照當前駕駛方向(順時針或逆時針)向右轉或向左轉，但是在訓練完成之後，我們的模型在有些情況下，無法照常跑完3圈，甚至車輛很容易失控。

![image](https://user-images.githubusercontent.com/107915065/178389208-dbc515b8-af7e-4935-b002-6954b4197956.png)
![289775466_403746338388863_2342595496004969141_n](https://user-images.githubusercontent.com/74124750/178387117-11e8c996-80fd-4b6b-959e-83858c584307.jpg)

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
     
