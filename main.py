def word_count(text):
  return len(text.split())

def unique_letter_count(text):
  letter_map = dict()

  for c in text.lower():

    if c == ' ' or not c.isalpha():
      continue

    try:
      letter_map[c] += 1
    except KeyError:
      letter_map[c] = 1

  return letter_map

def book_report(text):
  wc=word_count(text)
  unique_letter_map=unique_letter_count(text)
  
  report_list = [
    { "name": letter, "count": lc } for letter, lc in unique_letter_map.items()
  ]

  sort_on=lambda dict: dict["count"]
  report_list.sort(reverse=True, key=sort_on)

  print("--- Begin report of books/frankenstein.txt ---\n")
  print(f"{wc} words found in the document\n")

  for letter in report_list: 
    name, count = letter.values()
    print(f"The {name} character was found {count} times")

  print("\n-- end report --")

def main():
  with open("./books/frankenstein.txt") as file:
      text = file.read()
      book_report(text)

if __name__ == "__main__":
    main()
