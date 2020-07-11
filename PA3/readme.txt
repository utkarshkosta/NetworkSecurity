TASK 1:
	COMMANDS :
	python3 t1_server.py
	python3 t1_client.py

	OUTPUT :
	The files sample.avi and sample.mp3 will be transferred from the client to the host.
	Two new files named receivedAudio.mp3 and receivedVideo.avi will be generated, which will be identical to those sent.

TASK 2 and TASK 3:
	COMMANDS :
	python3 spy.py

	OUTPUT : 
	After running the file, 3 files will be generated :
	1. recordedVideo.avi
	2. recordedAudio.npy
	3. keyLog.txt
	Each corresponding to the recorded video, audio and key strokes respectively.
	The duration is 10 seconds and can be changed by modifying the duration variable in spy.py.


TASK 4:
	COMMANDS :
	python3 customVid.py

	OUTPUT :
	The program will generate a 10 second video by using the images in the folder called 'images'.
	The file keyLogger.py records the key strokes for 10 secs and then sends it to the server.

	NOTE :
	1. The video called 'custom.avi' is already attached with the archive. You can delete the file and run the program again to verify.
	2. The file keyLogger.py records the keystrokes and sends it to the server. If only keystrokes are required without sending it to the server, use spy.py.

TASK 5:
	COMMANDS :
	python3 stegnography.py

	OUTPUT :
	Generates a video file called msgHidden.avi using the video custom.avi, it contains the keyLogger.py hidden inside it.
	Now msgHidden.avi will be used to spread the keylogger to clients.

TASK 6 and TASK 7:
	Open 2 terminals and run the following commands, one on each terminal.

	COMMANDS : 
	python3 t6_server.py
	python3 t6_client.py <client_name>

	This will generate a folder called <client_name> in the current directory. The folder contains the video which contains the hidden keylogger, and the keylogger.py extracted from the video and saved with the name 'receivedSpyware.py'

	Now, close the client terminal (leave the server running) and open another terminal in the directory 2019H1030600H_UtkarshKosta/<client_name>.
	Ensure the terminal directory is inside the <client_name> folder.

	In this new terminal, run the command :
	python3 receivedSpyware.py

	This command will record the keystrokes for 10 seconds and send it to the server.
	
	
PLAYING .npy audio files :
	To play a .npy audio file, run the command :
	python3 playAudio.py <audio_file>.npy
