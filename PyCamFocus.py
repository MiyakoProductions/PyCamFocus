from pynput import keyboard
import cv2 # If you get an error, try installing OpenCV2 with: pip install opencv-python

# The hotkeys are set here. You can change the hotkey to any character.
# I used [ and ] which I bound the wheel on my Xencelab remote to.
def on_key_release(key):
    global focus_value

    if key == keyboard.KeyCode.from_char(']'):  # Right Square Bracket
        focus_value = min(focus_value + 5, 255)  # Increase focus value by 5
        cap.set(cv2.CAP_PROP_FOCUS, focus_value)
        print(f"Focus increased to {focus_value}") # Debug output, may be annoying to non-programmers

    elif key == keyboard.KeyCode.from_char('['):  # Left Square Bracket
        focus_value = max(focus_value - 5, 0)  # Decrease focus value by 5
        cap.set(cv2.CAP_PROP_FOCUS, focus_value)
        print(f"Focus decreased to {focus_value}") # Debug output, may be annoying to non-programmers

# Initialize the webcam
# You may need to change the number here if you have more than one webcam.
# I used OBS Studio's Video Capture Device source to see the list of cameras I had in numerical order.
cap = cv2.VideoCapture(0)

# Set the desired resolution and frame rate immediately after opening the webcam
# If the image appears stretched, try changing the aspect ratio.
# My webcam, a Razer Kiyo Pro, displayed best at 4:3 instead of 16:9
desired_width = 1440
desired_height = 1080
desired_fps = 30  # Adjust this value to your desired frame rate

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Set the resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH, desired_width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, desired_height)


# Set the frame rate
cap.set(cv2.CAP_PROP_FPS, desired_fps)

# Set initial focus value
focus_value = 128  # You can set this to your desired initial focus value
cap.set(cv2.CAP_PROP_AUTOFOCUS, 0)  # Disable autofocus
cap.set(cv2.CAP_PROP_FOCUS, focus_value)  # Set manual focus value

# Create a listener for key presses
listener = keyboard.Listener(on_release=on_key_release)
listener.start()

# Create a named window to allow resizing of the window.
# Resizing will also change the resolution of the webcam.
cv2.namedWindow("Webcam", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Webcam", desired_width, desired_height)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (desired_width, desired_height))
    cv2.imshow("Webcam", frame)

    # Quit the script if the window or terminal is active with "q" or any key you want.
    # Or do Control+C like me. :3
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the OpenCV window
cap.release()
cv2.destroyAllWindows()
