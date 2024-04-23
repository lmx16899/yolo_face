#匯入模組
import cv2
from PIL import Image, ImageOps, ImageFilter

#攝像頭
cap = cv2.VideoCapture(0)#這裡如果你是預設的攝像頭，那麼就是0，否則你要取1


num = 1
while(cap.isOpened()):#檢測是否在開啟狀態
    ret_flag,Vshow = cap.read()#得到每幀影像
    cv2.imshow("Capture_Test",Vshow)#顯示影像
    k = cv2.waitKey(1) & 0xFF#按鍵判斷
    if k == ord('s'):#儲存
        cv2.imwrite('C:/Users/lmx16/Desktop/V1/mydata1/ '+str(num+63)+".jpg",Vshow)#儲存路徑
        print("success to save "+str(num)+".jpg")
        print("-------------------------")
        num += 1
    elif k == ord(' '):#空格退出
        break

  #釋放攝像頭
cap.release()
#釋放記憶體
cv2.destroyAllWindows()















