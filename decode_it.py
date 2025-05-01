# Author: AnuragPandey | https://www.linkedin.com/in/-anurag-pandey-/
try:
    import zlib
    import base64
    import numpy as np
    from PIL import Image
except ImportError:
    print("""
    Hi Decoder,
        Congratulations on decoding this NFT :) 
        But to execute this program, 
        you need to install 'pillow' and 'numpy' library.
    """)
assert zlib, "Python3 should be installed on your system"
assert base64, "Python3 should be installed on your system"
assert np, "Numpy library should be installed on your system"
assert Image, "Pillow library should be installed on your system"

# Constants
FILE_EXTENSION = "py"
FILE_NAME = "encode_it"


def generate_source():
    try:
        img = Image.open("DECODE.IT.png")
    except FileNotFoundError:
        print("""
        Hi Decoder,
              If you are using this code to DECODE from the image,
              you need to put the DECODE.IT NFT Image into current folder with this file
              and the NFT image file name should be 'DECODE.IT.png'
        """)
    pixels = np.asarray(img)
    rows, cols = pixels.shape
    source = []
    for r in range(rows):
        for c in range(cols):
            if pixels[r, c] != 0 and pixels[r, c] != 255:
                source.append(chr(pixels[r, c]))
        source.append("\n")
    
    with open(f"{FILE_NAME}.{FILE_EXTENSION}", 'w') as f:
        f.write("".join(source))

if __name__=="__main__":
    generate_source()
    print("""
    
    HI DECODER, 
        MY NAME IS ANURAG PANDEY, I AM THE AUTHOR OF DECODE.IT NFT. 
        FIRST OF ALL, I WANT TO CONGRATULATE YOU FOR SUCCESSFULLY DECODING THE DECODE.IT NFT.
        THIS NFT PROJECT WAS FUN TO BUILD AND INSPIRED ME TO LEARN MORE ABOUT METAVERSE AND BLOCKCHAIN.
        IF YOU HAVE EXECUTED THIS DECODED PROGRAM, IT WOULD HAVE CREATED A encode_it.py FILE FOR YOU.
        
        ABOUT 180 LINES ARE CODE-FREE IN encode_it.py file, YOU CAN UTILIZE THEM BY ADDING PYTHON3 CODE THERE.
        AND TO ENCODE THE NEW ADDITIONAL CODE INTO DECODE.IT IMAGE, 
        
        JUST RERUN THAT PROGRAM :)  
          
        ENJOY !!

        FOLLOW ME FOR MORE UPDATES: https://www.linkedin.com/in/-anurag-pandey-/
    
    """)

