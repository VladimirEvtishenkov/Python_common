# Установка обратного порядка байтов в массиве

def reverse_bytes(in_bytes):
    out_bytes = bytearray(in_bytes)
    out_bytes.reverse()
    return bytes(out_bytes)