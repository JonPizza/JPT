import sys
import cv2
import time

from pynput import keyboard

vid = cv2.VideoCapture(sys.argv[1] + '.mp4')
times_list = eval(open(sys.argv[1] + '.json').read())
amount_of_frames = int(vid.get(cv2.CAP_PROP_FRAME_COUNT) - 1)
curr_frame = 0

def save_result(hip, time):
    open(sys.argv[1] + '-final', 'a').write(f'{hip} : {time}')

def on_press(key):
    global curr_frame, frame
    try:
        k = key.char
    except:
        k = key.name 
    if k in ['left', 'right', 'up', 'down']: 
        if k == 'left' and curr_frame > 0:
            curr_frame -= 1
        elif k == 'right' and curr_frame <= amount_of_frames - 1:
            curr_frame += 1
        elif k == 'up' and curr_frame <= amount_of_frames - 10:
            curr_frame += 10
        elif k == 'down' and curr_frame > 9:
            curr_frame -= 10
        elif k == ',' and curr_frame > 99:
            curr_frame -= 100
        elif k == '.' and curr_frame <= amount_of_frames - 100:
            curr_frame += 100
        elif k == '1234567890abcdefhijklmnop': # Max 25 ppl/heat
            save_result(k.upper(), round(times_list[curr_frame], 2))
    return True

def main():
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    prev_frame = -1
    while True:
        vid.set(cv2.CAP_PROP_POS_FRAMES, curr_frame)
        if prev_frame != curr_frame:
            print(f'Frame: \t{curr_frame}/{amount_of_frames} | Time: {round(times_list[curr_frame], 2)}')
            prev_frame = curr_frame
        res, frame = vid.read()
        cv2.imshow('Race', frame)
        cv2.waitKey(1)

if __name__ == '__main__':
    main()