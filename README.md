<h1 align="center">Mediablend</h1>

<p align="center">
  <img src="https://raw.githubusercontent.com/atharvashukla/mediablend/main/mediablend_logo.svg" />
</p>


Mediablend: A command-line tool to seamlessly combine slide images, audio, and transition timestamps into an engaging video presentation.

## Overview

Mediablend is a command-line tool that allows users to combine a set of slide images, an audio file, and slide transition timestamps to create a video. This tool is useful for creating lecture or presentation videos using pre-recorded audio and a sequence of slide images.

## Dependencies

- Python 3.x
- moviepy

## Installation

Ensure you have Python 3.x installed on your system.
Install the required package:

```python
pip install moviepy
```

## Usage

To use Slide Video Creator, follow these steps:

1. Prepare a folder containing your slide images in PNG format, named `slide-1.png`, `slide-2.png`, etc.
2. Prepare a `.wav` audio file containing the audio for the video.
3. Prepare a `.txt` file containing the slide transition timestamps in seconds, one per line.
4. Run the script with the following command:
    ```zsh
    python3 main.py path/to/slides-folder path/to/audio.wav path/to/timestamps.txt output/video.mp4
    ```

## Arguments

- `slide_folder`: Path to the folder containing slide images named slide-1.png, slide-2.png, etc.
- `audio_file`: Path to the .wav audio file.
- `txt_file`: Path to the .txt file containing timestamps for slide transitions.
- `output_file`: Path to the output video file (.mp4 format).

## Functions

- `read_timestamps(txt_file)`: Reads slide transition timestamps from a text file.
- `get_slide_paths(slide_folder)`: Gets the paths of slide images in a folder.
- `generate_slide_timings(audio_file, timestamps)`: Generates slide timings based on the timestamps and the audio file duration.
- `create_video_clips(slides, slide_timings, fps=24)`: Creates video clips using the slide images and timings.
- `create_video(audio_file, video_clips, output_file, fps=24)`: Combines video clips with the audio file and creates the final video output.
- `main(args)`: Main function to create a video using slide images, audio, and slide transition timestamps.


## Example

To create a video using the following files:

- Slide images in a folder: `path/to/slides-folder`
- Audio file: `path/to/audio.wav`
- Timestamps file: `path/to/timestamps.txt`

Run the following command:

```python
python3 main.py path/to/slides-folder path/to/audio.wav path/to/timestamps.txt output/video.mp4
```

The output video will be saved as `output/video.mp4`.
