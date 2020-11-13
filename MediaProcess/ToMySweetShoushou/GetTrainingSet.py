# coding:utf-8
from sys import call_tracing
import cv2
import sys
import os
from time import sleep, time
import hashlib
# reload(sys)
def md5(data):
    m = hashlib.md5()
    m.update(data.encode('utf8'))
    a = m.hexdigest()
    return a
# sys.setdefaultencoding('utf8')
def Cacth(Mypath):
    cap = cv2.VideoCapture(0)
    cap.set(3,640)
    cap.set(4,480)
    cap.set(1, 10.0)  
    # fourcc = cv2.VideoWriter_fourcc(*'XVID')
    # home = os.path.expanduser("~")
    # des = './'+Mypath+'/'
    # out = cv2.VideoWriter(des+'video.avi', fourcc,30,(640,480))
    before=time()
    for i in range(1,70):
        ret,frame = cap.read()
        if ret == True:
            frame = cv2.flip(frame, 1)
            # a = out.write(frame)
            cv2.imwrite("./"+Mypath+"/"+str(i)+".png", frame)	
            #sleep(0.01)
            # k = cv2.waitKey(0)
            # if k == 27:
            #     break
        else:
            break
    print("Costs time:",time()-before)
    cap.release()
    # out.release()
    cv2.destroyAllWindows()

def Doit():
    
    Mypath=md5(str(time()))
    if not os.path.exists("./"+Mypath):
        os.makedirs("./"+Mypath)
    print("Meida Resouce Saved in "+"./"+Mypath)
    Cacth(Mypath)
    
# 用python3直接运行就行
Doit()
