# MusicXML to Arduino
Parse MusicXML to the Arduino melody

Based on C# and Ruby versions:
- [shvelo - musicxml_to_arduino](https://github.com/shvelo/musicxml_to_arduino) (Ruby)
- [MrRedBeard - DotNet-MXL-Parsing-for-Arduino](https://github.com/MrRedBeard/DotNet-MXL-Parsing-for-Arduino) (C#)
## Requirements
Python3 installed on your OS
## Usage
You can use `.mxl` or `.xml` files to generate Arduino code.
```
python translate-cmd.py <path-to-mxl-file>
```
Script will generate two files (melody.h and melody.cpp). You can use them in your .ino file as shown in the example file.
