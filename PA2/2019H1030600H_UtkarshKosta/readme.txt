Submitted by : Utkarsh Kosta, 2019H1030600H

Kindly make sure all files are in the same directory, as some files utilise functions in other files.

TASK 1 : 

	Run the command : python3 rsa.py <file_to_encrypt>
	eg : python3 rsa.py rsa.py

	Output format : 
	1. The cipher text generated is printed on the terminal screen.
	2. The cipher text is then deciphered and a file called 'deciphered_file' is generated in the same directory.

TASK 2 :

	Run the command : python3 smc.py

	Output format :
	1. The program automatically selects two random integers x and y and runs the secure two party protocol.
	2. The output (x <= y or x > y) along with their values, the keys (e,d,n), the value of m1, c1 etc. is displayed on the terminal.


TASK 3 and TASK 4 :

	1. Open 2 terminals.
	2. On one terminal, run the command : python3 server.py
	Now the server will be listening for new connections.
	3. On the other terminal, run the command : python3 client.py <username> <password>

	NOTE:
	If you wish to run multiple clients, run the above command multiple times. Each time give the appropriate username and password.
	eg : 
	python3 server.py (terminal 1)
	python3 client.py user1 pass1 (terminal 2)
	python3 client.py user2 pass2 (terminal 2)
	python3 client.py user3 pass3 (terminal 2)

	Output format : 
	The client having username : <username> and password : <password> will register itself to the server. The output prints the table storing the (username, password hash and public key) of clients, on the terminal running the server.

TASK 5 :

	1. Open 3 terminals.
	2. First, run the command : 
	python3 smc_server.py    (terminal 1)
	3. Second, run the command for client1 : 
	python3 smc_client.py c1 <x>	(terminal 2)
	4. Third, run the command for client2 : 
	python3 smc_client.py c2 <y>	(terminal 3)
	5. Replace the values <x> and <y> with appropriate integers.

	NOTE:
	1. Run the commands in the order specified, otherwise the program results in some internal synchronisation issue that was out of the scope of this assignment.
	2. In case an error mentioning "out of range value for the randint()" or "invalid literal for int() with base 10", kindly repeat the above procedure after deleting the files c1 & c2.


	Output format :
	1. terminal 1 prints the registered client details (username, password hash, public key).
	2. terminal 2 (running c1 who has value x) prints out the received public key of c2, selected m1, and the final result (x <= y or x > y).
	3. terminal 3 (runnning c2 who has value y) prints out the result received from c1 (x <= y or x > y).
