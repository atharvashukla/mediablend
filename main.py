import os
import re
import argparse
from moviepy.editor import ImageClip, concatenate_videoclips, AudioFileClip


# Read slide transition timestamps from a text file
def read_timestamps(txt_file):
    with open(txt_file, "r") as f:
        timestamps = [int(line.strip()) for line in f.readlines()]
    return timestamps


# Get the paths of slide images in a folder
def get_slide_paths(slide_folder):
    slides = [os.path.join(slide_folder, f) for f in os.listdir(slide_folder) if f.endswith('.png')]
    slides = sorted(slides, key=lambda x: int(re.search(r'slide-(\d+)', x).group(1)))
    return slides

# Generate slide timings based on the timestamps and the audio file duration
def generate_slide_timings(audio_file, timestamps):
    audio_duration = AudioFileClip(audio_file).duration
    slide_timings = [(timestamps[i], timestamps[i+1]) for i in range(len(timestamps)-1)]
    slide_timings.append((timestamps[-1], audio_duration))
    return slide_timings

# Create video clips using the slide images and timings
def create_video_clips(slides, slide_timings, fps=24):
    video_clips = []
    for slide, timing in zip(slides, slide_timings):
        clip = ImageClip(slide, duration=timing[1]-timing[0]).set_fps(fps)
        video_clips.append(clip)
    return video_clips

# Combine video clips with the audio file and create the final video output
def create_video(audio_file, video_clips, output_file, fps=24):
    final_clip = concatenate_videoclips(video_clips)
    final_clip = final_clip.set_audio(AudioFileClip(audio_file))
    final_clip.write_videofile(output_file, codec='libx264', audio_codec='aac', fps=fps)

# Main function to create a video using slide images, audio, and slide transition timestamps
def main(slide_folder, audio_file, txt_file, output_file):
    timestamps = read_timestamps(txt_file)
    slides = get_slide_paths(slide_folder)
    slide_timings = generate_slide_timings(audio_file, timestamps)
    video_clips = create_video_clips(slides, slide_timings)
    create_video(audio_file, video_clips, output_file)


def main(args):
    slide_folder = args.slide_folder
    audio_file = args.audio_file
    txt_file = args.txt_file
    output_file = args.output_file

    timestamps = read_timestamps(txt_file)
    slides = get_slide_paths(slide_folder)
    slide_timings = generate_slide_timings(audio_file, timestamps)
    video_clips = create_video_clips(slides, slide_timings)
    create_video(audio_file, video_clips, output_file)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create a video from slides, audio, and slide timestamps.')
    parser.add_argument('slide_folder', help='Path to the folder containing slide images named slide-1, slide-2, ...')
    parser.add_argument('audio_file', help='Path to the .wav audio file.')
    parser.add_argument('txt_file', help='Path to the .txt file containing timestamps for slide transitions.')
    parser.add_argument('output_file', help='Path to the output video file (.mp4 format).')

    args = parser.parse_args()
    main(args)


# python3 main.py path/to/slides-folder path/to/audio.wav path/to/timestamps.txt output/video.mp4
