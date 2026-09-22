import cv2
import numpy as np

# Open the webcam
cap = cv2.VideoCapture(0)

# Check if camera is opened
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    # Read frame from camera
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame.")
        break

    # Convert BGR image to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define lower and upper range for BLUE
    lower_blue = np.array([100, 100, 100])
    upper_blue = np.array([140, 255, 255])

    # Create mask for blue colour
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Find contours of blue objects
    contours, _ = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    # Draw rectangle around detected blue objects
    for contour in contours:
        area = cv2.contourArea(contour)

        if area > 500:
            x, y, w, h = cv2.boundingRect(contour)

            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (255, 0, 0),
                2
            )

            cv2.putText(
                frame,
                "BLUE",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 0, 0),
                2
            )

    # Display camera frame
    cv2.imshow("Blue Colour Detection", frame)

    # Display mask
    cv2.imshow("Blue Mask", mask)

    # Press q to exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release camera
cap.release()

# Close all windows
cv2.destroyAllWindows()