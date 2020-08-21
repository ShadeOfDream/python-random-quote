import random

def primary():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = len(quotes) - 1
  rnd = random.randint(0, last)
  #rnd1 = random.randint(0, last)
  #rnd2 = random.randint(0, last)

  print(quotes[rnd])
  #print(quotes[rnd1], end='')
  #print(quotes[rnd2])

  #f = open("quotes.txt", "a")
  #f.write("New quote!")
  #f.close()

if __name__== "__main__":
  primary()
