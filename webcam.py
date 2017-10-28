#python library
import numpy as np
import argparse
import os

#OpenCV
import cv2


# preparing to save the video
def initWriter(camera_ID, w, h, fps, save_path):
    #fourcc = cv2.cv.CV_FOURCC('D','I','B',' ')
    #fourcc = cv2.cv.CV_FOURCC('D','I','V','X')
    fourcc = cv2.cv.CV_FOURCC('F','L','V','1')
    rec = cv2.VideoWriter(save_path+'camera_'+str(camera_ID)+'.avi', \
                          fourcc, fps, (w, h))
    return rec


# capture the video
def capture(camera_ID, trial_number):

    fps = 30

    # DELL insoiron13
    # width = 640
    # height = 480
    # brightness = 0.6
    # contrast = 0.08
    # saturation = 0.7

    # OpnenCampus
    # width = 1280  #640
    # height = 800  #480
    # brightness = 0.501960813999
    # contrast = 0.1254902035
    # saturation = 0.109803922474

    # Tsukucha
    width = 1280   #320
    height = 800  #240
    brightness = 0.498039215803
    contrast = 0.6
    saturation = 0.3

    cap = cv2.VideoCapture(camera_ID)

    print '\n'+'dafault value'
    print 'width: '+str(cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH))
    print 'height: '+str(cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))
    #print 'frame rate: '+str(cap.get(cv2.cv.CV_CAP_PROP_FPS))
    print 'brightness: '+str(cap.get(cv2.cv.CV_CAP_PROP_BRIGHTNESS))
    print 'contrast: '+str(cap.get(cv2.cv.CV_CAP_PROP_CONTRAST))
    print 'saturation: '+str(cap.get(cv2.cv.CV_CAP_PROP_SATURATION))+'\n'

    cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, height)
    cap.set(cv2.cv.CV_CAP_PROP_BRIGHTNESS, brightness)
    cap.set(cv2.cv.CV_CAP_PROP_CONTRAST, contrast)
    cap.set(cv2.cv.CV_CAP_PROP_SATURATION, saturation)
    # cap.set(cv2.cv.CV_CAP_PROP_FPS, fps)

    video_path = 'videos/' + str(trial_number) + '/'
    image_path = 'pictures/' + str(trial_number) + '/'
    img_cnt = 0

    if not os.path.isdir(video_path):
        os.makedirs(video_path)

    if not os.path.isdir(image_path):
        os.makedirs(image_path)

    rec = initWriter(camera_ID, width, height, fps, video_path)
    cv2.namedWindow('camera:'+str(camera_ID), cv2.WINDOW_NORMAL)
    save_flag = False

    while(True):

        ret, frame = cap.read()
        #frame = cv2.flip(frame, 1)

        print cap.get(cv2.cv.CV_CAP_PROP_FPS)

        if ret == False:
            print 'error'
            break

        cv2.imshow('camera:'+str(camera_ID), frame)

        k = cv2.waitKey(1)

        if k & 0xFF == 27: #Esc
            break

        if k & 0xFF == ord('v'):
            print 'start recording.'
            save_flag = True

        if k & 0xFF == ord('p'):
            cv2.imwrite(image_path+'/im'+str(img_cnt)+'.jpg', frame)
            print 'picture saved.'
            img_cnt += 1

        if save_flag:
            rec.write(frame)

    cap.release()
    rec.release()


#main
if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='taking photos, videos.')
    parser.add_argument('--ID', '-i', type=int, default=0,help='camera ID')
    parser.add_argument('--trial_number', '-n', type=int, default=1,help='number of trial')
    args = parser.parse_args()

    capture(args.ID, args.trial_number)
    #cv2.dstroyAllWindows()
