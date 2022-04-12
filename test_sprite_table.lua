location = 0x009e
while True do
    value1 = memory.read_u8(location + 0)
    value2 = memory.read_u8(location + 1)
    value3 = memory.read_u8(location + 2)
    value4 = memory.read_u8(location + 3)
    value5 = memory.read_u8(location + 4)
    print(value1,value2,value3,value4,value5)
