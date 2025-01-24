# Real-Time and Video-Based Gender Detection System

## Overview
This project implements a **gender detection system** capable of:
1. Detecting gender in real-time using a live camera feed.
2. Processing uploaded video files to identify the gender of individuals in the video.

## Features
- **Real-time Gender Detection**: Analyzes live video streams and identifies gender instantly.
- **Video File Processing**: Allows users to upload video files and detects the gender of people frame by frame.
- **Easy to Use**: Plug-and-play scripts for both real-time and offline video processing.

## Repository Files
- **`gender_age (realtime).py`**: Script for real-time gender detection using a webcam.
- **`gender_detection_video.py`**: Script for processing uploaded video files for gender detection.

## Requirements
- Python 3.x
- OpenCV
- NumPy
- Pre-trained models for gender detection (e.g., Caffe or TensorFlow models)

Install the required libraries using:
```bash
pip install -r requirements.txt
```

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/repository_name.git
   ```
2. Navigate to the directory:
   ```bash
   cd repository_name
   ```
3. Run the desired script:
   - **Real-Time Detection**:
     ```bash
     python gender_age (realtime).py
     ```
   - **Video File Processing**:
     ```bash
     python gender_detection_video.py --input your_video_file.mp4
     ```

## Pre-trained Models
Download the required pre-trained models and place them in a folder named `models` in the project directory:
- **Gender Model**: [Provide a link to the pre-trained model]

## Demo
- **Real-Time Detection**: The system uses your webcam to detect gender in real time.
- **Video Processing**: Upload a video, and the script will process it frame by frame to detect gender.

## How It Works
1. The system loads a pre-trained deep learning model for gender detection.
2. For real-time detection, the webcam feed is analyzed frame by frame.
3. For video files, each frame of the video is processed to identify gender.
4. Detected gender labels are displayed on the video output.

## Example Output
- **Real-Time Detection**: 
  Displays gender labels on individuals detected in the live feed.
- **Video Detection**: 
  Outputs a video file or real-time preview with gender labels overlaid on detected faces.

## Contributions
Feel free to contribute to this project by submitting issues, feature requests, or pull requests.

## License
[MIT License](LICENSE)
