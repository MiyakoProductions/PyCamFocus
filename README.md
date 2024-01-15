      ███████╗███╗   ███╗██╗██╗     ██╗   ██╗
      ██╔════╝████╗ ████║  ║██║     ╚██╗ ██╔╝
      █████╗  ██╔████╔██║██║██║      ╚████╔╝ 
      ██╔══╝  ██║╚██╔╝██║██║██║       ╚██╔╝  
      ███████╗██║ ╚═╝ ██║██║███████╗   ██║   
      ╚══════╝╚═╝     ╚═╝╚═╝╚══════╝   ╚═╝   
      Twitter/Twitch/Youtube: @ChiuYukina
    ═══════════════════════════════════════════
    
It bugged me that webcams still don't have any  good way
to control the focus manually. So I took the matter into
my own hands with this small Python script.

To use this script you will need to install
OpenCV2 and Pynput using the commands:
* pip install opencv-python
* pip install pynput

Using the script is simple. You may launch the script by
double-clicking on the file or using the command
"python PyCamFocus.py" in your terminal.

The default hotkeys are "[" to defocus and "]" to focus.
Additionally "q" is used to exit the script.
You may change the hotkeys and the steps following
the comments in the script.

Lastly, the default resolution is set to 1440x1080
which worked best for my Razer Kiyo Pro. Your camera may
use a different aspect ratio or resolution.

To make the script easier to use, I bound the wheel of
a Xencelab Remote to [ and ] Video:
https://x.com/ChiuYukina/status/1729769133569429595?s=20
