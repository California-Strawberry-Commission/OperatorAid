import serial, sys, time
port = sys.argv[1] if len(sys.argv) > 1 else 'COM5'
secs = float(sys.argv[2]) if len(sys.argv) > 2 else 12.0
s = serial.Serial()
s.port = port
s.baudrate = 115200
s.timeout = 0.3
s.dtr = True
s.rts = False
s.open()
time.sleep(0.5)
s.reset_input_buffer()
end = time.time() + secs
while time.time() < end:
    d = s.read(4096)
    if d:
        sys.stdout.buffer.write(d)
        sys.stdout.flush()
s.close()
