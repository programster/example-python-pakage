import os

def run(name=None):
    """
    Places binary image file wherever you called this script from.
    """
    source=os.path.dirname(__file__) + "/data/britney.jpg"
    dest=os.getcwd() + "/britney.jpg"
    with open(source, 'rb') as src, open(dest, 'wb') as dst: dst.write(src.read())