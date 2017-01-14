import cv2

class Camera(object):
    """Get one frame from camera."""

    video_capture = None

    def __init__(self):
        self.open_camera()

    def __encode_frame__(self, frame):
        return cv2.imencode('.jpg', frame)[1].tostring()

    def __html_response_from_frame__(self, encoded_frame):
        return (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + encoded_frame + b'\r\n')

    def open_camera(self):
        self.video_capture = cv2.VideoCapture(0)

    def get_frame(self):
        if self.video_capture is not None and self.video_capture.isOpened(): # try to get the first frame
            status, frame = self.video_capture.read()
            if status:
                yield self.__html_response_from_frame__(self.__encode_frame__(frame))

        while True:
            if video_capture is None:
                yield None
            status, frame = self.video_capture.read()
            if status:
                yield self.__html_response_from_frame__(self.__encode_frame__(frame))

        self.close_camera()
        yield None

    def close_camera(self):
        self.video_capture.release()
        self.video_capture = None
