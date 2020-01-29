from pymodbus.client.sync import ModbusSerialClient
client = ModbusSerialClient(method='rtu', port="/dev/tty.your_tty", timeout=1, baudrate=9600)
res = client.read_holding_registers(0x00, 1, unit=0x01)

def scan_holding(cantidad):
    values = [ client.read_holding_registers(address, 1,unit=0x01) for address in range(0, cantidad, 2) ]
    for i in range(len(values)):
        try:
            print(f"{values[i].registers[0]}")
        except:
            print("not a value")
    return values

def scan_input(cantidad):
    values = [ client.read_input_registers(address, 1,unit=0x01)  for address in range(0, cantidad, 2) ]
    for i in range(len(values)):
        try:
            print(f"{values[i].registers[0]}")
        except:
            print("not a value")

    return values
