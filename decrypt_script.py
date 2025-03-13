encrypted_hex = "encrypted_flag"
encrypted_bytes = bytes.fromhex(encrypted_hex)

def reverse_bit_rotation(byte):
    return ((byte >> 2) | (byte << 6)) & 0xFF

deobfuscated_bytes = bytes(reverse_bit_rotation(b) for b in encrypted_bytes)

key = session_key
flag = "".join(chr(deobfuscated_bytes[i] ^ (key + i % 5)) for i in range(len(deobfuscated_bytes)))
print("Decrypted Flag:", flag)
