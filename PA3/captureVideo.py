import numpy as numpy
import cv2
import time


def record_video(duration, captureObject):
	# cv2.namedWindow("test", 1)
	frames_ = []
	start = time.time()
	while(1):
		ret, frame_ = captureObject.read()
		end = time.time()
		if ret == True:
			# cv2.imshow("test", frame)
			frames_.append(frame_)
			cv2.waitKey(1)
			t = end - start 
			print(t)
			if (int(t) == duration):
				break
		else:
			break
	return frames_


if __name__=='__main__':
	cap = cv2.VideoCapture(0)
	width = int(cap.get(3))
	height = int(cap.get(4))
	out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (width, height))
	# print(type(out))
	frames = record_video(5, cap)
	for frame in frames:
		out.write(frame)
	cap.release()
	out.release()
	cv2.destroyAllWindows()