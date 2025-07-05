import cv2
from object_detection import detect_objects
from scene_caption import generate_caption
from text_to_speech import speak

def main():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Cannot open camera")
        return

    print("Press 's' to describe the scene | Press 'q' to quit")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        cv2.imshow("Scene View", frame)

        key = cv2.waitKey(1)
        if key == ord('s'):
            print("Processing...")
            objects = detect_objects(frame)
            caption = generate_caption(frame)

            if objects:
                description = f"{caption}. I see: {', '.join(objects)}."
            else:
                description = caption

            speak(description)

        elif key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
