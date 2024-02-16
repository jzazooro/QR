from pyzbar.pyzbar import decode
import cv2

def read_qr_code(image_path):
    # Load the image using OpenCV
    image = cv2.imread(image_path)

    # Use pyzbar's decode method to detect the QR code
    decoded_objects = decode(image)
    
    if decoded_objects:
        # Print the type and data of each decoded object
        for obj in decoded_objects:
            print('Type:', obj.type)
            print('Data:', obj.data.decode('utf-8'))
    else:
        print('No QR code found.')

# Replace 'path_to_your_image.png' with the path to your QR code image
read_qr_code('flag.png')
