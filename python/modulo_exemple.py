def check_bank(iban):
    bban = iban[4]
    verif = int(bban[-2:])
    number = int(bban[:-2])

    return number % 97 == verif

print(check_bank(""))
