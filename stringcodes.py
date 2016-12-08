#! /usr/bin/python3
# _encoding:utf-8_
# Written by liuzhaoyang
# wcontact:liu575563079@gmail.com
# python字符的编码与解码

if __name__ == "__main__":
    input_bytes = b'\xff\xfe4\x001\x003\x00 \x00i\x00s\x00 \x00i\x00n\x00.\x00'
    input_char = input_bytes.decode('utf-16')
    print(str(input_char))

    out_put = 'we are doing the great thing!\n'
    out_put_bytes = out_put.encode('utf-8')
    print(out_put_bytes)
    with open('bytes.txt','wb') as file:
        file.write(out_put_bytes)

