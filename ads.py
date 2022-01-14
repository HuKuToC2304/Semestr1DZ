import random 
player_score = 0 
computer_score = 0 
choices = ["камень", "бумага", "ножницы"]
print("Камень давит ножницы. Ножницы режут бумагу. Бумага кроет камень.")
player = input("Выберите: камень, бумага или ножницы (выйти) ")
while player != "выйти":
	player = player.lower()
	computer = random.choice(choices)
	print("Твой выбор " +player+ ", компьютер выбрал " +computer+ ".")
	if player == computer:
		print("Ничья")
	elif player == "камень":
		if computer == "ножницы":
			print("Ты победил!")
			player_score = player_score + 1 
		else:
			print("Победил компьютер!")
			computer_score = player_score + 1  
		print("Общий счет: у вас ", player_score, "у компьютера", computer_score)
	elif player == "бумага":
		if computer == "камень":
			print("Ты победил!")
			player_score = player_score + 1 
		else:
			print("Победил компьютер!")
			computer_score = computer_score + 1
		print("Общий счет: у вас ", player_score, "у компьютера", computer_score)
	else:
		print("По-моему, произошла ошибка...")
	print()
	player = input("Выберите: камень, бумага или ножницы (выйти)? ")






















