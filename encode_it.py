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
FILE_SIZE = (512, 512)
FILE_EXTENSION = "png"
FILE_NAME = "DECODE.IT"
BLACK_PIXEL_LOCS = """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"""

def compress_to_base64(int_list):
    array = np.array(int_list, dtype=np.uint32)
    compressed = zlib.compress(array.tobytes())
    encoded = base64.b64encode(compressed).decode('utf-8')
    return encoded

def decompress_from_base64(encoded_string):
    compressed = base64.b64decode(encoded_string)
    decompressed = zlib.decompress(compressed)
    array = np.frombuffer(decompressed, dtype=np.uint32)
    return array.tolist()

def generate_from_source():

    ##@ Current Source Reader
    with open(__file__, 'r') as f:
        source = f.read()
    ##@

    gen_img = np.full(FILE_SIZE, 255, dtype=np.uint8)
    rows, cols = gen_img.shape # Width, Height
    # r*512 + c = idx
    # idx % 512 = c
    # idx // 512 = r
    blocs = [[idx//512, idx%512] for idx in 
             decompress_from_base64(BLACK_PIXEL_LOCS)]
    for bloc in blocs:
        gen_img[bloc[0], bloc[1]] = 0
    index = 0
    for r in range(rows):
        for c in range(cols):
            if gen_img[r, c] == 255 and index < len(source):
                order = ord(source[index])
                if order == 10:
                    index+=1
                    break
                gen_img[r, c] = order
                index+=1
    nimg = Image.fromarray(gen_img)
    nimg.save(f"{FILE_NAME}.{FILE_EXTENSION}")

if __name__=="__main__":
    generate_from_source()
    print("""
    
    HI DECODER, 
        MY NAME IS ANURAG PANDEY, I AM THE AUTHOR OF DECODE.IT NFT. 
        FIRST OF ALL, I WANT TO CONGRATULATE YOU FOR SUCCESSFULLY DECODING THE DECODE.IT NFT.
        THIS NFT PROJECT WAS FUN TO BUILD AND INSPIRED ME TO LEARN MORE ABOUT METAVERSE AND BLOCKCHAIN.
        IF YOU HAVE EXECUTED THIS DECODED PROGRAM, IT WOULD HAVE CREATED A DECODE.IT IMAGE FOR YOU.
        ABOUT 180 LINES ARE CODE-FREE, YOU CAN UTILIZE THEM BY ADDING PYTHON3 CODE THERE.
        AND TO ENCODE THIS NEW ADDITIONAL CODE INTO DECODE.IT IMAGE, 
        
        JUST RERUN THIS PROGRAM :)  
          
        ENJOY !!

        FOLLOW ME FOR MORE UPDATES: https://www.linkedin.com/in/-anurag-pandey-/
    
    """)

































































































































































































r"""
                                                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                                  
PPPPPPPPPPPPPPPPP        YYYYYYY       YYYYYYY     TTTTTTTTTTTTTTTTTTTTTTT     HHHHHHHHH     HHHHHHHHH          OOOOOOOOO          NNNNNNNN        NNNNNNNN               FFFFFFFFFFFFFFFFFFFFFF     IIIIIIIIII     LLLLLLLLLLL                  EEEEEEEEEEEEEEEEEEEEEE           
P::::::::::::::::P       Y:::::Y       Y:::::Y     T:::::::::::::::::::::T     H:::::::H     H:::::::H        OO:::::::::OO        N:::::::N       N::::::N               F::::::::::::::::::::F     I::::::::I     L:::::::::L                  E::::::::::::::::::::E           
P::::::PPPPPP:::::P      Y:::::Y       Y:::::Y     T:::::::::::::::::::::T     H:::::::H     H:::::::H      OO:::::::::::::OO      N::::::::N      N::::::N               F::::::::::::::::::::F     I::::::::I     L:::::::::L                  E::::::::::::::::::::E           
PP:::::P     P:::::P     Y::::::Y     Y::::::Y     T:::::TT:::::::TT:::::T     HH::::::H     H::::::HH     O:::::::OOO:::::::O     N:::::::::N     N::::::N               FF::::::FFFFFFFFF::::F     II::::::II     LL:::::::LL                  EE::::::EEEEEEEEE::::E           
  P::::P     P:::::P     YYY:::::Y   Y:::::YYY     TTTTTT  T:::::T  TTTTTT       H:::::H     H:::::H       O::::::O   O::::::O     N::::::::::N    N::::::N                 F:::::F       FFFFFF       I::::I         L:::::L                      E:::::E       EEEEEE           
  P::::P     P:::::P        Y:::::Y Y:::::Y                T:::::T               H:::::H     H:::::H       O:::::O     O:::::O     N:::::::::::N   N::::::N                 F:::::F                    I::::I         L:::::L                      E:::::E                        
  P::::PPPPPP:::::P          Y:::::Y:::::Y                 T:::::T               H::::::HHHHH::::::H       O:::::O     O:::::O     N:::::::N::::N  N::::::N                 F::::::FFFFFFFFFF          I::::I         L:::::L                      E::::::EEEEEEEEEE              
  P:::::::::::::PP            Y:::::::::Y                  T:::::T               H:::::::::::::::::H       O:::::O     O:::::O     N::::::N N::::N N::::::N                 F:::::::::::::::F          I::::I         L:::::L                      E:::::::::::::::E              
  P::::PPPPPPPPP               Y:::::::Y                   T:::::T               H:::::::::::::::::H       O:::::O     O:::::O     N::::::N  N::::N:::::::N                 F:::::::::::::::F          I::::I         L:::::L                      E:::::::::::::::E              
  P::::P                        Y:::::Y                    T:::::T               H::::::HHHHH::::::H       O:::::O     O:::::O     N::::::N   N:::::::::::N                 F::::::FFFFFFFFFF          I::::I         L:::::L                      E::::::EEEEEEEEEE              
  P::::P                        Y:::::Y                    T:::::T               H:::::H     H:::::H       O:::::O     O:::::O     N::::::N    N::::::::::N                 F:::::F                    I::::I         L:::::L                      E:::::E                        
  P::::P                        Y:::::Y                    T:::::T               H:::::H     H:::::H       O::::::O   O::::::O     N::::::N     N:::::::::N                 F:::::F                    I::::I         L:::::L         LLLLLL       E:::::E       EEEEEE           
PP::::::PP                      Y:::::Y                  TT:::::::TT           HH::::::H     H::::::HH     O:::::::OOO:::::::O     N::::::N      N::::::::N               FF:::::::FF                II::::::II     LL:::::::LLLLLLLLL:::::L     EE::::::EEEEEEEE:::::E           
P::::::::P                   YYYY:::::YYYY               T:::::::::T           H:::::::H     H:::::::H      OO:::::::::::::OO      N::::::N       N:::::::N               F::::::::FF                I::::::::I     L::::::::::::::::::::::L     E::::::::::::::::::::E           
P::::::::P                   Y:::::::::::Y               T:::::::::T           H:::::::H     H:::::::H        OO:::::::::OO        N::::::N        N::::::N               F::::::::FF                I::::::::I     L::::::::::::::::::::::L     E::::::::::::::::::::E           
PPPPPPPPPP                   YYYYYYYYYYYYY               TTTTTTTTTTT           HHHHHHHHH     HHHHHHHHH          OOOOOOOOO          NNNNNNNN         NNNNNNN               FFFFFFFFFFF                IIIIIIIIII     LLLLLLLLLLLLLLLLLLLLLLLL     EEEEEEEEEEEEEEEEEEEEEE           
                                                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                                  












































                                                                                                                                                                                                                                                                                  
DDDDDDDDDDDDD             EEEEEEEEEEEEEEEEEEEEEE             CCCCCCCCCCCCC          OOOOOOOOO          DDDDDDDDDDDDD             EEEEEEEEEEEEEEEEEEEEEE               HHHHHHHHH     HHHHHHHHH     IIIIIIIIII     NNNNNNNN        NNNNNNNN     TTTTTTTTTTTTTTTTTTTTTTT             
D::::::::::::DDD          E::::::::::::::::::::E          CCC::::::::::::C        OO:::::::::OO        D::::::::::::DDD          E::::::::::::::::::::E               H:::::::H     H:::::::H     I::::::::I     N:::::::N       N::::::N     T:::::::::::::::::::::T             
D:::::::::::::::DD        E::::::::::::::::::::E        CC:::::::::::::::C      OO:::::::::::::OO      D:::::::::::::::DD        E::::::::::::::::::::E               H:::::::H     H:::::::H     I::::::::I     N::::::::N      N::::::N     T:::::::::::::::::::::T             
DDD:::::DDDDD:::::D       EE::::::EEEEEEEEE::::E       C:::::CCCCCCCC::::C     O:::::::OOO:::::::O     DDD:::::DDDDD:::::D       EE::::::EEEEEEEEE::::E               HH::::::H     H::::::HH     II::::::II     N:::::::::N     N::::::N     T:::::TT:::::::TT:::::T             
  D:::::D    D:::::D        E:::::E       EEEEEE      C:::::C       CCCCCC     O::::::O   O::::::O       D:::::D    D:::::D        E:::::E       EEEEEE                 H:::::H     H:::::H         I::::I       N::::::::::N    N::::::N     TTTTTT  T:::::T  TTTTTT             
  D:::::D     D:::::D       E:::::E                  C:::::C                   O:::::O     O:::::O       D:::::D     D:::::D       E:::::E                              H:::::H     H:::::H         I::::I       N:::::::::::N   N::::::N             T:::::T              :::::: 
  D:::::D     D:::::D       E::::::EEEEEEEEEE        C:::::C                   O:::::O     O:::::O       D:::::D     D:::::D       E::::::EEEEEEEEEE                    H::::::HHHHH::::::H         I::::I       N:::::::N::::N  N::::::N             T:::::T              :::::: 
  D:::::D     D:::::D       E:::::::::::::::E        C:::::C                   O:::::O     O:::::O       D:::::D     D:::::D       E:::::::::::::::E                    H:::::::::::::::::H         I::::I       N::::::N N::::N N::::::N             T:::::T              :::::: 
  D:::::D     D:::::D       E:::::::::::::::E        C:::::C                   O:::::O     O:::::O       D:::::D     D:::::D       E:::::::::::::::E                    H:::::::::::::::::H         I::::I       N::::::N  N::::N:::::::N             T:::::T                     
  D:::::D     D:::::D       E::::::EEEEEEEEEE        C:::::C                   O:::::O     O:::::O       D:::::D     D:::::D       E::::::EEEEEEEEEE                    H::::::HHHHH::::::H         I::::I       N::::::N   N:::::::::::N             T:::::T                     
  D:::::D     D:::::D       E:::::E                  C:::::C                   O:::::O     O:::::O       D:::::D     D:::::D       E:::::E                              H:::::H     H:::::H         I::::I       N::::::N    N::::::::::N             T:::::T                     
  D:::::D    D:::::D        E:::::E       EEEEEE      C:::::C       CCCCCC     O::::::O   O::::::O       D:::::D    D:::::D        E:::::E       EEEEEE                 H:::::H     H:::::H         I::::I       N::::::N     N:::::::::N             T:::::T              :::::: 
DDD:::::DDDDD:::::D       EE::::::EEEEEEEE:::::E       C:::::CCCCCCCC::::C     O:::::::OOO:::::::O     DDD:::::DDDDD:::::D       EE::::::EEEEEEEE:::::E               HH::::::H     H::::::HH     II::::::II     N::::::N      N::::::::N           TT:::::::TT            :::::: 
D:::::::::::::::DD        E::::::::::::::::::::E        CC:::::::::::::::C      OO:::::::::::::OO      D:::::::::::::::DD        E::::::::::::::::::::E               H:::::::H     H:::::::H     I::::::::I     N::::::N       N:::::::N           T:::::::::T            :::::: 
D::::::::::::DDD          E::::::::::::::::::::E          CCC::::::::::::C        OO:::::::::OO        D::::::::::::DDD          E::::::::::::::::::::E               H:::::::H     H:::::::H     I::::::::I     N::::::N        N::::::N           T:::::::::T                   
DDDDDDDDDDDDD             EEEEEEEEEEEEEEEEEEEEEE             CCCCCCCCCCCCC          OOOOOOOOO          DDDDDDDDDDDDD             EEEEEEEEEEEEEEEEEEEEEE               HHHHHHHHH     HHHHHHHHH     IIIIIIIIII     NNNNNNNN         NNNNNNN           TTTTTTTTTTT                   
                                                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                                  
IIIIIIIIII     FFFFFFFFFFFFFFFFFFFFFF               PPPPPPPPPPPPPPPPP        IIIIIIIIII     XXXXXXX       XXXXXXX     EEEEEEEEEEEEEEEEEEEEEE     LLLLLLLLLLL                                                                                                                      
I::::::::I     F::::::::::::::::::::F               P::::::::::::::::P       I::::::::I     X:::::X       X:::::X     E::::::::::::::::::::E     L:::::::::L                                                                                                                      
I::::::::I     F::::::::::::::::::::F               P::::::PPPPPP:::::P      I::::::::I     X:::::X       X:::::X     E::::::::::::::::::::E     L:::::::::L                                                                                                                      
II::::::II     FF::::::FFFFFFFFF::::F               PP:::::P     P:::::P     II::::::II     X::::::X     X::::::X     EE::::::EEEEEEEEE::::E     LL:::::::LL                                                                                                                      
  I::::I         F:::::F       FFFFFF                 P::::P     P:::::P       I::::I       XXX:::::X   X:::::XXX       E:::::E       EEEEEE       L:::::L                                                                                                                        
  I::::I         F:::::F                              P::::P     P:::::P       I::::I          X:::::X X:::::X          E:::::E                    L:::::L                                                                                                                        
  I::::I         F::::::FFFFFFFFFF                    P::::PPPPPP:::::P        I::::I           X:::::X:::::X           E::::::EEEEEEEEEE          L:::::L                                                                                                                        
  I::::I         F:::::::::::::::F                    P:::::::::::::PP         I::::I            X:::::::::X            E:::::::::::::::E          L:::::L                                                                                                                        
  I::::I         F:::::::::::::::F                    P::::PPPPPPPPP           I::::I            X:::::::::X            E:::::::::::::::E          L:::::L                                                                                                                        
  I::::I         F::::::FFFFFFFFFF                    P::::P                   I::::I           X:::::X:::::X           E::::::EEEEEEEEEE          L:::::L                                                                                                                        
  I::::I         F:::::F                              P::::P                   I::::I          X:::::X X:::::X          E:::::E                    L:::::L                                                                                                                        
  I::::I         F:::::F                              P::::P                   I::::I       XXX:::::X   X:::::XXX       E:::::E       EEEEEE       L:::::L         LLLLLL                                                                                                         
II::::::II     FF:::::::FF                          PP::::::PP               II::::::II     X::::::X     X::::::X     EE::::::EEEEEEEE:::::E     LL:::::::LLLLLLLLL:::::L                                                                                                         
I::::::::I     F::::::::FF                          P::::::::P               I::::::::I     X:::::X       X:::::X     E::::::::::::::::::::E     L::::::::::::::::::::::L                                                                                                         
I::::::::I     F::::::::FF                          P::::::::P               I::::::::I     X:::::X       X:::::X     E::::::::::::::::::::E     L::::::::::::::::::::::L                                                                                                         
IIIIIIIIII     FFFFFFFFFFF                          PPPPPPPPPP               IIIIIIIIII     XXXXXXX       XXXXXXX     EEEEEEEEEEEEEEEEEEEEEE     LLLLLLLLLLLLLLLLLLLLLLLL                                                                                                         
                                                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                                  
     000000000                         OOOOOOOOO     RRRRRRRRRRRRRRRRR                   222222222222222         555555555555555555      555555555555555555                                                                                                                       
   00:::::::::00                     OO:::::::::OO   R::::::::::::::::R                 2:::::::::::::::22       5::::::::::::::::5      5::::::::::::::::5                                                                                                                       
 00:::::::::::::00                 OO:::::::::::::OO R::::::RRRRRR:::::R                2::::::222222:::::2      5::::::::::::::::5      5::::::::::::::::5                                                                                                                       
0:::::::000:::::::0               O:::::::OOO:::::::ORR:::::R     R:::::R               2222222     2:::::2      5:::::555555555555      5:::::555555555555                                                                                                                       
0::::::0   0::::::0               O::::::O   O::::::O  R::::R     R:::::R                           2:::::2      5:::::5                 5:::::5                                                                                                                                  
0:::::0     0:::::0               O:::::O     O:::::O  R::::R     R:::::R                           2:::::2      5:::::5                 5:::::5                                                                                                                                  
0:::::0     0:::::0               O:::::O     O:::::O  R::::RRRRRR:::::R                         2222::::2       5:::::5555555555        5:::::5555555555                                                                                                                         
0:::::0 000 0:::::0               O:::::O     O:::::O  R:::::::::::::RR                     22222::::::22        5:::::::::::::::5       5:::::::::::::::5                                                                                                                        
0:::::0 000 0:::::0               O:::::O     O:::::O  R::::RRRRRR:::::R                  22::::::::222          555555555555:::::5      555555555555:::::5                                                                                                                       
0:::::0     0:::::0               O:::::O     O:::::O  R::::R     R:::::R                2:::::22222                         5:::::5                 5:::::5                                                                                                                      
0:::::0     0:::::0               O:::::O     O:::::O  R::::R     R:::::R               2:::::2                              5:::::5                 5:::::5                                                                                                                      
0::::::0   0::::::0               O::::::O   O::::::O  R::::R     R:::::R               2:::::2                  5555555     5:::::5     5555555     5:::::5                                                                                                                      
0:::::::000:::::::0               O:::::::OOO:::::::ORR:::::R     R:::::R               2:::::2       222222     5::::::55555::::::5     5::::::55555::::::5                                                                                                                      
 00:::::::::::::00                 OO:::::::::::::OO R::::::R     R:::::R               2::::::2222222:::::2      55:::::::::::::55       55:::::::::::::55                                                                                                                       
   00:::::::::00                     OO:::::::::OO   R::::::R     R:::::R               2::::::::::::::::::2        55:::::::::55           55:::::::::55                                                                                                                         
     000000000                         OOOOOOOOO     RRRRRRRR     RRRRRRR               22222222222222222222          555555555               555555555                                                                                                                           
                                                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                                  
TTTTTTTTTTTTTTTTTTTTTTT     HHHHHHHHH     HHHHHHHHH     EEEEEEEEEEEEEEEEEEEEEE     NNNNNNNN        NNNNNNNN                  SSSSSSSSSSSSSSS      KKKKKKKKK    KKKKKKK     IIIIIIIIII     PPPPPPPPPPPPPPPPP                                                                       
T:::::::::::::::::::::T     H:::::::H     H:::::::H     E::::::::::::::::::::E     N:::::::N       N::::::N                SS:::::::::::::::S     K:::::::K    K:::::K     I::::::::I     P::::::::::::::::P                                                                      
T:::::::::::::::::::::T     H:::::::H     H:::::::H     E::::::::::::::::::::E     N::::::::N      N::::::N               S:::::SSSSSS::::::S     K:::::::K    K:::::K     I::::::::I     P::::::PPPPPP:::::P                                                                     
T:::::TT:::::::TT:::::T     HH::::::H     H::::::HH     EE::::::EEEEEEEEE::::E     N:::::::::N     N::::::N               S:::::S     SSSSSSS     K:::::::K   K::::::K     II::::::II     PP:::::P     P:::::P                                                                    
TTTTTT  T:::::T  TTTTTT       H:::::H     H:::::H         E:::::E       EEEEEE     N::::::::::N    N::::::N               S:::::S                 KK::::::K  K:::::KKK       I::::I         P::::P     P:::::P                                                                    
        T:::::T               H:::::H     H:::::H         E:::::E                  N:::::::::::N   N::::::N               S:::::S                   K:::::K K:::::K          I::::I         P::::P     P:::::P                                                                    
        T:::::T               H::::::HHHHH::::::H         E::::::EEEEEEEEEE        N:::::::N::::N  N::::::N                S::::SSSS                K::::::K:::::K           I::::I         P::::PPPPPP:::::P                                                                     
        T:::::T               H:::::::::::::::::H         E:::::::::::::::E        N::::::N N::::N N::::::N                 SS::::::SSSSS           K:::::::::::K            I::::I         P:::::::::::::PP                                                                      
        T:::::T               H:::::::::::::::::H         E:::::::::::::::E        N::::::N  N::::N:::::::N                   SSS::::::::SS         K:::::::::::K            I::::I         P::::PPPPPPPPP                                                                        
        T:::::T               H::::::HHHHH::::::H         E::::::EEEEEEEEEE        N::::::N   N:::::::::::N                      SSSSSS::::S        K::::::K:::::K           I::::I         P::::P                                                                                
        T:::::T               H:::::H     H:::::H         E:::::E                  N::::::N    N::::::::::N                           S:::::S       K:::::K K:::::K          I::::I         P::::P                                                                                
        T:::::T               H:::::H     H:::::H         E:::::E       EEEEEE     N::::::N     N:::::::::N                           S:::::S     KK::::::K  K:::::KKK       I::::I         P::::P                                                                                
      TT:::::::TT           HH::::::H     H::::::HH     EE::::::EEEEEEEE:::::E     N::::::N      N::::::::N               SSSSSSS     S:::::S     K:::::::K   K::::::K     II::::::II     PP::::::PP                                                                              
      T:::::::::T           H:::::::H     H:::::::H     E::::::::::::::::::::E     N::::::N       N:::::::N               S::::::SSSSSS:::::S     K:::::::K    K:::::K     I::::::::I     P::::::::P                                                                              
      T:::::::::T           H:::::::H     H:::::::H     E::::::::::::::::::::E     N::::::N        N::::::N               S:::::::::::::::SS      K:::::::K    K:::::K     I::::::::I     P::::::::P                                                                              
      TTTTTTTTTTT           HHHHHHHHH     HHHHHHHHH     EEEEEEEEEEEEEEEEEEEEEE     NNNNNNNN         NNNNNNN                SSSSSSSSSSSSSSS        KKKKKKKKK    KKKKKKK     IIIIIIIIII     PPPPPPPPPP                                                                              
                                                                                                                                                                                                                                                                                  
"""