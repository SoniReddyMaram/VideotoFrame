import sys
import cv2
import os
from glob import glob

def extractFrames(pathIn, pathOut):
    
    if not os.path.exists(pathOut):
        os.mkdir(pathOut)
        
    
 
    video_list = glob(pathIn + '/*.avi')
    count=1
    
    for video in video_list:
        print("Process the video",video)
        
        cap = cv2.VideoCapture(video)
        if not cap.isOpened():
            print('Cant open video {}'.format(video))
            sys.exit(0)
        
        skip_frame=0
        while (cap.isOpened()):
            # Capture frame-by-frame
            ret, frame = cap.read()
            fps = round(cap.get(5))
            skip_frame=skip_frame+fps*60
            if ret == True:
                print('Read %d frame: ' % count, ret)
                cv2.imwrite(os.path.join(pathOut, "frame{:d}.jpg".format(count)), frame)  
                count= count+1
                cap.set(cv2.CAP_PROP_POS_FRAMES,skip_frame)
            else:
                print("Done")
                break
        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()
    
def main():
    extractFrames("Path of your videos folder", 'folder name to extract images')
    # extractFrames("Path of your videos folder", 'folder name to extract images')
    # extractFrames("Path of your videos folder", 'folder name to extract images')
if __name__=="__main__":
    main()
