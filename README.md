#### 資訊工程學系(1131)
# 智慧多媒體設計與創作實驗(B4CS040007A)  
> 1. [Realtime Object Detection Using YOLOv8n](https://github.com/Anguschen1011/YOLO_Project/blob/main/README.md#1-realtime-object-detection-using-yolov8n)  
> 2. [Object Segmentation Using YOLOv9c](https://github.com/Anguschen1011/YOLO_Project/tree/main?tab=readme-ov-file#2-object-segmentation-using-yolov9c)  
> 3. [Object Detection Using YOLO11m](https://github.com/Anguschen1011/YOLO_Project/tree/main?tab=readme-ov-file#3-object-detection-using-yolo11m)



## 1. Realtime Object Detection Using YOLOv8n 
- 開啟攝影機，使用程式擷取攝影機的畫面  
- 將第一個 Frame，使用 YOLOv8 進行物件偵測與辨識  
- 將所偵測的物件座標點傳給追蹤器  
- 進行物件追蹤  
- 生成一個影片包含物件追蹤的結果  

<br>

- Turn on the camera and use a program to capture the camera feed.
- Use YOLOv8 to perform object detection and recognition on the first frame.
- Send the detected object coordinates to the tracker.
- Perform object tracking.
- Generate a video containing the results of object tracking.
### Environments
```
conda create --name object_detection python=3.8 -y
conda activate object_detection

# install packages
pip install ultralytics

pip uninstall opencv-python
pip install opencv-contrib-python
```
### Run  
```
Realtime_object_detection/object_detectio.py
```
### Results (Running on Apple M1 silicon)
![result_example](Realtime_object_detection/result/results.gif) 



## 2. Object Segmentation Using YOLOv9c
NuInsSeg Dataset : [[Kaggle]](https://www.kaggle.com/datasets/ipateam/nuinsseg/data)
- contains more than 30k manually segmented nuclei from 31 human and mouse organs and 665 image patches extracted from H&E-stained whole slide images.  

### Environments
```
conda create --name object_detection python=3.8 -y
conda activate object_detection

# install packages
pip install ultralytics 
pip install pycocotools 
pip install scikit-learn 
pip install matplotlib
```

See notebook at :  
```
Nuclei_Instance_Segmentation/Yolov9c_segmentation.ipynb
```

### Results

See more reults in :   
```
Nuclei_Instance_Segmentation/results
```

```
Result after training 100 epochs.
Training on Colab T4 GPU

Class     Images  Instances      Box(P          R      mAP50  mAP50-95)     Mask(P          R      mAP50  mAP50-95)
  all        133       6285      0.848      0.796      0.872      0.519      0.839      0.783      0.856      0.465
```



## 3. Object Detection Using YOLO11m
Underwater Plastic Pollution Detection Dataset : [[Kaggle]](https://www.kaggle.com/datasets/arnavs19/underwater-plastic-pollution-detection)
- Train Directory:  
  - Contains 3,628 images along with their associated labels.  
- Valid Directory:  
  - Comprises 1,001 images paired with their respective labels.  
- Test Directory:  
  - Encompasses 501 images along with their labels.  
- Number of Class : 15  
  - Class Names - ['Mask', 'can', 'cellphone', 'electronics', 'gbottle', 'glove', 'metal', 'misc', 'net', 'pbag', 'pbottle', 'plastic', 'rod', 'sunglasses', 'tire']  

### Environments
```
conda create --name object_detection python=3.8 -y
conda activate object_detection

# install packages
pip install ultralytics
pip install --upgrade kagglehub albumentations
sudo apt install tree
```

See notebook at :  
```
Underwater_Plastic_Pollution_Detection/yolo11m_underwater_plastics_detection.ipynb
```

### Results  

See more reults in :   
```
Underwater_Plastic_Pollution_Detection/results
```

```
Result after training 100 epochs
Training on Colab T4 GPU

       Class     Images  Instances      Box(P          R      mAP50  mAP50-95)
         all       1001       1891      0.857      0.741      0.815     0.523
        Mask         77         90          1       0.43      0.802     0.624
         can         18         20      0.854        0.7      0.782     0.308
   cellphone         61         71      0.931      0.972      0.981     0.885
 electronics         27         40      0.936       0.73      0.834      0.51
     gbottle         36         82      0.821      0.744      0.784     0.588
       glove         37         55      0.916      0.794      0.854      0.71
       metal         10         22      0.794      0.351      0.596     0.363
        misc         48         51       0.58      0.813      0.685     0.407
         net        146        148      0.937      0.907      0.952     0.699
        pbag        290        330      0.895      0.961       0.98     0.873
     pbottle        122        284      0.803      0.777      0.822     0.515
     plastic         51         59      0.721       0.61      0.665     0.272
         rod          7          9      0.854      0.667      0.715     0.253
  sunglasses          3          3      0.977          1      0.995     0.478
        tire        143        627      0.834      0.667      0.777     0.358
```

