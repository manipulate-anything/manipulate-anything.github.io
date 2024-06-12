#!/usr/bin/env bash

tasks=("put_knife"
       "take_umbrella"
       "lamp_on"
       "open_wine"
       "play_jenga"
       "open_box"
       "pick_and_lift"
       "put_block"
       "sort_mustard")

for task in "${tasks[@]}"
do
    ffmpeg -i ${task}.mp4 -c:v libx264 -crf 23 -preset medium -c:a aac -b:a 128k ${task}_fixed.mp4
    rm ${task}.mp4
    mv ${task}_fixed.mp4 ${task}.mp4
done
