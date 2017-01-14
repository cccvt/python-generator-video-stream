import cv2

class Camera(object):
    """Get one frame from camera."""

    video_capture = None

    def __init__(self):
        self.open_camera()

    def __encode_frame__(self, frame):
        return cv2.imencode('.jpg', frame)[1].tostring()

    def open_camera(self):
        self.video_capture = cv2.VideoCapture(0)

    def get_frame(self):
        if self.video_capture is not None and self.video_capture.isOpened(): # try to get the first frame
            status, frame = self.video_capture.read()
            if status:
                yield self.__encode_frame__(frame)
        else:
            rval = False

        while True:
            # Capture frame-by-frame
            status, frame = self.video_capture.read()
            if status:
                yield self.__encode_frame__(frame)

        yield None

    def close_camera(self):
        self.video_capture.release()
        self.video_capture = None
