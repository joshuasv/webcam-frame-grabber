import os
import argparse
from datetime import datetime

import cv2


def save_picture(out_dpath, frame):
    # Save frame to disk
    frame_fname = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
    frame_fpath = os.path.join(out_dpath, frame_fname + '.png')
    cv2.imwrite(frame_fpath, frame)
    total_in_dir = len(os.listdir(out_dpath))
    print(f'Saved {frame_fpath}. Total: {total_in_dir}')

def webcam_frame_grabber(out_dpath, camera_idx, mode):
    
    # Create output directory if it does not exist
    if not os.path.isdir(out_dpath):
        os.makedirs(out_dpath)

    # Stream placeholder variables
    cont_capture = False
    cont_dpath = None

    # Initialize camera
    cap = cv2.VideoCapture(camera_idx, cv2.CAP_V4L)

    # Handle not being able to open camera
    if not cap.isOpened():
        raise Exception('Cannot open camera.')
    
    # Start acquiring data from the webcam
    while True:
        # Capture frame
        ret, frame = cap.read()
        # Handle not being able to receive frame
        if not ret:
            raise Exception('Did not receive frame. End?')
        # Display current frame 
        cv2.imshow('frame', frame)
        # Wait for user input
        key = cv2.waitKey(1) & 0xFF
        # Exit application
        if key == ord('q'):
            break
        # Start capturing
        if key == ord('s'):
            # Save image right away
            if mode == 'frame':
                save_picture(out_dpath, frame)
            # Start streaming process
            elif mode == 'stream':
                if not cont_capture:
                    # Create directory for the current capturing stream
                    cont_dname = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
                    cont_dpath = os.path.join(out_dpath, cont_dname)
                    os.makedirs(cont_dpath)
                # Switch variable to start/stop continuous acquisition
                cont_capture = not cont_capture
            else:
                raise Exception(f'Mode {mode} not expected.')

        # Save frame on stream mode 
        if mode == 'stream' and cont_capture:
            save_picture(cont_dpath, frame)

    # Release resources
    cap.release()
    cv2.destroyAllWindows()

def main(args):

    webcam_frame_grabber(args.out_dpath, args.camera_idx, args.mode)

if __name__ == '__main__':
    
    # Parent parser for common arguments
    parent_parser = argparse.ArgumentParser(add_help=False)
    parent_parser.add_argument('out_dpath')
    parent_parser.add_argument('--camera_idx', type=int, default=0)
    # Top-level parser
    parser = argparse.ArgumentParser(description='Let\'s grab frames from your webcam!')
    subparsers = parser.add_subparsers(dest='mode', help='Operating mode')
    subparsers.required = True
    # Parser for the frame mode    
    parser_frame = subparsers.add_parser('frame', parents=[parent_parser], help='Frame mode')
    # Parser for the stream mode
    parser_stream = subparsers.add_parser('stream', parents=[parent_parser], help='Stream mode')
    args = parser.parse_args()

    main(args)
