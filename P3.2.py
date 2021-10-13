import binascii

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

target = ciphertexts[0]
length = len(ciphertexts)

# Convert hexadecimal digits to asscii corresponding characters
ciphertexts = [binascii.unhexlify(x) for x in ciphertexts]

# This method allows XOR operations on hexadecimal strings directly
def strxor(a, b):     # xor two strings of different lengths
    return "".join([chr(x ^ y) for x, y in zip(a, b)])

# The XOR operation is performed on each character in the string, so the string to be operated on must be divided into one form before use.
# The first method was used here, but the key s that were obtained were discarded as if they could not be converted to numbers.
def stror1(a, b):
    if len(a) > len(b):
       return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
       return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

def find_letter(s):
    #Returns the position of a given letter in a given string
    position = []
    for index in range(len(s)):
        #There may be more cases where whitespace is odd or zero
        if (s[index] >= 'A' and s[index] <= 'Z') or (s[index] >= 'a' and s[index] <= 'z') or s[index] == chr(0):
            # space_counts[index] += 1
            position.append(index)
    return position

# Possibility of calculating space position
def space_possibility(s):
    space_new = []
    for position in range(400):
        count = 0
        for idx_i in range(length - 1):
            if position in s[idx_i]:
                count += 1
        if count > 7:  # If the XOR suffix occurs more than seven times, the plain text is considered a space
            space_new.append(position)
    return space_new

# Location where possible space characters were found
def find_space(ciphertexts):
    space_possib = []  # Used to save possible spaces
    # Using double loops to achieve double exclusive or
    for ciphertext_i in ciphertexts:
        space = []  # Used to save possible spaces
        for ciphertext_j in ciphertexts:
            # Do not disagree with yourself or
            if ciphertext_i == ciphertext_j:
                continue
            xor_res = strxor(ciphertext_i, ciphertext_j)
            # Record the position of possible space characters in each plaintext
            space.append(find_letter(xor_res))
        # Making a Possibility Judgment of Spaces Position
        space_possib.append(space_possibility(space))
    return space_possib

#Compute to get corresponding Key
def cal_key(cipher):
    space_possib = find_space(cipher)
    key = [0] * 200  #Store key
    for cipher_idx in range(length):
        for position in range(len(space_possib[cipher_idx])):
            idx = space_possib[cipher_idx][position] #Hexadecimal, expressed in 2 bits
            a = cipher[cipher_idx][idx]
            key[space_possib[cipher_idx][position]] = a ^ ord(" ") # Compute the key to get the result decimal (ascii code)

    key_str = "" #Empty String for Keys
    for k in key:
        key_str += chr(k)#translate into
    return key_str  #Get Key String

if __name__ == '__main__':
    # space_possib = find_space(ciphertexts)
    key = cal_key(ciphertexts)
    result = ""
    f = ''.join([chr(int(d, 16)) for d in [target[i:i + 2] for i in range(0, len(target), 2)]])
    for letter in stror1(f, key):
            result += letter
    print(result)