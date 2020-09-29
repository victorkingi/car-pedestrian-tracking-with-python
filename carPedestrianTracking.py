import cv2

# Our image
img_file = 'index.jpeg'
video_car = cv2.VideoCapture('Tesla2.mp4')
video_pedestrian = cv2.VideoCapture('Pedestrians.mp4')

# pre-trained
classifier_file_car = 'car.xml'
classifier_file_pedestrian = 'pedestrian'

# create car classifier
car_tracker = cv2.CascadeClassifier(classifier_file_car)
pedestrian_tracker = cv2.CascadeClassifier(classifier_file_pedestrian)

# read forever until car stops/ crashes
while True:
    (read_successful, frame) = video_pedestrian.read()

    # Safe coding.
    if read_successful:
        # must convert to gray scale
        grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break

    # detect cars
    cars = car_tracker.detectMultiScale(grayscaled_frame)
    pedestrians = pedestrian_tracker.detectMultiScale(grayscaled_frame)

    # Draw rectangles around cars
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.rectangle(frame, (x + 1, y + 2), (x + w, y + h), (0, 0, 255), 2)

    for (x, y, w, h) in pedestrians:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.rectangle(frame, (x + 1, y + 2), (x + w, y + h), (0, 255, 255), 2)

    # display image
    # cv2.imshow('my car detector', frame)
    cv2.imshow('my pedestrian & car detector', frame)

    # don't autoclose
    key = cv2.waitKey(1)

    if key == 81 or key == 113:
        break

# clean up
video_pedestrian.release()

"""
# create opencv image
img = cv2.imread(img_file)

# convert to grayscale (needed for faster cascade)
black_n_white = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# create car classifier
car_tracker = cv2.CascadeClassifier(classifier_file)

# detect cars
cars = car_tracker.detectMultiScale(black_n_white)

# Draw rectangles around cars
for (x, y, w, h) in cars:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

# display image with faces spotted
cv2.imshow('my car detector', img)

# don't autoclose wait here listen for key press
cv2.waitKey()
"""
