import codecs
import base64

def hex_to_base64(hex):
    raw_bytes = bytes.fromhex(hex)
    return base64.b64encode(raw_bytes).decode()

if __name__ == '__main__':
    hex = '7468657265206973206d6f726520746f206c696665207468616e20626f6f6b732c20627574206e6f74206d756368206d6f7265'
    bytes1 = bytes.fromhex(hex)
    base64_str = 'NzQ2ODY1NzI2NTIwNjk3MzIwNmQ2ZjcyNjUyMDc0NmYyMDZjNjk2NjY1MjA3NDY4NjE2ZTIwNjI2ZjZmNmI3MzJjMjA2Mjc1NzQyMDZlNmY3NDIwNmQ3NTYzNjgyMDZkNmY3MjY1'
    bytes2 = base64.b64decode(base64_str)
    print(bytes1 == bytes2)