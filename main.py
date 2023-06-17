import serial
import click


@click.command()
@click.option('--port', '-p',
              prompt='Serial device',
              help='Enter serial device to listen to, e.g. /dev/ttyUSB0',
              required=True)
@click.option('--baud', '-b', prompt='Baudrate', help='Set a baudrate, e.g. 115200', type=int)
def start_serial(port, baud):
    ser_port = serial.Serial(port, baud)

    try:
        while True:
            line = ser_port.readline()
            print(line.decode('ascii'))

    except KeyboardInterrupt:
        print("Exit")

    finally:
        ser_port.close()