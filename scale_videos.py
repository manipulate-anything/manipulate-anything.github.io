#!/usr/bin/env python

import argparse
import os
import re
import subprocess


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--folder",
        type=str,
        default=".",
        help="The folder from which to grab the video files for conversion",
    )
    parser.add_argument(
        "--width",
        type=int,
        default=640,
        help="The desired video width for the converted videos",
    )
    args = parser.parse_args()

    # Get the path to the desired folder
    videos_folder_path = os.path.abspath(os.path.join(os.getcwd(), args.folder))

    # Get all the valid videos to convert (.mp4 for now)
    video_files = [
        os.path.join(videos_folder_path, file)
        for file in os.listdir(videos_folder_path)
        if re.search("\.mp4$", file) and "scaled" not in file  # type: ignore
    ]
    video_files_names = [
        f"{os.path.splitext(os.path.basename(file))[0]}_scaled.mp4"
        for file in video_files
    ]
    video_files_paths = [
        os.path.join(videos_folder_path, file) for file in video_files_names
    ]

    # Use ffmpeg to scale the videos accordingly
    for video_file_in, video_file_out in zip(video_files, video_files_paths):
        if subprocess.call(
            (
                "ffmpeg",
                "-i",
                video_file_in,
                "-vf",
                f"scale={args.width}:-2",
                video_file_out,
            )
        ):
            return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
