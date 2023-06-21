## passgen

### Description :

##### English :

````
PassGen is an advanced tool for generating strong passwords, whether for personal use or to create a wordlist. It offers the option of double-encrypting passwords using the SHA-256 and SHA-3 hash algorithms, thus enhancing the security of your data.

You'll benefit from a wide range of arguments for password generation, encryption, combined generation with encryption, as well as content transfer to a file.

When generating passwords, you'll have full control over specifying the number of characters and the number of passwords required. As far as encryption is concerned, you'll have the option of encrypting your own password, as well as
taking advantage of an automatic generation option with double encryption.

So you can manage your password generation and encryption with ease.
````

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

##### French :

````
PassGen est un outil avancé qui vous permet de générer des mots de passe robustes, que ce soit pour un usage personnel ou pour créer une wordlist. Il offre la possibilité de réaliser un double chiffrement des mots de passe en utilisant les algorithmes de hachage SHA-256 et SHA-3, renforçant ainsi la sécurité de vos données.

Vous bénéficierez d'une étendue d'arguments pour la génération de mots de passe, le chiffrement, la génération combinée avec chiffrement, ainsi que le transfert du contenu vers un fichier.

Lors de la génération des mots de passe, vous aurez le contrôle total pour spécifier le nombre de caractères et le nombre de mots de passe souhaités. En ce qui concerne le chiffrement, vous aurez la possibilité de chiffrer votre propre mot de passe, mais également de profiter d'une option de génération automatique avec double chiffrement.

Ainsi, vous pourrez gérer efficacement la génération et le chiffrement de vos mots de passe en toute simplicité.
````

### Utilisation :

##### Command :

````python3.11 ./passgen.py "option"````

##### Manual :

````
usage: passgen.py [-h] [-pG] [-sG] [-eP] [-gEP] [-fT]

Password Generator + SHA-256 and SHA-3 Encryption

options:

  -h, --help            show this help message and exit
  
  -pG, --passwordGeneration          --> Password Generation
  -sG, --wordlistGeneration          --> Password generation for wordlist creation
  -eP, --encryptPassword             --> Encryption of your own password
  -gEP, --generateEncryptedPassword  --> Password Generation + Encryption
  -fT, --fileTransfer                --> Transfer of the content to a file
````

##### Example :










