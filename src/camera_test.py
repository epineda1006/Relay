import cv2

cap = cv2.VideoCapture(0)

print("Relay camera test starting...") 
print("Press Q to quit") 

while True:
    ret, frame = cap.read()

    if not ret: 
        print("Camera not found")
        break

    cv2.imshow("Relay - Camera Feed", frame) 

    if cv2.waitKey(1) & 0xFF == ord('q'): 
       break

cap.release()
cv2.destroyAllWindows()
print("Camera closed")
