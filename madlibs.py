# trying basic python project "madlibs"

def main():
  print("It's is an madlib game guess some word, later read it. If it make sense then You are Awesome")
  country = input("country : ")
  transport = input("vehicle : ")
  tech = input("high tech : ")
  food = input("food : ")

  madlibs = f"I want to visit to {country}.\nTravel all around {country} using {transport}.\nI want to experience {tech}. Want to try a famous {food} of {country}."

  print(madlibs)

if __name__ == "__main__":
  main()