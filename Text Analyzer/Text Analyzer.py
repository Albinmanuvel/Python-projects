def analyze_text(text):
  """Analyzes a given text by counting words, characters, and vowels."""
  words = len(text.split())
  chars = len(text)
  vowels = 0
  for char in text:
    if char.lower() in "aeiou":
      vowels += 1
  return {"words": words, "characters": chars, "vowels": vowels}

text = input("Enter some text: ")
analysis = analyze_text(text)
print("The text has", analysis["words"], "words,", analysis["characters"], "characters, and", analysis["vowels"], "vowels.")
