import textwrap

def wrap(string, max_width):
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

if __name__ == '__main__':
    string, max_width = "bscnksbcjscksbcjksbckjdscsbdcbsdkjbcsdjcbsdjkcbsdkjbckjdsbjksd",9
    result = wrap(string, max_width)
    print(result)

