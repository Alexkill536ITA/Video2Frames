# Video2Frames 

Simple python script to convert a video file to frames as jpg files

### Usage : 

```
python video2frames.py input/video/file/path output/folder [--maxframes] [--rotate]
```

Options : 
	--maxframes : Max number of output frames (or files)
	--rotate : Rotate clock-wise output frames, possible values = {90, 180, 270}

### Example : 

Split video to frames files (max 250 files) and rotate 90 degress clock-wise 

```  
python video2frames.py /tmp/my_video.mpg /tmp/images --maxframes=250 --rotate=90
```

