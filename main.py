import cv2
import mediapipe as mp

# ---- STEP 1: Try to detect a working camera across all backends ----
backends = [
    ("DSHOW", cv2.CAP_DSHOW),
    ("MSMF", cv2.CAP_MSMF),
    ("ANY", cv2.CAP_ANY),
]

cap = None
for name, backend in backends:
    for index in range(3):
        print(f"Trying {name} backend, camera index {index}...")
        test_cap = cv2.VideoCapture(index, backend)
        if test_cap.isOpened():
            ret, frame = test_cap.read()
            if ret and frame is not None:
                cap = test_cap
                print(f"✅ Using camera index {index} with {name} backend")
                break
            else:
                print(f"   Opened but no frame from {name} index {index}")
                test_cap.release()
        else:
            print(f"   Could not open {name} index {index}")
    if cap is not None:
        break

# ---- STEP 2: If no camera found, exit with clear instructions ----
if cap is None:
    print("\n❌ No camera detected by OpenCV.")
    print("This is a SYSTEM issue, not a code issue.")
    print("Try these in order:")
    print("  1. Restart your PC")
    print("  2. Close all camera-using apps (Zoom, Teams, Discord, OBS, browsers)")
    print("  3. Windows Settings -> Privacy & security -> Camera ->")
    print("     Turn ON 'Let desktop apps access your camera'")
    print("  4. Disable antivirus 'Webcam Shield' / 'Camera Protection'")
    print("  5. Check Device Manager for camera driver issues")
    print("  6. Run: python -m cv2_enumerate_cameras")
    raise SystemExit(1)

# ---- STEP 3: Set up MediaPipe Hands ----
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5,
)
mp_draw = mp.solutions.drawing_utils

# ---- STEP 4: Main loop ----
print("Camera running. Press 'q' in the window to quit.")
while True:
    success, img = cap.read()
    if not success or img is None:
        continue

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_landmark in results.multi_hand_landmarks:
            h, w, _ = img.shape
            for id, lm in enumerate(hand_landmark.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                cv2.circle(img, (cx, cy), 4, (0, 0, 255), cv2.FILLED)

            mp_draw.draw_landmarks(img, hand_landmark, mp_hands.HAND_CONNECTIONS)

    cv2.imshow('Image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
# update 6

# update 7

# update 10

# update 11

# refactor 2

# refactor 3

# refactor 4

# refactor 5

# refactor 10

# refactor 12

# refactor 13

# refactor 15

# refactor 17

# refactor 20

# refactor 21

# refactor 22

# refactor 27

# refactor 29

# refactor 30

# refactor 32

# refactor 39

# refactor 40

# refactor 47

# refactor 48

# refactor 50

# refactor 52

# refactor 53

# refactor 54

# refactor 58

# refactor 59

# refactor 60

# refactor 63

# refactor 64

# refactor 65
