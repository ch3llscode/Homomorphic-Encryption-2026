import socket
from phe import paillier
import numpy as np
import json

def client_program():
	
	host = "10.12.129.25"
	port = 5025 

	client_socket = socket.socket()  
	client_socket.connect((host, port))  
	
	message = "123"
	
	
	data = ""
	
	
	client_socket.send(message.encode())  
	data= client_socket.recv(102400).decode()  

	print('Received from server: ' + data)  
		
	serialised = data
	received_dict = json.loads(serialised)
	pk = received_dict['public_key']
	public_key_rec = paillier.PaillierPublicKey(int(pk['n']))
	mean = [
		paillier.EncryptedNumber(public_key_rec, int(x[0]), int(x[1]))
		for x in received_dict['values']
		]
	print("Data Collected")
	with open("priv_key.txt") as f:
		data=json.load(f)
	n=int(data["public_key"]["n"])
	p=int(data["private_key"]["p"])
	q=int(data["private_key"]["q"])
	
	public_key=paillier.PaillierPublicKey(n)
	private_key=paillier.PaillierPrivateKey(public_key, p, q)

	answer= input("Do you want to decrypt? (yes/no):")
	if answer.lower() =="yes":
		decrypted_mean=private_key.decrypt(mean[0])
		print("Decrypting")
		print(decrypted_mean)
		
	else:
		enc_with_one_pub_key={}
		enc_with_one_pub_key['public_key']={'n': public_key.n}
		enc_with_one_pub_key['values']=[
		(str(x.ciphertext()), x.exponent) for x in mean
		]
		encrypted_string=json.dumps(enc_with_one_pub_key)
		with open("enc_mean.txt", "w") as f:
			f.write(encrypted_string)
		print("saving in enc_mean.txt")
	

	client_socket.close()  


if __name__ == '__main__':
    client_program()