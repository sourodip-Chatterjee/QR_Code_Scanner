import cv2
from pyzbar.pyzbar import decode

def qr_code_scanner():
    # Initialize the webcam
    cap = cv2.VideoCapture(0)
    print("Press 'q' to exit the scanner.")

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        if not ret:
            print("Failed to grab frame.")
            break

        # Detect and decode QR codes
        decoded_objects = decode(frame)
        for obj in decoded_objects:
            data = obj.data.decode('utf-8')
            points = obj.polygon
            print(f"QR Code Data: {data}")

            # Draw a polygon around the QR code
            if len(points) > 4:
                hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
                points = hull
            else:
                points = np.array(points)

            # Draw bounding box
            for i in range(len(points)):
                pt1 = tuple(points[i])
                pt2 = tuple(points[(i + 1) % len(points)])
                cv2.line(frame, pt1, pt2, (0, 255, 0), 3)

            # Display decoded data above the QR code
            rect = obj.rect
            cv2.putText(frame, data, (rect.left, rect.top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        # Display the frame with detected QR codes
        cv2.imshow("QR Code Scanner", frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    qr_code_scanner()
