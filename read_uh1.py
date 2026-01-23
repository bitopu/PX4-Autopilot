import socket
import struct

# Configuration (Must match the JSBSim XML)
UDP_IP = "172.19.32.1" # localhost
UDP_PORT = 5150

# 1. Create the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print(f"Listening for JSBSim data on {UDP_IP}:{UDP_PORT}...")

try:
    while True:
        # 2. Receive data (buffer size 1024 bytes is usually enough)
        data, addr = sock.recvfrom(1024) 
        
        # 3. Decode the bytes to string
        # JSBSim sends text like: "time_val, alt_val, pitch_val, roll_val\n"
        raw_string = data.decode('utf-8').strip()
        
        # 4. Split into a list of values
        values = raw_string.split(',')

        time = float(values[0])
        throttle_pos_0 = float(values[1])
        collective_cmd = float(values[2])
        aileron_cmd = float(values[3])
        elevator_cmd = float(values[4])
        rudder_cmd = float(values[5])
        active_engine = float(values[6])
        starter_cmd = float(values[7])
        fuel_flow = not float(values[8])
        n1 = float(values[9])
        print(f"Time: {time:.2f} s, Throttle Pos 0: {throttle_pos_0:.2f}, Collective Cmd: {collective_cmd:.2f}, Aileron Cmd: {aileron_cmd:.2f}, Elevator Cmd: {elevator_cmd:.2f}, Rudder Cmd: {rudder_cmd:.2f}, Active Engine: {active_engine:.2f}, Starter Cmd: {starter_cmd:.2f}, Fuel Flow: {fuel_flow:.2f}, N1: {n1:.2f}")
except KeyboardInterrupt:
    print("\nStopping...")
    sock.close()
