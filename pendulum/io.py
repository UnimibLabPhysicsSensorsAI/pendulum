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

def video_capture(name, camera=0, record_duration=None):
    # Initialize video capture object
    cap = cv2.VideoCapture(camera)  # Use 0 for the default camera, or provide the index of the camera you want to use

    # Check if video capture object is successfully initialized
    if not cap.isOpened():
        print("Error: Couldn't access the camera.")
        exit()

    # Get the default frame size
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'MP4V')  # You can also use other codecs like 'MJPG', 'DIVX', 'X264', etc.
    out = cv2.VideoWriter(name+'.mp4', fourcc, 20.0, (frame_width, frame_height))

    # Record the video
    if record_duration is None:
        print('Starting Video Capture. Press "q" to stop recording.')
    end_time = None
    start_time = time.time()
    if record_duration is not None:
        end_time = start_time + record_duration
    while cap.isOpened() and time.time() <= end_time if end_time is not None else True:
        ret, frame = cap.read()

        # If frame is read properly
        if ret == True:
            # Write the frame into the video file
            out.write(frame)

            # Display the resulting frame
            cv2.imshow('Frame', frame)

            # Break the loop when 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    # Release everything when done
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    return

def saveVideo(frames, path, fps=29):
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    size = (frames[0].shape[1], frames[0].shape[0])
    out = cv2.VideoWriter(path, fourcc, fps, size)
    for frame in frames:
        out.write(frame)
    out.release()