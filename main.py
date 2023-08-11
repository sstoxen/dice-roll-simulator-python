import random


def roll_dice(amount: int = 2) -> list[int]:
  if amount <= 0:
    raise ValueError
  rolls: list[int] = []
  for i in range(amount):
    random_roll: int = random.randint(1, 6)
    rolls.append(random_roll)

  return rolls


def main():
  finished = False
  while not finished:
    try:
      user_input: str = input("Home many dice would you like to roll (exit to be done)? ")
      if user_input.lower() == "exit":
        print("Thanks for playing!")
        finished = True
      else:
        dice_values = roll_dice(int(user_input))
        dice_total = 0
        for die in dice_values:
          dice_total += die
        print("Dice values:", *dice_values)
        print("Total:", dice_total)
    except ValueError:
      print("(Please enter a valid integer)")


if __name__ == "__main__":
  main()
