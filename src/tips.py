from pathlib import Path

src_path = Path(__file__).parent
tipstxt_path = src_path / 'tips.txt'

with open(tipstxt_path, 'r') as file:
    TIPS = file.readlines()
