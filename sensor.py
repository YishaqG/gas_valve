#!/usr/local/bin/python

import mraa
from lib.Servo import Servo

a_gas_port = 0
d_gas_port = 2

def main():
    # while True:
    #     input_port = mraa.Aio( a_gas_port )
    #     print( sample(input_port) )

    i = 0
    servo = Servo(3)
    while i < 180:
        servo.write(i)
        i += 5

def sample( input_port ):
    max_range_value = 100
    result = 0
    for i in range(0, max_range_value):
        result += input_port.read()

    return result / max_range_value

if __name__ == '__main__':
    main()
