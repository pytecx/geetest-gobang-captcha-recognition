
# Gobang Captcha Recognition

Solves the captcha made by Geetest called **GoBang**.


## Information

The captcha is a 5x5 grid game where the goal is to arrange five identical items in a row, either horizontally, vertically, or diagonally.

The grid is represented by a 2D array where each cell contains a ball represented by a number (1-4), or a empty cell represented by 0.

**Array Representation**
```python
game = [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]
```

**Table Representation**

| Number | Represents     |
|--------|----------------|
| 0      | Empty Cell    |
| 1      | Blue Ball      |
| 2      | Yellow Ball    |
| 3      | White Ball     |
| 4      | Black Ball     |

**Image Representation**

![Image Representation](https://cdn.discordapp.com/attachments/1114209716705435711/1185229644241313862/gobang.png?ex=658eda1f&is=657c651f&hm=810c515db50aecb50a2eed91ee7d85e08fe37cb1e4a1939a048d5c51bf74cf41&)


## Solution

1. Identify all empty spaces and the positions of each type of item.
2. For each item, check if moving it to any of the empty spaces will result in five of the same items in a row.
3. If a valid move is found, return the source and destination coordinates.
## Usage

```python
import requests
import uuid
import time
import json
import re
from gobang import solve_captcha

captcha_id = ""

def get_captcha(captchaId):
  timestamp = round(time.time() * 1000)
  challenge = str(uuid.uuid4())
  resp = requests.get(url="https://gcaptcha4.geetest.com/load", params={
      "callback": "geetest_{}".format(timestamp),
      "captcha_id": captchaId,
      "challenge": challenge,
      "client_type": "web",
      "risk_type": "winlinze",
      "lang": "en",
  })
  pattern = re.compile(r'geetest_\d+\((.*)\)')
  match = pattern.search(resp.text)
  if match:
    return json.loads(match.group(1))
  else:
    return None

captcha = get_captcha(captcha_id)
game = captcha["data"]["ques"]
result = solve_captcha(game)

print("Input: {} | Output: {}".format(game, result))
```
## Note

This repository just recognises the answer for the captcha, it does not provide a full working solution to solve it.
