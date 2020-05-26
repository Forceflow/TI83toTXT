from pathlib import Path
import sys
import tokens

def bytes_debug_explicit(b) :
    # variable passed was a single int : convert it to byte
    if isinstance(b, int):
        b = b.to_bytes(1, 'big')
    result = ""
    count = 0
    for b_element in b:
        count+=1
        result += format(b_element,'08b') + " "
        if (count % 8 == 0): result += "\n"
    return result.rstrip("\n")

def bytes_debug_hex(b, groupby=1) :
    # variable passed was a single int : convert it to byte
    if isinstance(b, int):
        b = b.to_bytes(1, 'big')
    result = ""
    count = 0
    for b_element in b:
        count+=1
        result += '{:02x}'.format(b_element)
        if (count % groupby == 0):
            result += " "
    return result.rstrip("\n")

def main() :
    if(len(sys.argv) < 2):
        print("Syntax: TI83toTXT.py (filename)")
        exit(1)
    print("Parsing", sys.argv[1])
    data = Path(sys.argv[1]).read_bytes()
    checkFixedHeader(data)

def checkFixedHeader(data):
    # First 11 bytes should read "**TI83F*"
    spec_b = data[0:11]
    if (spec_b == bytes.fromhex("2a2a54493833462a1a0a00")) :
        print("Header is **TI83F* 0x1a 0x0A 0x00")
    # Next 42 bytes are comment
    comment_b = data[11:52]
    # print(bytes_debug_explicit(comment_b))
    # print(bytes_debug_hex(comment_b, groupby=2))
    print("Comment is \"", str(comment_b.decode('utf-8')), "\"", sep="")

if __name__ == "__main__": main()