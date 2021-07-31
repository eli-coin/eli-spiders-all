from Crypto.Cipher import AES

def aes_decode(data, key):
    """AES解密
    :param key:  密钥（16.32）一般16的倍数
    :param data:  要解密的数据
    :return:  处理好的数据
    """
    cryptor = AES.new(key, AES.MODE_CBC, key)
    plain_text = cryptor.decrypt(data)
    return plain_text.rstrip(b'\0')  # .decode("utf-8")

if __name__ == '__main__':
    src='ts_list/0.ts'
    dec='ts_list/0_de.ts'
    key='xxxx'
    print(len(key))
    with open(src,"rb") as f:
        content = f.read()

    res = aes_decode(content,key)
    with open(dec,"wb") as f2:
        f2.write(res)