import cv2
import datetime

cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)

frame_count = 0

print("Relay overlay test starting...")
print("Press Q to quit")

while True:
    ret, frame = cap.read()

    if not ret:
        print("Camera not found")
        break

    frame_count += 1

    height, width, channels = frame.shape

    timestamp = datetime.datetime.now().strftime("%H:%M:%S")

    cv2.putText(
        frame,
        "Relay scanning...",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

    cv2.putText(
        frame,
        f"Resolution: {width}x{height}",
        (20, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 255),
        1
    )

    cv2.putText(
        frame,
        f"Frame: {frame_count}",
        (20, 110),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 255),
        1
    )

    cv2.putText(
        frame,
        timestamp,
        (20, 140),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (200, 200, 200),
        1
    )

    cv2.imshow("Relay - Overlay Test", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print(f"Relay closed. Total frames processed: {frame_count}")