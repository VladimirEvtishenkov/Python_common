# Расчёт CRC-6

def crc6(bits, poly=0x1B, init=0x3F):
    crc = init
    for bit in bits:
        # Извлекаем старший (5-й) бит текущего CRC и делаем XOR с входящим битом
        bit_in = bit ^ ((crc >> 5) & 1)
        # Сдвигаем CRC влево на 1 бит и ограничиваем 6 битами
        crc = (crc << 1) & 0x3F
        # Если входящий бит после XOR равен 1, применяем полином
        if bit_in:
            crc ^= poly
    return crc
