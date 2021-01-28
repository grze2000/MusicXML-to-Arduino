import sys
import os
import xml.etree.ElementTree as ET
from zipfile import ZipFile
import tempfile

class Converter:
    durationValues = {'whole': 4, 'half': 2, 'quarter': 1, 'eighth': 0.5, '16th': 0.25}
    steps = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'A']

    def convertXML(self, file):
        print(file)

    def convertMXL(self, file):
        with tempfile.TemporaryDirectory() as tmpDir:
            with ZipFile(file, 'r') as mxl:
                mxl.extractall(tmpDir)
                for file in os.listdir(tmpDir):
                    if file.endswith('.xml'):
                        return self.convertXML(os.path.join(tmpDir, file))
                raise FileNotFoundError('.xml file not found')

    def convert(self, inputFile, outputDir):
        if not os.path.exists(inputFile):
            raise FileNotFoundError(f"{inputFile} doesn't exist")

        if not os.path.isdir(outputDir):
            raise FileNotFoundError(f"Directory {outputDir} doesn't exist")

        if inputFile.endswith('.xml'):
            self.convertXML(inputFile)
        elif inputFile.endswith('.mxl'):
            self.convertMXL(inputFile)
        else:
            raise ValueError(f"Invalid file type: .{inputFile.split('.')[-1]}. Expected .xml or .xml")

