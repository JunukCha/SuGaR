import argparse
import cv2
import os

def video_to_images(video_path, output_folder):
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    if os.path.exists(video_path):
        # Open the video file
        cap = cv2.VideoCapture(video_path)

        if not cap.isOpened():
            print(f"Error: Could not open video file {video_path}")
            return

        frame_count = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            # Save frame as image
            output_path = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")
            cv2.imwrite(output_path, frame)
            frame_count += 1

        cap.release()
        print(f"Done: {frame_count} frames extracted to {output_folder}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert a video file to images.")
    parser.add_argument("--video_path", type=str, help="Path to the input video file")
    parser.add_argument("--output_folder", type=str, help="Folder to save the extracted images")

    args = parser.parse_args()
    video_to_images(args.video_path, args.output_folder)
