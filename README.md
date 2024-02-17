# 📸 Webcam Frame Grabber

Webcam Frame Grabber is a simple Python utility that captures frames from your webcam and saves them to a specified directory. This tool is perfect for creating datasets for computer vision projects or simply capturing snapshots from your webcam.

## 🛠 Installation

Before you can use Webcam Frame Grabber, you'll need to install the required Python libraries. The script relies on `opencv-python` for capturing and processing video frames.

1. Clone this repository or download the `webcam_frame_grabber.py` script to your local machine.
2. Ensure you have Python installed on your system. This script is tested with Python 3.6+.
3. Create a virtual environment (optional but recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
4. Install the required packages using the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```

## 🚀 Usage

To use the Webcam Frame Grabber, you'll need to specify the output directory where the captured frames will be saved. Optionally, you can specify the index of the camera (useful if you have multiple webcams).

### Basic Command

```bash
python webcam_frame_grabber.py <output_directory> [--camera_idx CAMERA_INDEX]
```

- `<output_directory>`: The directory where the captured frames will be saved. The script will create this directory if it does not exist.
- `--camera_idx CAMERA_INDEX`: (Optional) The index of the webcam to use. Defaults to 0 (the primary webcam).

### Example

```bash
python webcam_frame_grabber.py ./captured_frames --camera_idx 0
```

This command will start capturing frames from the primary webcam and save them to the `./captured_frames` directory.

### Saving Frames

While the script is running, you can:
- Press `q` to quit the program. 🛑
- Press `s` to save the current frame to the output directory. The frames are timestamped for convenience. 💾

## 📋 Requirements

- Python 3.6+ 🐍
- opencv-python 🖼️

Refer to the `requirements.txt` for detailed version requirements.