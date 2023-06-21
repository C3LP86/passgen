import argparse
import random
import string
import hashlib
import pyfiglet



print("")
print("<====================================================================================>")

ascii_banner = pyfiglet.figlet_format("PASSGEN")
print(  ascii_banner  )

print("<====================================================================================>")
print("")



parser = argparse.ArgumentParser(description='Password Generator + SHA-256 and SHA-3 Encryption')

parser.add_argument("-pG", "--passwordGeneration", action="store_true", help="Password Generation")
parser.add_argument("-sG", "--wordlistGeneration", action="store_true", help="Password generation for wordlist creation")
parser.add_argument("-eP", "--encryptPassword", action="store_true", help="Encryption of your own password")
parser.add_argument("-gEP", "--generateEncryptedPassword", action="store_true", help="Password Generation + Encryption")
parser.add_argument("-fT", "--fileTransfer", action="store_true", help="Transfer of the content to a file")

args = parser.parse_args()



if hasattr(args, 'help'):
    parser.print_help()
    exit()



if args.passwordGeneration:

	punctuation = string.punctuation.replace(",", "")
	caractères = string.ascii_letters + string.digits + punctuation

	x = int(input("Indicates the desired number of characters (minimum -> 12) : "))

	if x >= 12:
		y = int(input("Indicates the number of passwords required : "))
		def Generator_Password():
			Password = ""
			for i in range(x):
				Password += random.choice(caractères)
			return Password

		n = 1
		passwords = ""
		for j in range(y):
			password = Generator_Password()
			passwords += f"[{n}] - " "Here's the password : " + password + "\n"
			n += 1

		print(passwords)

	else:
		while x < 12:
			print("You must have at least 12 characters !")
			x = int(input("Indicates the number of characters required (minimum -> 12) : "))

		y = int(input("Indicates the number of passwords required : "))
		def Generator_Password():
			Password = ""
			for i in range(x):
				Password += random.choice(caractères)
			return Password

		n = 1
		passwords = ""
		for j in range(y):
			password = Generator_Password()
			passwords += f"[{n}] - " "Here's the password : " + password + "\n"
			n += 1

		print(passwords)



if args.wordlistGeneration:

	caractères = string.ascii_letters + string.digits + string.punctuation

	x = int(input("Indicates the number of characters required (minimum -> 12) : "))

	if x >= 12:
		y = int(input("Specifies the number of passwords required : "))
		def Generator_Password():
			password = ""
			for i in range(x):
				password += random.choice(caractères)
			return password

		passwords = ""
		for j in range(y):
			password = Generator_Password()
			passwords += password + "\n"
			
		print(passwords)

	else:
		while x < 12:
			print("You must have at least 12 characters !")
			x = int(input("Indicates the number of characters required (minimum -> 12) : "))

		y = int(input("Indicates the number of passwords required : "))
		def Generator_Password():
			password = ""
			for i in range(x):
				password += random.choice(caractères)
			return password

		passwords = ""
		for j in range(y):
			password = Generator_Password()
			passwords += password + "\n"
			
		print(passwords)



if args.encryptPassword:
	
	print("SHA-256 / SHA3 encryption of current password")
	print("")

	passwords = ""
	
	password = input("Indicates the password to be encrypted : ")
	
	hash_object_sha256 = hashlib.sha256()
	password_bytes = password.encode('utf-8')
	hash_object_sha256.update(password_bytes)
	hash_sha256 = hash_object_sha256.digest()

	hash_object_sha3 = hashlib.sha3_256()
	hash_object_sha3.update(hash_sha256)
	hash_sha3 = hash_object_sha3.digest()
	encryption = hash_sha3.hex()

	passwords += "The encrypted password is : " + encryption + "\n" 

	print(passwords)



if args.generateEncryptedPassword:

	caractères = string.ascii_letters + string.digits + string.punctuation

	x = int(input("Indicates the number of characters required (minimum -> 12) : "))

	if x >= 12:
		y = int(input("Indicates the number of passwords required : "))
		def Generator_Password():
			Password = ""
			for i in range(x):
				Password += random.choice(caractères)
			return Password

	else:
		while x < 12:
			print("You must have at least 12 characters !")
			x = int(input("Indicates the number of characters required (minimum -> 12) : "))

		y = int(input("Indicates the number of passwords required : "))
		def Generator_Password():
			Password = ""
			for i in range(x):
				Password += random.choice(caractères)
			return Password
	
	print("")
	print("SHA-256 / SHA3 encryption of current password")
	print("")

	passwords = ""
	for j in range(y):
		password = Generator_Password()

		hash_object_sha256 = hashlib.sha256()
		password_bytes = password.encode('utf-8')
		hash_object_sha256.update(password_bytes)
		hash_sha256 = hash_object_sha256.digest()

		hash_object_sha3 = hashlib.sha3_256()
		hash_object_sha3.update(hash_sha256)
		hash_sha3 = hash_object_sha3.digest()
		encryption = hash_sha3.hex()

		passwords += f"[{j+1}] - The password '{password}' encrypted in SHA256 / SHA3 right here : {encryption}\n"

	print(passwords)



if args.fileTransfer:
	file = input("Enter the name of the file where you want to place the result : ")
	with open(file, "w") as f:
		f.write(str(passwords))