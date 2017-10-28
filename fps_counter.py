# -*- coding: utf-8 -*-
import cv2
import argparse

class FrameRate:
    def __init__(self):
        self._count     = 0
        self._fps       = 0
        self._freq      = 1000 / cv2.getTickFrequency()
        self._tmStart   = cv2.getTickCount()
        self._tmNow     = cv2.getTickCount()
    def get(self):
        self._count     += 1
        self._tmNow      = cv2.getTickCount()
        tmDiff           = (self._tmNow - self._tmStart) * self._freq
        if tmDiff >= 1000 :
            self._tmStart    = self._tmNow
            self._fps        = self._count
            self._count      = 0
        return self._fps


#main
if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Camera streaming')
    parser.add_argument('--ID', '-c', type=int, default=0,help='Camera ID')
    args = parser.parse_args()

    gFrameRate = FrameRate()         # 初期化
    fontcolor = (255,255,255)
    fontface  = cv2.FONT_HERSHEY_SIMPLEX
    fontthick = 2

    cap = cv2.VideoCapture(args.ID)

    while( cv2.waitKey(1) < 0 ):

        ret, ImgFrame = cap.read()
        fps = gFrameRate.get()           # フレームレート取得
        fps_str = '%4d' % fps
        cv2.putText(ImgFrame, fps_str, (10,25), fontface, 1.0, fontcolor, fontthick , cv2.CV_AA)
        cv2.imshow('Capture',ImgFrame)

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
