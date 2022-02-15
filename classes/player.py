class Player:
    def __init__(self, botPlay:bool):
        self.botPlay = botPlay
    
    def start(self):
        """Starts the game"""
        if self.botPlay:
            self.botStart()
        else:
            self.humanStart()
    
    def botStart(self) -> None:
        """starts the game in bot mode

        Raises:
            ValueError: if the choice is not valid (rock, paper or scissors) then it will raise an error
        """
        import random
        print("The bot is picking what to play...")
        options = ["rock", "paper", "scissors"]
        self.choice = options[random.randint(0,2)]
        print("The bot has picked")
        print(f'The bot has played {self.choice}')
        hummanChoice = input("Rock, paper or scissors? ")
        if hummanChoice.lower() in options:
            self.humanChoice = hummanChoice.lower()
        else:
            raise ValueError("Invalid Choice")
        print(f'You have played {self.humanChoice}')
        if self.checkChoice(self.humanChoice, self.choice):
            print("You won!")
        else:
            print("You lost!")


    def humanStart(self) -> None:
        """starts the game in human mode"""
        import time
        from os import system
        print("Player 1: START")
        player1 = input("Rock, paper or scissors?\n>>> ").lower()
        system("cls")
        print("Player 2: START")
        player2 = input("Rock, paper or scissors?\n>>> ").lower()
        system("cls")
        if self.checkChoice(player1, player2):
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")

    def checkChoice(self, choice1:str, choice2:str) -> bool:
        """Checks the choice of the player

        Args:
            choice1 (str): The choice for (player)1
            choice2 (str): The choice for (player)2

        Raises:
            ValueError: if the choice is not valid (rock, paper or scissors) then it will raise an error

        Returns:
            bool: True if (player)1 wins and false if (player)2 wins
        """
        if choice1 == choice2:
            return True
        elif choice1 == "rock" and choice2 == "paper":
            return False
        elif choice1 == "rock" and choice2 == "scissors":
            return True
        elif choice1 == "paper" and choice2 == "rock":
            return True
        elif choice1 == "paper" and choice2 == "scissors":
            return False
        elif choice1 == "scissors" and choice2 == "rock":
            return False
        elif choice1 == "scissors" and choice2 == "paper":
            return True
        else:
            raise ValueError("Invalid Choice")
    

