import textwrap

"""
Textwrap
The textwrap module provides two convenient functions: wrap() and fill().

textwrap.wrap()
The wrap() function wraps a single paragraph in text (a string) so that every line is width characters long at most.
It returns a list of output lines.

textwrap.fill()
The fill() function wraps a single paragraph in text and returns a single string containing the wrapped paragraph.
"""

def wrap(string, max_width):
    """
    output = ""
    c=1
    for i in range(0,len(string)):
        
        if c<=max_width:
            output =output+ string[i]
        else:
            output = output + "\n"
            output = output+ string[i]
            c=1
        c+=1
    return output
    """
    return textwrap.fill(string,max_width)

if __name__ == '__main__':
    string, max_width = "bscnksbcjscksbcjksbckjdscsbdcbsdkjbcsdjcbsdjkcbsdkjbckjdsbjksd",9
    result = wrap(string, max_width)
    print(result)

print(textwrap.wrap("ABCDE",2))
print(textwrap.fill("ABCDE",2))
