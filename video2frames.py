__author__ = 'vfdev'

# Python
import argparse
import os
import shutil

# Opencv
import cv2


def main(args):
    print args

    if not os.path.exists(args.input):
        parser.error("Input video file is not found")
        return 1

    if os.path.exists(args.output):
        print "Remove existing output folder"
        shutil.rmtree(args.output)

    os.makedirs(args.output)

    cap = cv2.VideoCapture()
    cap.open(args.input)
    if not cap.isOpened():
        parser.error("Failed to open input video")
        return 1

    frameCount = cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT)

    print frameCount
    maxframes = args.maxframes
    skipDelta = 0
    if args.maxframes and frameCount > maxframes:
        skipDelta = frameCount / maxframes
        print "Video has {fc}, but maxframes is set to {mf}".format(fc=frameCount, mf=maxframes)
        print "Skip frames delta is {d}".format(d=skipDelta)

    frameId = 0
    rotateAngle = args.rotate if args.rotate else 0
    if rotateAngle > 0:
        print "Rotate output frames on {deg} clock-wise".format(deg=rotateAngle)

    while frameId < frameCount:
        ret, frame = cap.read()
        # print frameId, ret, frame.shape
        if not ret:
            print "Failed to get the frame {f}".format(f=frameId)
            continue

        # Rotate if needed:
        if rotateAngle > 0:
            if rotateAngle == 90:
                frame = cv2.transpose(frame)
                frame = cv2.flip(frame, 1)
            elif rotateAngle == 180:
                frame = cv2.flip(frame, -1)
            elif rotateAngle == 270:
                frame = cv2.transpose(frame)
                frame = cv2.flip(frame, 0)

        fname = "frame_" + str(frameId) + ".jpg"
        ofname = os.path.join(args.output, fname)
        ret = cv2.imwrite(ofname, frame)
        if not ret:
            print "Failed to write the frame {f}".format(f=frameId)
            continue

        frameId += int(1 + skipDelta)
        cap.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, frameId)

    return 0

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Video2Frames converter")
    parser.add_argument('input', metavar='<input_video_file>', help="Input video file")
    parser.add_argument('output', metavar='<output_folder>', help="Output folder. If exists it will be removed")
    parser.add_argument('--maxframes', type=int, help="Output max number of frames")
    parser.add_argument('--rotate', type=int, choices={90, 180, 270}, help="Rotate clock-wise output frames")

    args = parser.parse_args()
    ret = main(args)
    exit(ret)