mystery = {
  "a": 2
}

mystery.setdefault("A", 5)
mystery.setdefault("a", 10)
mystery.setdefault("B", 30)
mystery.setdefault("B", 40)

print(mystery)
print(mystery.get("A"))

nba_finals = {
  "Game 1": {
    "date": "05/05/2019",
    "location": "San Francisco",
    "statistics": {
      "points": 200,
      "rebounds": 20,
      "assists": 25
    }
  }
}

print(nba_finals["Game 1"]["statistics"]["rebounds"])