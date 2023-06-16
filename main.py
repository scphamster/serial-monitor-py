import serial
import sys
import click

def main():
    ser_port = serial.Serial('/dev/ttyUSB0', 115200)

    try:
        while True:
            line = ser_port.readline()
            print(line.decode('ascii'))

    except KeyboardInterrupt:
        print("Exit")

    finally:
        ser_port.close()


if __name__ == '__main__':
    main()
