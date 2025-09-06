## MC3DS Movies
- Makes/Plays movies in mc3ds via the pack-icon/block display.


## Generating an Animation:
- Have python and cv2/pillow installed with Python (`opencv-python` and `pillow` via pip).
- Execute the script by using `py [PATH_TO_C2A.py] [PATH_TO_MP4.mp4]`. (Do not include the `[]`).
- Place the generated animation on the following directory on your 3DS Console: `.\megapackPlugin\Animations\Helmet\`.
- Do **NOT** rename the File.

## Playing Animations:
- Click "Edit" on a World, or Create a New one.
- Goto the Texture Pack selection screen, and have the default on selected (called "Minecraft").
- Press "select", and check-mark the box that says "Play Animation off of SDMC" by pressing "A".
- Exit the menu by pressing the "X" button on the top-right of the bottom screen.
- The video will play within roughly 30s, and with audio if converted to dspadpcm.
  - With the name `exampleAudio.bcwav`, and in the same PATH as the animation on the 3DS Console.
