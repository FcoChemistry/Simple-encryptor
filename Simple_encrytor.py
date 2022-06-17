def chyper (plaintext, k):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypt = ''
    t = plaintext.lower()
    for ch in t:
        if ch in alphabet:
            x = alphabet.find(ch)  + k
            if x >= 25:
                let = alphabet[-26+k]
                encrypt = encrypt + let
            else:
                let = alphabet[x]
                encrypt = encrypt + let
        else:
            encrypt = encrypt + ch

    return encrypt
