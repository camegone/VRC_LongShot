# VRC_LongShot
a program to take long exposured photos. intended to use on VRC, but this can use for other desktop apps.
compatible for windows. need to have python installed on your PC.
![preview image 1](https://pbs.twimg.com/media/FrpXKT3agAAa8j7?format=png&name=900x900)
![preview image 2](https://pbs.twimg.com/media/FrpXLODaMAEXKEx?format=png&name=900x900)
![preview image 3](https://pbs.twimg.com/media/FrpXMVHacAAmq2K?format=png&name=900x900)
![preview image 4](https://pbs.twimg.com/media/FrpXSeXaIAEisCA?format=png&name=900x900)

# Installation
 1. clone this repo. 
 1. run `install.bat`.
 

# Usage
 1. run app you want to shot (default is VRChat)
 1. run `vrc_longhoot.py`
 1. wait until the shot ends. (if you change focus on other windows, recording will be interrupted and the image saved immediately.)


# Option
 you can change the behavior via manually edit `options.json`.
 ## version
  for the internal purpose. **DO NOT CHANGE**
 
 ## capture
  settings of capturing behavior
  ### target
   the name of window to take a photo. default is `VRChat`.
  ### fps
   frequancy of capture the screen. default is `10`. *recommends to set below than 20*
  ### seconds
   a time to end recording automatically. default is `10`.
  ### resize
   if True, resize the window to determined size below. default is `true`.
  ### size
   target size of application's rendering area.
   #### width
    default is `1280`.
   #### height
    default is `720`.
 ## save
  config among saving pictures
  ### folder
   a folder to save photos. both relative and absolute path will be accepted. default is `photos/`
  ### prefix
   specify the prefix of fine name to be saved. default is `VRCLS`
  ### monthly_subdir
   if true, your photos are sorted into subdirs for each months. default is `true`
  ### make_bright
   if true, images will be slightly brighter than it is turned off. default is `true` (If `true`, the most bright pixel has to be maximum brightness, when `false` each pixels are just divided by the frames elapsed.)
