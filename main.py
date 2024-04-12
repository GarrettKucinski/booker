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

def char_dict_to_sorted_list(char_dict):
  report_list = [
    { "name": letter, "count": lc } for letter, lc in char_dict.items()
  ]

  sort_on=lambda dict: dict["count"]
  report_list.sort(reverse=True, key=sort_on)

  return report_list

def generate_book_report(text, book):
  wc=word_count(text)
  unique_char_map=unique_letter_count(text)
  sorted_char_list=char_dict_to_sorted_list(unique_char_map)

  print(f"--- Begin report of {book} ---\n")
  print(f"{wc} words found in the document\n")

  for letter in sorted_char_list: 
    name, count = letter.values()
    print(f"The {name} character was found {count} times")

  print("\n-- end report --")

def main():
  book_path="./books/frankenstein.txt"
  with open(book_path) as file:
      text = file.read()
      generate_book_report(text, book_path)

if __name__ == "__main__":
    main()
