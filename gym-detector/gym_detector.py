import cv2
import mediapipe as mp

# set mediapipe
mp_drawing = mp.solutions.download_utils
mp_pose = mp.solutions.pose

# CV2 Parameters
cap = cv2.VideoCapture(0)
# Set the desired frame width and height
frame_width = 400
frame_height = 400

# Set the frame width and height for the video capture object
cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)


# Check cam is open or not
if not cap.isOpened():
    print("Failed to open webcam")
    exit()


## Setup mediapipe instance
with mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5,
) as pose:
    # Set Webcam using OpenCV2
    while True:
        ret, frame = cap.read()

        if not ret:
            print("Failed to capture frame")
            break

        # horizontal flip of webcam
        frame = cv2.flip(frame, 1)

        # Detection Stuff
        # recolor the image
        image = cv2.cvtColor(flipped_frame, cv2.COLOR_BG2BGR)
        image.flags.writeable = False

        # Make detections
        results = pose.process(image)

        # Rerender using CV2 -> recolor the RGB
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        print(results)

        # Perform any desired image processing or display the frame
        cv2.imshow("Webcam", frame)

        # Exit the loop if 'q' is pressed
        if cv2.waitKey(1) == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()
