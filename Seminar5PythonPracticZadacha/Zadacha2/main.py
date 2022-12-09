
# 3) Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#
# Входные данные хранятся в отдельных текстовых файлах.
# stroka = "aaabbbbccbbb"
# ....
# stroka = "3a4b2c3b"
# Восстановить
# Ввёл: stroka = "3a4b2c3b"
# Вывод: stroka = "aaabbbbccbbb"

# import string
# >>> string.ascii_uppercase
# 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# >>> string.ascii_lowercase
# 'abcdefghijklmnopqrstuvwxyz'
# >>> string.ascii_letters
# 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# ord('ö') -> 246
# chr(65) - > A




def EncodeOrdChr(text):
    result = ""
    samplerChr = "abcdefghijklmopqrstuvwxyzABCDEFGHIJKLMOPQRSTUVWXYZ"
    textListSplit = list(text)
    # print(textListSplit)
    for symbol in textListSplit:
        result += str(f'{ord(symbol)}{samplerChr[0]}')+"\\n"
        samplerChr = samplerChr[1:]+samplerChr[0]
    # print(result)
    return result

def DecodeOrdChr(text):
    result = ""
    textSplit = text.split("\\n")
    textSplit.pop(len(textSplit)-1)
    textSplit = [textSplit[i][:-1] for i in range(len(textSplit))]
    # print(textSplit)
    for number in textSplit:
        result += chr(int(number))
    # print(result)
    return result

# print("EncodeOrdChr: "+EncodeOrdChr(r"GeeksforGeeks")) # зашифровать, encrypt, кодировать, encode
# print("DecodeOrdChr: "+DecodeOrdChr(r"71a\n101b\n101c\n107d\n115e\n102f\n111g\n114h\n71i\n101j\n101k\n107l\n115m\n")) # расшифровать, decrypt, декодировать, decode



# https://tonais.ru/osnovy/kodirovanie-dlin-seriy-rle-python

# rle-encode.py
def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 1
    if not data: return ''
    for char in data:
        # If the prev and current characters
        # don't match...
        if char != prev_char:
            # ...then add the count and character
            # to our encoding
            if prev_char:
                if str(count) != "1":
                    encoding += str(count) + prev_char
                else:
                    encoding += prev_char
            count = 1
            prev_char = char
        else:
            # Or increment our counter
            # if the characters do match
            count += 1
    else:
        # Finish off the encoding
        if str(count) != "1":
            encoding += str(count) + prev_char
        else:
            encoding += prev_char
        return encoding

# rle-decode.py
def rle_decode(data):
    decode = ''
    count = ''
    for char in data:
        # If the character is numerical...
        if char.isdigit():
            # ...append it to our count
            count += char
        else:
            # Otherwise we've seen a non-numerical
            # character and need to expand it for
            # the decoding
            try:
                decode += char * int(count)
            except ValueError:
                decode += char * int(1)
            count = ''
    return decode

with open("input.txt",'r',encoding="utf-8") as f:
   fText = f.read().split("\n")

fOutDecode = open("outputDecode.txt",'w',encoding="utf-8")
fOutDecode.close()
fOutDecode = open("outputDecode.txt",'a+',encoding="utf-8")

fOutEncode = open("outputEncode.txt",'w',encoding="utf-8")
fOutEncode.close()
fOutEncode = open("outputEncode.txt",'a+',encoding="utf-8")

fOutEncDecode = open("outputEncDecode.txt",'w',encoding="utf-8")
fOutEncDecode.close()
fOutEncDecode = open("outputEncDecode.txt",'a+',encoding="utf-8")

fOutDecEncode = open("outputDecEncode.txt",'w',encoding="utf-8")
fOutDecEncode.close()
fOutDecEncode = open("outputDecEncode.txt",'a+',encoding="utf-8")

for text in fText:
    fOutDecode.write(rle_decode(text) + "\n")
    # fOutDecode.write(DecodeOrdChr(text) + "\n")
    fOutEncode.write(rle_encode(text) + "\n")
    # fOutEncode.write(EncodeOrdChr(text) + "\n")
    fOutDecEncode.write(rle_encode(rle_decode(text)) + "\n")
    # fOutDecEncode.write(EncodeOrdChr(DecodeOrdChr(text)) + "\n")
    fOutEncDecode.write(rle_decode(rle_encode(text)) + "\n")
    # fOutEncDecode.write(DecodeOrdChr(EncodeOrdChr(text)) + "\n")

fOutDecode.close()
fOutEncode.close()
fOutDecEncode.close()
fOutEncDecode.close()




# import urllib.parse
#
# fText = "Александр Пушкин начал писать свои первые произведения уже в семь лет. В годы учебы в Лицее он прославился, когда прочитал свое стихотворение Гавриилу Державину. Пушкин первым из русских писателей начал зарабатывать литературным трудом. Он создавал не только лирические стихи, но и сказки, историческую прозу и произведения в поддержку революционеров - за вольнодумство поэта даже отправляли в ссылки."
# print(fText)
# query = fText
# result1 = urllib.parse.quote(query)
# final1result = urllib.parse.unquote_plus(result1)
#
# result2 = urllib.parse.quote_plus(query)
# final2result =urllib.parse.unquote_plus(result2)
#
# print(result1,final1result,result2,final2result,sep="\n")
