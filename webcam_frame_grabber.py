import os
import argparse
from datetime import datetime

import cv2

def webcam_frame_grabber(out_dpath, camera_idx):
    
    if not os.path.isdir(out_dpath):
        os.makedirs(out_dpath)

    cap = cv2.VideoCapture(camera_idx)
    
    if not cap.isOpened():
        raise Exception('Cannot open camera.')
    
    while True:
        ret, frame = cap.read()

        if not ret:
            raise Exception('Did not receive frame. End?')
        
        cv2.imshow('frame', frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        if key == ord('s'):
            frame_fname = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
            frame_fpath = os.path.join(out_dpath, frame_fname + '.png')
            cv2.imwrite(frame_fpath, frame)
            print(f'Saved {frame_fpath}.')

    cap.release()
    cv2.destroyAllWindows()

def main(args):

    webcam_frame_grabber(args.out_dpath, args.camera_idx)

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()    
    parser.add_argument('out_dpath')
    parser.add_argument('--camera_idx', type=int, default=0)
    args = parser.parse_args()

    main(args)
