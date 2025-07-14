import time

def typing_test():
  prompt_text= "The little bunny rabbit was faster than turtle but still the turtle won the race through determination"
  print("Typing Speed Test")
  print("------------------")
  print(f"Type the following:\n{prompt_text}\n")
  input("Press Enter when you’re ready...")
  
  start_time = time.time()
  user_input= input("\nstart typing here:\n")
  end_time=time.time()
  
  elapsed_time = end_time - start_time
  words = len(prompt_text.split())
  wpm = (words / elapsed_time) * 60
  print(f"\nYour time: {elapsed_time:.2f} seconds")
  print(f"\nYour speed: {wpm:.2f} words per minute")
  print(f"\nYour input was:\n{user_input}")
  
  if user_input == prompt_text:
      print("\nPerfect! No mistakes.")
  else:
      print("\nYou made some mistakes. Try again!")

typing_test()




