def welcome_message():
  print("Hello! Welcome to the Messi Chatbot.")

def get_user_info():
  name = input("What's your name? ")
  age = input("How old are you? ")
  return name, age

def menu():
  print("\nHow can I help you?")
  print("1. Option 1")
  print("2. Option 2")
  print("3. Option 3")
  print("4. Exit")

def main():
  welcome_message()
  name, age = get_user_info()
  print(f"\nNice to meet you, {name}! You are {age} years old.")

  while True:
      menu()
      choice = input("Enter your choice (1-4): ")

      if choice == '1':
          print("You chose Option 1. Placeholder for action.")
      elif choice == '2':
          print("You chose Option 2. Placeholder for action.")
      elif choice == '3':
          print("You chose Option 3. Placeholder for action.")
      elif choice == '4':
          print("Goodbye! Have a great day.")
          break
      else:
          print("Invalid choice. Please choose a number between 1 and 4.")

if __name__ == "__main__":
  main()
