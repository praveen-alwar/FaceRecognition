# import numpy as np
# import cv2

# # Open a sample video available in sample-videos
# vcap = cv2.VideoCapture('https://www.sample-videos.com/video123/mp4/720/big_buck_bunny_720p_1mb.mp4')

# # rtsp://<username>:<password>@<ip>:<port>/cam/realmonitor?channel=<channelNo>&subtype=<typeNo>
# # rtsp://<username>:<password>@<address>:<port>/Streaming/Channels/<id>/
# # rtsp://admin:pas12345@192.168.11.110:554/Streaming/Channels/202/

# if not vcap.isOpened():
#    print ("File Cannot be Opened")

# while True:
#     # Capture frame-by-frame
#     ret, frame = vcap.read()
#     #print cap.isOpened(), ret
#     if frame is not None:
#         # Display the resulting frame
#         clo = cv2.imshow('Video', frame)
#         # Press q to close the video windows before it ends if you want
#         if cv2.waitKey(22) & 0xFF == ord('q'):
#             break
#     else:
#         print ("Frame is None")
#         break

# # When everything done, release the capture
# vcap.release()
# cv2.destroyAllWindows()
# print("Video stopped")

import cv2

print("Before URL")
feed = cv2.VideoCapture('https://www.sample-videos.com/video123/mp4/720/big_buck_bunny_720p_1mb.mp4')

# rtsp://<username>:<password>@<ip>:<port>/cam/realmonitor?channel=<channelNo>&subtype=<typeNo>
# rtsp://<username>:<password>@<address>:<port>/Streaming/Channels/<id>/
# rtsp://admin:pas12345@192.168.11.110:554/Streaming/Channels/202/

print("After URL")

while True:

    # print('About to start the Read command')
    ret, frame = feed.read()
    # print('About to show frame of Video.')
    cv2.imshow("Vid", frame)
    # print('Running..')

    keyCode = cv2.waitKey(1)

    if cv2.getWindowProperty("Vid", cv2.WND_PROP_VISIBLE) < 1:
        break

feed.release()
cv2.destroyAllWindows()