import templates
import sys

def invalid_input(input):
  """Checks inputs for empty strings or only whitespace. Returns True if invalid, else False."""
  return not input.strip()

def run_story():
  """
  Contains the entire gameplay loop of Mad-lib generation.
  """
  # Welcome text
  print("Welcome to the Mad Lib Generator!")
  print("To create a story, simply advance through the option choices. You’ll pick a genre, then choose your own words through a series of prompts. The final result will be a custom story!")
  print("Are you ready to get started?")
  print("Type “YES” to Start. Type “NO” to Quit.")
  begin = input("YES/NO: ").lower()
  print()

  if begin in ("no", "n"):
    sys.exit("See you next time!")
  elif begin in ("yes", "y"):
    print("----------")
    print()
    print("Choose a Genre")
  else:
    sys.exit("Not a valid input; please try again next time!")

  # Genre selection
  genre_choice = None
  genre_list = ['1 - Fantasy', "2 - Science Fiction", "3 - Western", "Q - Quit"]
  print("It’s a simple, easy way to further personalize your story!")

  while genre_choice is None:
    for item in genre_list:
      print(item)
    print("Enter the corresponding number or letter from the list to make your selection.")
    genre_select = input("CHOOSE: ").lower()
    invalid_genre = invalid_input(genre_select)

    # Checks for invalid input
    if invalid_genre:
      print("Oops!")
      print("That is not a valid input. Only enter a number that appears on the list, or type “Q” to quit.")
      print("Let’s try that again!")
      print()
      continue

    # Quit from genre select and confirmation
    while genre_select in ("q", "quit"):
      print()
      print("Are you sure you want to Quit?")
      print("Quitting now will abandon all story progress without saving.")
      print("Enter “BACK” to go back to the page you came from, or “QUIT” to quit and exit.")
      quit_confirm = input("Confirmation: ").lower()
      if quit_confirm in ("quit"):
        sys.exit("See you next time!")
      elif quit_confirm in ("back"):
        print()
        break
      else:
        print("Unexpected input. Try again.")
        print()

    if genre_select == "1":
      genre_choice = templates.fantasy
    elif genre_select == "2":
      genre_choice = templates.scifi
    elif genre_select == "3":
      genre_choice = templates.western
    print()

  print("----------")
  print()
  # Word input
  user_words = []
  current_index = len(user_words)
  template_length = len(genre_choice["blanks"])

  while current_index < template_length:
    for i in range(template_length):
      expected_pos = genre_choice["blanks"][current_index]
      print(f"current index: {current_index}")
      print(f"current word bank: {user_words}")
      print("Enter any word you like that matches the specified part of speech.")
      print("Or type “QUIT” to quit.")
      print("(Type your word, then press Enter)")
      word_choice = input(f"{expected_pos}: ").lower()
      invalid_word = invalid_input(word_choice)
      print()
      
      # invalid word handling   
      if invalid_word:
        print("Invalid input. Default substituted.")
        user_words.append(expected_pos)
        current_index += 1
        print()
        continue
    
      # Quit from word input and confirmation
      elif word_choice in ("quit"):
        while word_choice in ("quit"):
          #print()
          print("Are you sure you want to Quit?")
          print("QUITTING NOW WILL ABANDON ALL STORY PROGRESS WITHOUT SAVING.")
          print("You will have to spend some time starting from the beginning when you return.")
          print("Enter “BACK” to go back to the page you came from, or “QUIT” to quit and exit.")
          quit_confirm = input("Confirmation: ").lower()
          if quit_confirm == "quit":
            sys.exit("See you next time!")
          elif quit_confirm == "back":
            print()
            break
          else:
            print("Unexpected input. Try again.")
            print()

      else:
        user_words.append(word_choice)
        current_index += 1

  print("----------")
  print()
  # final story creation
  final_story = genre_choice["text"].format(*user_words)
  print("Your story:")
  print()
  print(final_story)
  print()
  input("(Press Enter to continue.)")
  print()
  print("----------")
  print()

  # reset for next loop
  user_words = []
  current_index = 0
  genre_choice = None

# story controller; restart or end
#restart_switch = 1
while True:
  run_story()

  print("That was a great story! ")
  print("Would you like to go again?")
  print("Choose fun, new words to end up with a different story every time!")
  print("Type “YES” to Restart. Type “NO” to Quit.")
  restart = input("YES/NO: ").lower()
  invalid_restart = invalid_input(restart)

  if invalid_restart:
    print("That is not a valid input.")
    print("Exiting for safety!")
    sys.exit("See you next time!")

  elif restart in ("no", "n"):
    sys.exit("See you next time!")

  elif restart in ("yes", "y"):
    print("Hurray! Let's go!")
    print()
    print("----------")
    print()
    continue
  else:
    print("Unexpected input. Exiting now.")
    sys.exit()
