import cv2
import mediapipe as mp
import time

class poseDectector():
    def __init__(self, mode=False, maxHands = 2,modelC = 1, detectionCon = 0.5, trackCon = 0.5 ):
        self.mode = mode
        self.maxHands = maxHands
        self.modelC = modelC
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose()
        self.mpDraw = mp.solutions.drawing_utils
        
    def findPose(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)


while True:
    
    
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            cx, cy = int(lm.x*w), int(lm.y*h)
            cv2.circle(img, (cx, cy), 10, (255, 0, 0), cv2.FILLED)
    


def main():
    pTime = 0
    cap = cv2.VideoCapture('Chapter 2/poseVideos/media5.mp4')
    detector = poseDectector()
    while True:
        success, img = cap.read()
        
        
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
    
        cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        cv2.imshow("Image", img)
        cv2.waitKey(1)
    
if __name__ == "__main__":
    main()