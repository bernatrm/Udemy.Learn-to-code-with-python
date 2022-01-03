capitals = {
    "New York": "Albany",
    "California": "Sacramento",
    "Texas": "Austin"
}

inverted = { captial: state for state, captial in capitals.items() if len(state) != len(captial) }
print(inverted)