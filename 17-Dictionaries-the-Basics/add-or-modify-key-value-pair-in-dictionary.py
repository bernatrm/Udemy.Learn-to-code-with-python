sports_team_rosters = {
    "New England Patriots": ["Tom Brady", "Rob Gronkowski", "Julian Edelman"],
    "New York Giants": ["Eli Manning", "Odell Beckham"]
}

# print(sports_team_rosters["Pittsburgh Steelers"])
sports_team_rosters["Pittsburgh Steelers"] = ["Ben Roethlisberger", "Antonio Brown"]
# print(sports_team_rosters["Pittsburgh Steelers"])
# print(sports_team_rosters)

sports_team_rosters["New England Patriots"] = ["Eli Manning"]


video_game_options = {} # same that = dict()
# video_game_options = dict() # Create Empty Dictionary or convert object in Dictionary

video_game_options["subtitles"] = True
video_game_options["difficulty"] = "Medium"
video_game_options["volume"] = 7
print(video_game_options)

video_game_options["difficulty"] = "Hard"
video_game_options["subtitles"] = False
video_game_options["Volume"] = 10 # Case-sentitive, create a new Key
print(video_game_options)


words = ["danger", "beware", "danger", "beware", "beware"]

def count_words(words):
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

print(count_words(words))