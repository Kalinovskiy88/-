ED = input("[E]ncrypt|[D]ecrypt: ").upper()
if ED not in ['E','D']:
	print("Ошибка: режим не выбран"); raise SystemExit

Message = input("Введите сообщение:").upper()
key = input("Введите ключ:")

def encryptDecrypt(mode, message, key, final = ""):
	key *= len(message) // len(key) + 1
	for index, symbol in enumerate(message):
		if mode == 'E':
			temp = ord(symbol) + int(key[index]) -13
		else:
			temp = ord(symbol) - int(key[index]) -13
		final += chr(temp%26 + ord('A'))
	return final
print("Результат:",encryptDecrypt(ED, Message, key))
