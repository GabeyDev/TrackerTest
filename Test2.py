import socket
import datetime
import struct

def decode_hex_data():
    hex_data = input("Please enter your data: ")
    data_bytes = bytes.fromhex(hex_data)

    if len(data_bytes) < 8:
        print("Unable to read your data correctly, please restart and try again.")
        return

    start_bit = data_bytes[0:2]
    length = len(data_bytes) - 5 
    protocol_number = int.from_bytes(data_bytes[3:4], byteorder='big')
    device_id = data_bytes[5:12]
    information_serial_number = int.from_bytes(data_bytes[13:14], byteorder='big')
    error_check = int.from_bytes(data_bytes[15:16], byteorder='big')
    end_bit = data_bytes[16:18]  

    print("Start Bit:", start_bit.hex())
    print("Length:", length)
    print("Protocol Number:", protocol_number)
    print("Device ID:", device_id.hex())
    print("Information Serial Number:", information_serial_number)
    print("Error Check:", error_check)
    print("End Bit:", end_bit.hex())

def decode_hex_data_protocol(protocol_number):
    hex_data = input("Please enter your data: ")
    data_bytes = bytes.fromhex(hex_data)

    if len(data_bytes) < 9:
        print("Unable to read your data correctly, please restart and try again.")
        return

    start_bit = data_bytes[0:2]
    length = len(data_bytes) - 5

    match protocol_number:
        case 1:
            # Handle protocol 1
            gps_information = {
                "date_time": data_bytes[5:10],
                "quantity_GPS_satellites": data_bytes[11:12],
                "latitude": data_bytes[13:16],
                "longitude": data_bytes[17:20],
                "speed": data_bytes[21:22],
                "course_status": data_bytes[23:25]
            }
            print("GPS Information:", gps_information)
        case 2:
            # Handle protocol 2
            status_information = {
                "device_information": data_bytes[5:6],
                "battery_voltage_level": data_bytes[7:8],
                "GSM_signal_strength": data_bytes[9:10],
                "external_voltage": data_bytes[11:12],
                "language": data_bytes[13:14],
            }
            print("Status Information:", status_information)
        case 3:
            # Handle protocol 3
            pass  # Add implementation for protocol 3
        case _:
            print("Unknown protocol number.")

if __name__ == "__main__":
    decode_hex_data()
