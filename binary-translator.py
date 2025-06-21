while True:
    binary = input("Zadej binární kód (nebo 'break' pro ukončení): ")
    if binary.lower() == "break":
        break
    try:
        text = ''.join([chr(int(b, 2)) for b in binary.split()])
        print("Překlad:", text)
    except ValueError:
        print("⚠️ Chybný binární vstup – zkontroluj mezery a správné 8bitové bloky.")
