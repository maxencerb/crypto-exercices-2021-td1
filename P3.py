import binascii
from typing import List

alphabet = 'abcdefhijklmnopqrstuvwxyzABSDEFHIJKLMNOPQRSTUVWXYZ'
alphabet_ascii_num = [ord(c) for c in alphabet]
to_remove = '#$%&*+/<=>@[\]^_`{|}~'


ciphertexts = [
    "44dcf620955a4d1dd497d4725e07588aef87cd44c9674f4ea5bc1bb35b25646c6f73f8f8c28780c47bec0c42b596b6c3659ab15841e43985b4c3441d2c30e7014ef1a367296f7b956f976b16f36919fecd7daa37bacd6d682bead9de1ccead97e98d1bce0df9b95a56a77bc6cb42caa6a5cbab1ea74e9475709ecd9e9b030d3f9c5b591f0302ebeea56c7c",
    "56ccba2686141a14c098c43d5c554380ebc5cf4884604456eaf40ee7442d6424216dfab9c49a86892fe70640b786af86758cfc177be46ac6b48d0713322ded5308e3b47c28787b8e61d2280aff740ff49f70bb43f4d46b723aa7d78b0b81a5d9bdba0fcb06eefa0902bc33c1c542c4eb",
    "47d1b3639a5d0e1e9580c87442400c83e8c8d645844e4f59fce141e20c256324216dfab9db96d5ca29f6135baa84b0c76781fa0a65a17a87bb8d000e2935ed0149b0ac7c323d348727942a16e57d5bf8de2fe822b79a407d2deafa9116c4a2",
    "47d1b363975d1d13d086d47854530c92f8c8c744c7604e1ce7f40ef20c3b75652422e8f7cf818cd92fe60c41e582aec1789bf60c7eec398abac20f0f6022fb014fffaf77667c28c1649b3b10e3760ffec729bb72e8d5606920afdcde1ad8ead6bd8c0ed50cf2ba5a47a638d6d340d5efbecdf91aae098f6e748fd6d3960e7f0096574702536ad0f5a464607d6dd454c9",
    "4ad6a363905b035cc1d4d77c42530c96e587c144dd254b1cf6e85ab3432a30672e70adf2c98a86893dfd0c42e582e2c16290bf0f7eee3995a5c80715212fe15b4de3e07a283d289562932711e8635bf8de2fe822b79a497d31a998ac17d5afd9ff9a08c043ffb2174fad35d0c35ec6a6becdf938ae07906c7889",
    "47d1b33191140c09d0d4d46a4307589bfac2d011cb630a5ff7f45ee7432b62653f6af4b981d381c13afb4358ad8aa1ce379ef6147aa17283b0dd440f2520fa445ce3e060277b3ec161802415a67d14eecd7df76beece687963b9d18d0cc4b89bbd9e14c343e8b51b56e82cccc353c9a6a6cab517e20585796ddbcddbd5513a248d1e580a452faafabb66682f79da4fd51442d25b6c75baeffbb449cf87cbf90f19619580bf66bc09f80a228b",
    "47d1b33191140c09d0d4d46a4307589bfac2d011cb630a5ffcfd5afc4b3e7174277bb7b9c39d90892fe7025be582aeca789eec5862e97cc692c21219322de54446e4e067293d2e9262d2290af3701ebbd932e961ff9a707363a8ca9b19caeac3f59a5ac40cf8b85602a935c08a5fcfe3f1d7b11ab64e92796c8ed7ccd3507f24965b0b2c4c3cefeea764606174954ec81450ce482965a6f7eabf1d89c599d8184c769f808e77b106f6433e96b3",
    "44dcf620955a4d08d091806944420c92e5cecd4584724259f7e80ee744293067276bfdb9c580d5dc35e7025fb59ae2cf71c9fe5861f37688b28d06153463e15208e3a57d323d3a8f63d22817e8770ef6da2ebb6ff5c8613c33a5cf9b0a81acc5f2925ad30bf9fd1f4cbe32d6c55ecce3bfd7f956e22f84753da8d6dfdb4a2d",
    "47d1b363b75b0318dc87c53d635f4a8df8c38375cd665e55eae34fe1556c38367f32bbb08c9790cf32e1065ce580b0df679df05877f23992bdc8441d3237a84e4eb0b7612f69328f60d2240aa67714f7c934f565bad96b7826b996",
    "47d1b36387510e09d080807049545f83edc28358d73f0a6bede840b3593f796a2822e2f7c9de81c036ea435fa487ee86798ce91d64a16c95b08d10142563e34451b0ad7c34787b956f932558e96a18fe91",
]

# xoring char with space gives that char lowercase if it is uppercase and vice versa

max_length = max(list(map(lambda x: len(x), ciphertexts)))
key = [[] for _ in range(int(max_length/2))]

def hasSpace(num):
	return num in alphabet_ascii_num

def try_get_key():
	global key
	global ciphertexts
	for i in range(0, max_length, 2):
		current_cipher = [c for c in ciphertexts if len(c) > i]
		for cipher1index in range(len(current_cipher) - 1):
			for cipher2index in range(cipher1index + 1, len(current_cipher)):
				hex1 = current_cipher[cipher1index][i: i + 2]
				hex2 = current_cipher[cipher2index][i: i + 2]
				if hasSpace(int(hex1, 16) ^ int(hex2, 16)):
					key[int(i / 2)].append(hex(int(hex1, 16) ^ ord(' '))[2:])
					key[int(i / 2)].append(hex(int(hex2, 16) ^ ord(' '))[2:])

def remove_key_not_alpha():
	global key
	global ciphertexts
	for i in range(len(key)):
		index_cipher = 2 * i
		current_cipher = [c for c in ciphertexts if len(c) > index_cipher]
		for cipher in current_cipher:
			hex1 = cipher[index_cipher : index_cipher + 2]
			for k in key[i]:
				if chr(int(k, 16) ^ int(hex1, 16)) in to_remove:
					key[i].remove(k)

def xor_two_messages(m1, m2):
	# longest messge should be the first one
	if len(m1) < len(m2):
		m1, m2 = m2, m1
	result = ''
	for i in range(0, len(m2), 2):
		result += hex(int(m1[i: i + 2], 16) ^ int(m2[i: i + 2], 16))[2:]
	return result

def decode_message(cipher, key):
	message = xor_two_messages(key, cipher)
	message_str = ''
	for i in range(0, len(message), 2):
		message_str += chr(int(message[i: i + 2], 16))
	return message_str
		

if __name__ == '__main__':
	try_get_key()
	key = [list(set(k)) for k in key]
	remove_key_not_alpha()
	possible_key = ''
	for el in key:
		if len(el) == 0:
			possible_key += '00'
			continue
		possible_key += el[0]
	for cipher in ciphertexts:
		print(decode_message(cipher, possible_key))
	# num_possible_keys = 1
	# print(key)
	# for el in key:
	# 	if len(el) > 0:
	# 		num_possible_keys *= len(set(el))
	# print(num_possible_keys)