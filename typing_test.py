import time

def typing_test():
  prompt_text= "The little bunny rabbit was faster than turtle but still the turtle won the race through determination"
  print("Typing Speed Test")
  print(f"Type the following:\n{prompt_text}\n")
  enter= input("Press Enter when you’re ready...")
  
  start_time = time.time()
  user_input= input("start typing here:\n")
  end_time=time.time()
  
  elapsed_time = end_time - start_time
  words = len(prompt_text.split())
  wpm = (words / elapsed_time) * 60

typing_test()






