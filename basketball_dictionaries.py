class Player:
    def __init__(self, dictionary):
        self.name =  dictionary["name"]
        self.age =  dictionary["age"]
        self.position =  dictionary["position"]
        self.team =  dictionary["team"]

    def display_player(self):
        print("$*$*$*$*$*$*$*$*$*$*$**$*$*$*$*$*")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Position:", self.position)
        print("Team:", self.team)
kevin = {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
}
jason = {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving", 
    "age":32,
        "position": "Point Guard", 
    "team": "Brooklyn Nets"
}

# Create your Player instances here!
# player_jason = ???

player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)

player_kevin.display_player()
player_jason.display_player()
player_kyrie.display_player()