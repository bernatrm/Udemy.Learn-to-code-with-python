plays = ["Hamlet", "Macbeth", "King Lear"]

plays.insert(1, "Julius Caesar")
print(plays)

plays.insert(0, "Romeo and Juliet")
print(plays)

#If the index doesn't exist, simply append to the end
plays.insert(10, "A Midsummers Night's Dream") 
print(plays)