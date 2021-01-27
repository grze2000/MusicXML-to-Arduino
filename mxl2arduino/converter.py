import sys
import os
import xml.etree.ElementTree as ET
from zipfile import ZipFile
import tempfile

class Converter:
    durationValues = {'whole': 4, 'half': 2, 'quarter': 1, 'eighth': 0.5, '16th': 0.25}
    steps = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'A']

    def convert(self, inputFile, outputDir):
        pass
