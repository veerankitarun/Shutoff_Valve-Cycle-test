import serial
import time

# Set the COM port and baud rate
com_port = 'COM3'
baud_rate = 9600

try:
    # Open the serial port
    ser = serial.Serial(com_port, baud_rate)
    print(f"Connected to {com_port} at {baud_rate} baud")

    # Prompt the user for the number of cycles
    num_cycles = int(input("Enter the number of cycles: "))

    cycles_completed = 0

    while cycles_completed < num_cycles:
        # Send the 'AT+TVALVE=0' command to open the valve (ON)
        ser.write(b'AT+TVALVE=0\r\n')

        # Wait for the 'OK' response
        time.sleep(3)
        response = ser.read(ser.in_waiting).decode('utf-8')
        if 'OK' in response:
            # Send the 'AT+TVALVE=1' command to close the valve (OFF)
            ser.write(b'AT+TVALVE=1\r\n')

            # Wait for the 'OK' response
            time.sleep(2)
            response = ser.read(ser.in_waiting).decode('utf-8')
            if 'OK' in response:
                cycles_completed += 1
                print(f"Cycle {cycles_completed}/{num_cycles} completed")

    # Close the serial port
    ser.close()
    print("Serial port closed")

except serial.SerialException as e:
    print(f"Error: {e}")
except KeyboardInterrupt:
    print("Operation canceled by the user")
