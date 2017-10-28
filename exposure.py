# -*- coding: utf-8 -*-
import cv2
import subprocess

cap = cv2.VideoCapture(0)

cmd='v4l2-ctl -d /dev/video0 -c exposure_auto=3' # 自動露出
ret = subprocess.check_output([cmd],shell=True)

# 設定した後にすぐ変更するとうまく反映されないので、10回程度ムダにカメラ回す
_ = [cap.read()[:1] for i in range(10)]

cmd='v4l2-ctl -d /dev/video0 -c exposure_auto=1' # 現状で露出固定
ret = subprocess.check_output([cmd],shell=True)

while( cv2.waitKey(1) < 0 ):

    ret, ImgFrame = cap.read()
    cv2.imshow('Capture',ImgFrame)

    print 'frame rate: '+str(cap.get(cv2.cv.CV_CAP_PROP_FPS))

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
