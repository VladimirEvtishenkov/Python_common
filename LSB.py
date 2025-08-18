def calc_LSB(MSB, start_bits, end_bits):
    """
    Назначение: Реализация расчёта цены младшего разряда (ЦМР).

    Входные параметры: MSB - Цена старшего разряда (ЦСР);
                       start_bits - Начало занимаемого разряда;
                       end_bits - Конец занимаемого разряда.

    Выходные параметры: LSB - ЦМР.
    """
    bits = end_bits - start_bits
    LSB = MSB / (2 ** bits)
    return LSB
