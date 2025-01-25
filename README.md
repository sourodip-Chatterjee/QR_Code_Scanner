## QR Code Scanner

A simple and efficient QR Code Scanner built using Python. This application uses the computer's webcam to scan and decode QR codes in real time. It is perfect for personal use or as a starting point for integrating QR code scanning functionality into larger projects.
 
---

## Features

- **Real-Time Scanning**: Utilizes the webcam to capture and decode QR codes.
- **Polygon Visualization**: Draws a green polygon around detected QR codes.
- **Decoded Text Display**: Displays the decoded data near the QR code.
- **User-Friendly Interface**: Press 'q' to exit the scanner.

---

## Requirements

Ensure you have Python installed on your system. Then, install the required libraries:

```bash
pip install opencv-python pyzbar
```

---

## Usage

1. Clone or download this repository to your local machine.
2. Navigate to the project directory.
3. Run the script:

   ```bash
   python qr_code_scanner.py
   ```

4. Point your webcam at a QR code.
5. The decoded data will appear on the screen and in the terminal.
6. Press 'q' to exit the scanner.

---

## Code Overview

### **Main Functionality**

- **Webcam Initialization**:
  - Captures frames using OpenCV's `cv2.VideoCapture(0)`.

- **QR Code Detection and Decoding**:
  - `pyzbar.decode(frame)` identifies QR codes and extracts their data.

- **Visualization**:
  - Draws a green polygon around detected QR codes.
  - Displays the decoded data near the QR code.

- **Exit Mechanism**:
  - Press 'q' to stop the scanner and release the webcam.

---

## Enhancements (Optional)

Feel free to extend the functionality:

1. **Save Scanned Data**: Store the decoded QR code data in a text file or database.
2. **API Integration**: Automatically open URLs or trigger actions based on the scanned data.
3. **Image Support**: Add the ability to decode QR codes from static images.
4. **Cross-Platform Deployment**: Package the script as an executable using tools like `PyInstaller`.

---

## Example Output

When a QR code is detected, the decoded data is displayed both on the terminal and near the QR code in the video feed:

```
QR Code Data: https://example.com
```

