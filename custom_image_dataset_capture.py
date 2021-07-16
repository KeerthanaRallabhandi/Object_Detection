
import cv2   #importing opencv library

def capture_object():
    #creating an objecte called camera, of type openCV video capture, using the first camera in the list of cameras connected to the computer
    camera = cv2.VideoCapture(0)
    camera.set(cv2.CAP_PROP_FRAME_WIDTH,1280)   #creating a frame window of required size
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
    '''starting point and ending point of roi'''
    upper_left = (25,10)    #creating a coordinate rectangular bounding region of interest inside the frame to capture the object with the image ratio 800*480
    bottom_right = (825,490)
    cv2.namedWindow("Image Capture")

    img_counter = 0 #counter to the captured number of images set to zero

    while img_counter<= 20:     #using a loop, to get each frame of webcam with the method read()
        status,frame = camera.read() # reading the frames
        if not status:
            print("failed to grab the frame")
            break
        r = cv2.rectangle(frame, upper_left, bottom_right, (800, 50, 400), 5)   #create a Region of Interest (ROI) inside a frame
        rect_img = frame[upper_left[1]: bottom_right[1], upper_left[0]: bottom_right[0]]    #Positioning of the image capture

        #if frames are apperaring then the imageshow frame, showing the webcam to the user
        cv2.imshow("Test",frame)    #show the frame

        # key press for capture and quit
        k = cv2.waitKey(1)  #delay capture of object

        if k%256 == 27:     #ASCII value of ESC key = 27
            print("Escape hit, CLosing the window")
            break

        elif k%256 == 32:   #ASCII value of SPACE key = 32
            img_cap = "E:\Technical docs\datacollect\Train_set\obj2\Bottles_{}.jpg".format(img_counter)     #image saving
            cv2.imwrite(img_cap,rect_img)
            print("image capturead")
            img_counter = img_counter + 1


    camera.release()    #shutdown the camera
    cv2.destroyAllWindows()

capture_object()
