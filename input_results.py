import sys

fname = sys.argv[1] + '-final'

try:
    open(fname).read()
    print('Opening existing file')
except:
    open(fname, 'w').write('Hip or name: Time')
    print('Started new file')

with open(fname, 'a') as f:
    while True:
        hip_or_name = input('Hip or name: ')
        time = input('Time: ')
        f.write(f'{hip_or_name}: {time}\n')
        print('-- Got it ✓ --')