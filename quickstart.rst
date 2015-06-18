+Quickstart Information
======================

Project: 
========
Corrobo

Github URL: 
===========
https://github.com/johnwlockwood/corrobo

Docs URL:
=========
http://corrobo.readthedocs.org/en/latest/

Goals of the project:
=====================
Build an authentication provider.
Provide an IAM service. Provide as a microservice.
Frontend widgets to use the library.
Focus on knowing the identity across many services, not the transmission of data.

Use Cases:
==========
+ integration into application such as a flask app
+ 2nd factor authentication source (eg through twilio / getclef)

What libraries could this library consume?
=================================
+ crypto libraries
+ requests / https


Protocols to support:
=====================
RSA?
DH?

Note: Apparently it depends on the context (http://security.stackexchange.com/questions/35471/is-there-any-particular-reason-to-use-diffie-hellman-over-rsa-for-key-exchange)


Python Cryptography Libraries:
==============================
+https://pypi.python.org/pypi/pycrypto
+https://pypi.python.org/pypi/rsa
+https://docs.python.org/2/library/hmac.html - token hash flask-login
+https://docs.python.org/2/library/crypt.html - hash passwords, django
+libsodium
+https://pypi.python.org/pypi/bcrypt/1.1.0 - hash passwords, django
+all default django hashers: https://docs.djangoproject.com/en/1.8/topics/auth/passwords/
+more django: https://github.com/django/django/blob/55b3bd84681a87266f6bef72480aaef48a7c295f/docs/topics/auth/passwords.txt
+DJANGO: 
PASSWORD_HASHERS = (
    'myproject.hashers.MyPBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.SHA1PasswordHasher',
    'django.contrib.auth.hashers.MD5PasswordHasher',
    'django.contrib.auth.hashers.CryptPasswordHasher',
)




Definitions:
============

microservice:
=============
def: In computing, microservices is a software architecture style, in which complex applications are composed of small, independent processes communicating with each other using language-agnostic APIs. These services are small, highly decoupled and focus on doing a small task.
link: https://en.wikipedia.org/wiki/Microservices

IAM:
====
syn: IdM, IM, Identity Mangement, also IAM Services
def: In computing, identity management (IdM) describes the management of individual principals, their authentication, authorization,[1] and privileges within or across system and enterprise boundaries[2] with the goal of increasing security and productivity while decreasing cost, downtime and repetitive tasks.
link: https://en.wikipedia.org/wiki/Identity_management

Public-key Cryptography
=======================
syn: Asymmetric Cryptography
def: A class of cryptographic protocols based on algorithms that require two separate keys, one of which is secret (or private) and one of which is public. Although different, the two parts of this key pair are mathematically linked. The public key is used, for example, to encrypt plaintext or to verify a digital signature; whereas the private key is used for the opposite operation, in these examples to decrypt ciphertext or to create a digital signature. The term "asymmetric" stems from the use of different keys to perform these opposite functions, each the inverse of the other – as contrasted with conventional ("symmetric") cryptography which relies on the same key to perform both. Based on modulus math (from j lockwood).
link: https://en.wikipedia.org/wiki/Public-key_cryptography
more: http://security.stackexchange.com/questions/9260/sha-rsa-and-the-relation-between-them