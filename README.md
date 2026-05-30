# Homomorphic-Encryption-2026
This project is the result of my research experience of learning about homomorphic encryption with Professor Jung at Notre Dame. 

This is a client-server model where both programs should run simulatenously. Before runnning either program though, you should run num.py first to generate and store the private and public keys and encrypt numbers found in num.txt. This program should serialize the keys and encrypted numbers on .txt files. Later the client program will deserialize the private key to decrypt the encrypted result. 

The client-server model works like this: the client encrypts their data, serializes it, and then sends the encrypted numbers to the server. The server then deserializes the numbers, calculates the mean,serializes the encrypted result, and sends the result back to the client. Finally, the client will deserialize the encrypted mean and use the stored private key to decrypt it back into its plaintext form. 

The purpose of these programs was to demostrate how the use of homomorphic encryption allows for the protection of the client's data while still enabling the server to do its job. Homomorphic encryption provides privacy and protection to the client's personal information. Unfortunately when building this program, I was unable to figure out how to send the .txt files from server to client if they are different devices. So for the matter of actually running the program make sure you open the client and server program on the same device. 
