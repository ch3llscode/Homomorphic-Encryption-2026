import socket
from phe import paillier
import numpy as np
import json


def server_program():
    # get the hostname
	#host = socket.gethostname()
	host = "10.12.226.39"
	port = 5025 

	server_socket = socket.socket()  
	server_socket.bind((host, port))  

   
	conn, address = server_socket.accept()  
	print("Connection from: " + str(address))
    
	with open("enc_blood.txt") as f:
		serialised = f.read()
	received_dict = json.loads(serialised)
	pk = received_dict['public_key']
	public_key_rec = paillier.PaillierPublicKey(int(pk['n']))
	enc_nums_rec = [
		paillier.EncryptedNumber(public_key_rec, int(x[0]), int(x[1]))
		for x in received_dict['values']
	]

	print("Deserialised successfully")



	enc_mean=np.mean(enc_nums_rec)

	print("Mean calculations on ciphertexts is done")
    
	enc_with_one_pub_key={}
	enc_with_one_pub_key['public_key']={'n': public_key_rec.n}
	enc_with_one_pub_key['values']=[
		(str(enc_mean.ciphertext()), enc_mean.exponent)
		]
	encrypted_string=json.dumps(enc_with_one_pub_key)
    
	while True:
		
		data = conn.recv(1024).decode()
		if not data:

			break
		print("from connected user: " + str(data))
		data = encrypted_string
		conn.send(data.encode()) 
	conn.close()  


if __name__ == '__main__':
    server_program()