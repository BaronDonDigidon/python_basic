import re
from typing import List

with open('examples.html', 'r') as f:
    text = f.read()

pattern: str = r"<h3.*?>(.*?)</h3>"
matches: List[str] = re.findall(pattern, text, re.DOTALL)
headings: List[str] = [match.strip() for match in matches]
print(headings)
