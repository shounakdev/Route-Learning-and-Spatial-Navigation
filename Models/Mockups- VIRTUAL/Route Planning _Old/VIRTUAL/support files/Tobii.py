#The following example shows how to connect to the Tobii eye tracker:

# Create the Tobii extension 
tobii = viz.add('tobii.dle')

# Connect to Tobii eye tracker
eyeTracker = tobii.addEyeTracker()

#The next example shows how to get the gaze vector and perform an intersection test to determine where the user is looking:

# Get gaze matrix in local HMD coordinate system 
gazeMat = eyeTracker.getMatrix()

# Transform gaze matrix into world coordinate system using main view
gazeMat.postMult(viz.MainView.getMatrix())

# Intersect world gaze vector with scene
line = gazeMat.getLineForward(1000)
info = viz.intersect(line.begin, line.end)
if info.valid:
    print('User is looking at', info.point)
###################################################################################################################################
###################################################################################################################################