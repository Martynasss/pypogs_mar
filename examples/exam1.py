import sys
import time
#from PIL import Image

sys.path.append('..')

import pypogs
from pathlib import Path
import tifffile
import matplotlib.pyplot as plt
from tetra3 import get_centroids_from_image

# For testing image
# myImage = tifffile.imread("img1.tiff")
# myImage = myImage[:,:,1]  #leave only one channel
# tifffile.imshow(myImage)
# plt.imshow(myImage, cmap='gray')
# plt.show()

# Create a camera instance (see pypogs.camera.Camera)
cam = pypogs.Camera(model='ptgrey', identity='18285284', name='CoarseCam')

# COARSE/STAR
cam.exposure_time = 1  # 450
cam.gain = 0
cam.frame_rate = 4
cam.binning = 2
# cam.plate_scale = 20.3
cam.plate_scale = 1
cam.start()
img = cam.get_latest_image()


# Create a TrackingThread instance
tt = pypogs.TrackingThread(camera=cam, name='CoarseTrackThread')

tt.goal_x_y = [0, 0]   #goal is center of image
tt.spot_tracker.max_search_radius = 500
tt.spot_tracker.min_search_radius = 200
tt.spot_tracker.crop = (256, 256)
tt.spot_tracker.spot_min_sum = 500
tt.spot_tracker.bg_subtract_mode = 'local_median'
tt.spot_tracker.sigma_mode = 'local_median_abs'
tt.spot_tracker.fails_to_drop = 10
tt.spot_tracker.smoothing_parameter = 8
tt.spot_tracker.rmse_smoothing_parameter = 8
tt.feedforward_threshold = 10
tt.img_save_frequency = 1

# Set up tracking parameters (see SpotTracker in this module for details)
tt.spot_tracker.position_max_sd = 100
tt.spot_tracker.position_min_sd = 20
tt.spot_tracker.position_sigma = 5
# (Optional) set up a directory for image saving at .5 Hz
tt.image_folder = Path('./tracking_images')
tt.img_save_frequency = 0.5


# Start the tracker
tt.start()

# myImage = cam.get_latest_image()
# tifffile.imshow(myImage)
# time.sleep(1)  # Wait for a while

# LOOP
i = 0
while i<100:
    time.sleep(0.5)    # Wait for a while
    print(tt.track_alt_az)    # Read the position in arcsec (plate scale is 20.3)
    i = i+1


# Stop the tracker
tt.stop()
# Deinitialise the camera
cam.deinitialize()
