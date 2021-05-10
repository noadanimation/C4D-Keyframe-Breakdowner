## C4D Keyframe Breakdowner
Animation tool for Cinema 4D R23 to easily add inbetween poses, helpful for character animation workflows.

Inspired by (but with far less features than) https://github.com/boredstiff/tweenMachine

## Installation
Download everything then copy the 'keyframebreakdowner' directory to your Cinema 4D plugins folder, restart or open Cinema 4D.

## Use
1) Open the Keframe Breakdowner window from C4D's 'Extensions' menu - you can add the window to your layout so you don't have to do this step every time.
2) With your animated object or tag selected, press the buttons to create new inbetween keyframes (or alter existing keyframes) at your current project time, with values interpolated from the nearest previous and nearest next keyframes.
   * Pressing the numbered buttons (15 through 85) will create new keyframes that are 15%, 33%, 50% etc from the previous keyframe to the next keyframe.
   * Or enter a custom percentage in the text field above the 'Go' button, then press 'Go'
   * Press '--', '-', '+', or '++' to tweak existing keyframes by shifting their values slightly towards the previous or next keyframe
   * Press 'Swap' to swap the previous/current keyframe with the next keyframe

### Notes
* All animated parameters on your current selection will be altered at the same time, there's no option for excluding or selecting certain parameters.
* Your playhead needs to be between two keyframes for the plugin to do anything, as it interpolates between the values of the two keyframes.
* Ideally you should work with 'stepped' curves while using Keyframe Breakdowner, then smooth your curves once finished - it will respect the curve type of surrounding keyframes but might not smooth them nicely in other modes.

## Licence
Modified BSD - available in the .pyp file
