from pathlib import Path
import json
import sys
sys.path.append('../files/')

numbers = [2, 3, 5, 7, 11, 13]
path = Path('../files/numbers.json')
contents = json.dumps(numbers)
path.write_text(contents)