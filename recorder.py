import cv2
import time
import settings

class Recorder:
    def __init__(self, save_fname):
        self.vid = cv2.VideoCapture(settings.CAMERA_ID)
        self.save_fname = save_fname
        self.start_time = time.time()
        self.stop = False
        self.save = False
        self.frame_width = int(self.vid.get(3))
        self.frame_height = int(self.vid.get(4))
        self.vid_out = cv2.VideoWriter(save_fname + '.avi',
                                 cv2.VideoWriter_fourcc(*'MJPG'),
                                 60, (self.frame_width, self.frame_height))
        self.times_out = []

    def record(self, save_delay):
        while True:
            ret, frame = self.vid.read()
            print(time.time() - self.start_time)
            if self.save:
                self.times_out.append(time.time() - self.start_time)
                self.vid_out.write(frame)
            else:
                self.save = (time.time() - self.start_time) > save_delay
            
    
    def end(self):
        self.save = False
        self.vid_out.release()
        open(self.save_fname + '.json', 'w').write(str(self.times_out))
        self.vid.release()
        

if __name__ == '__main__':
    cam = Recorder('results/test')
    cam.record(1)
    cam.end()