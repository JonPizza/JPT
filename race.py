import os
import sys
import socket
import time

from recorder import Recorder

s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s1.bind(('0.0.0.0', 5050))

s1.listen(5)

delays = {
    '100m': 6,
    '200m': 16,
    '400m': 40,
    '800m': 100,
    '1600m': 60 * 3.5,
    'mile': 60 * 3.5,
    '3200m': 60 * 7.5,
    '2mile': 60 * 7.5,
}


def main():
    if len(sys.argv) == 1:
        print(f'Usage:\np {sys.argv[0]} <distance> <heat #>')
        exit()
    dist = sys.argv[1].lower()
    heat = sys.argv[2]
    cam = Recorder(f'results/{dist}/{heat}')
    print(dist + ' Heat ' + heat)

    if dist not in delays:
        delays[dist] = 0  # assume 0 delay, just in case

    os.system(f'mkdir -p results/{dist}')
    print('Waiting for socket connection to start...')
    conn, addr = s1.accept()
    r = conn.recv(1024)
    if r == b'Start!':
        print('Started!')
    else:
        print('ERROR??? Recieved ' + str(r) + ', starting timing anyways')
    cam.start_time = time.time()
    conn.close()
    s1.shutdown(socket.SHUT_RDWR)
    s1.close()
    try:
        cam.record(delays[dist])
    except KeyboardInterrupt:
        cam.end()
    print(f'Output directory: results/{dist}/{heat}')


if __name__ == '__main__':
    main()