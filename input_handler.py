from re import X
import sys
 
def get_input ():
    while True:
        try:
            x=int(sys.stdin.readline())
        except Exception:
            print("Please insert only intiger value of coordinate")
            continue
        break
    
    return x