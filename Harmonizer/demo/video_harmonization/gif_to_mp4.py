from moviepy.editor import VideoFileClip
import argparse
from pathlib import Path
import cv2

def parse_args():
    parser = argparse.ArgumentParser("Convert GIF to MP4", add_help=False)
    parser.add_argument("--gif", default="", type=str, required=True)
    parser.add_argument("--mp4", default="", type=str, required=False)
    parser.add_argument("--fps", default=24, type=int, help="Frames per second for the MP4 video")

    args = parser.parse_args()
    return args

def main():
    args = parse_args()

    # Input GIF file path
    gif_path = args.gif

    # Output MP4 file path
    if args.mp4:
        mp4_path = args.mp4
    else:
        mp4_path = str(Path(gif_path).with_suffix(".mp4"))

    # Open the GIF file using cv2.VideoCapture
    gif = cv2.VideoCapture(gif_path)

    # Get the width, height, and frame count of the GIF
    width = int(gif.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(gif.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = args.fps  # Use user-specified FPS

    # Define the codec and create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(mp4_path, fourcc, fps, (width, height))

    # Read each frame from the GIF and write it to the MP4 file
    while True:
        ret, frame = gif.read()
        if not ret:
            break  # End of GIF

        # Write the frame to the MP4 file
        video_writer.write(frame)

    # Release resources
    gif.release()
    video_writer.release()

    print(f"GIF has been successfully converted to MP4: {mp4_path}")

if __name__ == '__main__':
    main()