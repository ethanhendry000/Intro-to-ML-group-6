import cv2
import cv2.aruco as aruco

# EVERYTHING IN QUOTES IS JUST TESTING/MAIN LOOP LOGIC

'''
# Initialize ArUco and camera
aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
parameters = aruco.DetectorParameters()
# Change this to actual input camera. Right now it's just webcam
cap = cv2.VideoCapture(0)
'''

# Actual function to use in main loop
def get_robot_position(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    corners, ids, _ = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
    
    # Check if at least one marker was found
    if ids is not None:
        marker_corners = corners[0][0]
        
        # Center Calculation (Average of top left and bottom right)
        center_x = int((marker_corners[0][0] + marker_corners[2][0]) / 2)
        center_y = int((marker_corners[0][1] + marker_corners[2][1]) / 2)
        
        return (center_x, center_y)
    
    # We could change this to return last seen coordinates if it becomes too inconsistent
    return None


# Example loop to test it/how to structure our full program:
'''
while True:
    #ret, frame = cap.read()
    #if not ret:
        #break
    # Call function and get robot position coordinates
    pos = get_robot_position(frame)

    # If the robot is visible, do something with coords
    if pos is not None:
        # Unpack the tuple
        rx, ry = pos
        
        # Can display the coordinates on the video feed (optional)
        cv2.putText(frame, f"Robot: {rx}, {ry}", (20, 40), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
        # Crosshair/dot on robot (optional)
        cv2.drawMarker(frame, pos, (0, 0, 255), cv2.MARKER_CROSS, 20, 2)

        # Call whatever functions we create to send coords/results to robot or another function:

    # View results if need
    cv2.imshow('Lego Robot Tracking', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
'''
