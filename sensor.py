#!/usr/local/bin/python

import mraa

a_gas_port = 0
d_gas_port = 2

def main():
    input_port = mraa.Aio( a_gas_port )
    print( input_port.read() )

if __name__ == '__main__':
    main()
