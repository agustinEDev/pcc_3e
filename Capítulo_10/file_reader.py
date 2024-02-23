from pathlib import Path

path = Path('../files/pi_digits.txt')
content = path.read_text()

print(content)