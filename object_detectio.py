import cv2
import numpy as np
from ultralytics import YOLO

def detection(yolo_model, cap, out):
    # 第一幀處理
    first_frame = True

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error : The image cannot be loaded !")
            break
        
        if first_frame:
            # 將第一幀使用 YOLOv8 進行物件偵測
            results = yolo_model.predict(frame)
            detections = results[0].boxes.xyxy.cpu().numpy()  # 取得物件框座標

            # 初始化追蹤器
            tracker = cv2.legacy.MultiTracker_create()

            for bbox in detections:
                x1, y1, x2, y2 = map(int, bbox[:4])  # 取得邊界框座標
                tracker.add(cv2.legacy.TrackerMOSSE_create(), frame, (x1, y1, x2 - x1, y2 - y1)) # cv2.legacy.TrackerKCF_create()
            first_frame = False
        else:
            # 追蹤物件
            success, boxes = tracker.update(frame)
            for i, new_box in enumerate(boxes):
                x, y, w, h = map(int, new_box)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # 將結果寫入影片
        out.write(frame)

        # 顯示即時畫面
        cv2.imshow('Object Tracking', frame)
        key = cv2.waitKey(1) & 0xFF

        if key == ord('q'):  # 按下 q 結束程式
            print('Quit !')
            break
        elif key == ord('r'):  # 按下 r 重置 first_frame 並清空追蹤器
            print('Reset !')
            first_frame = True


if __name__ == "__main__":
    print('----------------------------------------------------')
    print('Press q for Quit.')
    print('Press r for reset first frame and clear the tracker.')
    print('----------------------------------------------------')

    yolo_model = YOLO('yolov8n.pt')
    vedio_path = './output.avi'
    # 打開攝影機
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error : Cannot open camera !")
        exit()

    # 初始化影片寫入器
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    print(f'Frame Width : {frame_width}, Frame Height : {frame_height}, FPS : {fps}')
    out = cv2.VideoWriter(vedio_path, cv2.VideoWriter_fourcc(*'XVID'), fps, (frame_width, frame_height))
    
    detection(yolo_model, cap, out)
    
    # 釋放資源
    cap.release()
    out.release()
    cv2.destroyAllWindows()
