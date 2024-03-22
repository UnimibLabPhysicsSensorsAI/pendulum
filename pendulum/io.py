import cv2, time

try:
    import picamera2
    from picamera2 import Picamera2

    def initialise_camera():
        """Initialise the camera."""
        camera = Picamera2()
        camera.configure("still")
        camera.start()
        time.sleep(1)
        camera.set_controls({"AeEnable": False, "AwbEnable": False, "FrameRate": 1.0})
        # And wait for those settings to take effect
        time.sleep(1)
        return camera
    
    def acquire_image(name, camera=None):
        """Acquire an image from the picamera."""
        if camera is None:
            camera = initialise_camera()
        # capture
        r = camera.capture_request()
        r.save("main", name)
        r.release()
        return 
    
    def close_camera(camera):
        """Close the camera."""
        camera.stop()
        return
    
except ImportError:
    print("Picamera2 is not available. The related functions are not defined.")

def load_image(name, color_conversion=cv2.COLOR_BGR2RGB):
    """ Load an image from a file and convert it to RGB"""
    loaded_image = cv2.imread(name)
    loaded_image_conv = cv2.cvtColor(loaded_image, color_conversion)
    return loaded_image_conv

def save_image(frame, name):
    """ Save an image to a file."""
    cv2.imwrite(name, frame)
    return

