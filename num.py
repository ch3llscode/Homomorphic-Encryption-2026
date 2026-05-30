from phe import paillier
import numpy as np
import json

public_key, private_key = paillier.generate_paillier_keypair()
print("KeyGen is done")

data= {
	"public_key": {"n": str(public_key.n)},
	"private_key":{"p": str(private_key.p), "q": str(private_key.q)}
	}
with open("priv_key.txt", "w") as f:
	json.dump(data,f)

number_list=[0,0,0,0,0,0,0,0,0,0]

with open("num.txt") as f:
	i = 0
	for x in f:
		number_list[i] = int(x)
		i = i + 1

print("Numbers Collected")


encrypted_number_list =[public_key.encrypt(x) for x in number_list]


print("Encryption is done")


enc_with_one_pub_key={}
enc_with_one_pub_key['public_key']={'n': public_key.n}
enc_with_one_pub_key['values']=[
	(str(x.ciphertext()), x.exponent) for x in encrypted_number_list
	]
encrypted_string=json.dumps(enc_with_one_pub_key)

with open("enc_blood.txt", "w") as f:
	f.write(encrypted_string)

print("Encrypted Numbers in File")

