from base64 import b64encode
import hashlib
import pyaes
import os

salt = b'Salt provided'
iterationCount = 500000

ciphertext = '07c14976d4c29ee283661eae6a94741e70177c9ded3122e2608d51a02f27f6f07df0b9d52a8b5d2e111f139abc4feb6402b7'
# Create random 16 bytes IV 
iv = 50
# Decryption with AES-256-CBC
decrypter = pyaes.Decrypter(pyaes.AESModeOfOperationCBC(key, iv))
decryptedData = decrypter.feed(ciphertext)
decryptedData += decrypter.feed()