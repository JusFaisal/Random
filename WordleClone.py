from rich.console import Console
import random


console= Console()

words = [
    "aback", "abate", "abbey", "abide", "abode", "about", "above", "abuse", "acorn", "actor",
    "adapt", "admit", "adopt", "adore", "adult", "affix", "after", "again", "agent", "agree",
    "ahead", "aisle", "alarm", "album", "alert", "alike", "alive", "allow", "alone", "along",
    "aloud", "alpha", "amaze", "amend", "angel", "anger", "angle", "angry", "ankle", "apple",
    "apply", "apron", "arise", "armed", "armor", "aroma", "array", "arrow", "aside", "asset",
    "audio", "audit", "awake", "aware", "awful", "bacon", "badge", "badly", "bagel", "baker",
    "balmy", "banjo", "basic", "batch", "beach", "beady", "beast", "begin", "being", "belly",
    "below", "bench", "berth", "bible", "bingo", "birth", "bison", "blade", "blame", "blank",
    "blaze", "blend", "bless", "blind", "blink", "bliss", "block", "blond", "blood", "bloom",
    "blown", "bluff", "blunt", "blush", "board", "boast", "bobby", "bogus", "boils", "booth",
    "boost", "booty", "bored", "borne", "bound", "bowel", "brace", "brain", "brake", "brand",
    "brave", "bread", "break", "breed", "bribe", "brick", "bride", "brief", "bring", "brisk",
    "broad", "broke", "brown", "brush", "buddy", "build", "built", "bulky", "bumpy", "bunny",
    "burnt", "burst", "bushy", "buyer", "cabin", "cable", "cacti", "caddy", "cadet", "cagey",
    "camel", "cameo", "candy", "carat", "cargo", "carve", "cause", "cease", "cedar", "chain",
    "chair", "chalk", "champ", "chant", "chaos", "charm", "chart", "chase", "cheap", "cheat",
    "check", "cheek", "cheer", "chess", "chest", "chief", "child", "chime", "china", "choir",
    "choke", "chomp", "chunk", "cider", "cinch", "civic", "civil", "claim", "clamp", "clash",
    "class", "clean", "clear", "click", "cliff", "climb", "cling", "cloak", "clock", "clone",
    "close", "cloud", "clown", "clump", "coach", "coast", "cobra", "cocoa", "colon", "color",
    "comet", "comic", "comma", "couch", "could", "count", "court", "cover", "craft", "crane",
    "crash", "crate", "crawl", "craze", "crazy", "creak", "cream", "credo", "creek", "creep",
    "crest", "crime", "crisp", "cross", "crowd", "crown", "crude", "cruel", "crush", "curve",
    "cycle", "daily", "dance", "dated", "dawn", "delay", "devil", "diary", "dirty", "ditch",
    "diver", "divis", "dizzy", "dodge", "doubt", "dough", "draft", "drain", "drake", "drama",
    "drank", "drape", "drawl", "dream", "drift", "drink", "drive", "drown", "drunk", "dryer",
    "ducky", "eagle", "early", "earth", "ebony", "edged", "edger", "eight", "eject", "elbow",
    "elder", "elite", "empty", "enemy", "enjoy", "enter", "entry", "equal", "equip", "error",
    "event", "every", "exact", "exile", "exist", "extra", "fairy", "faith", "false", "fancy",
    "feast", "fever", "fewer", "fiber", "field", "fiery", "fifty", "fight", "final", "finch",
    "first", "flame", "flank", "flash", "fling", "flint", "float", "flood", "flour", "fluff",
    "flush", "focus", "foist", "force", "forge", "forth", "forty", "found", "frail", "frame",
    "fresh", "frost", "fruit", "funny", "fussy", "gamma", "gamer", "giant", "glide", "globe",
    "glory", "gnash", "goose", "grace", "grade", "graft", "grain", "grasp", "grave", "great",
    "greed", "grief", "grind", "grove", "guard", "guess", "habit", "handy", "happy", "hardy",
    "haste", "hatch", "haunt", "heavy", "honor", "horse", "hotel", "hound", "house", "hover",
    "humor", "ideal", "image", "imply", "index", "infix", "inlet", "input", "ivory", "joint",
    "jolly", "joust", "judge", "juice", "jumbo", "jumpy", "kneel", "knock", "known", "label",
    "labor", "laser", "laugh", "layer", "leapt", "learn", "leave", "lemon", "light", "limit",
    "liver", "lofty", "lunar", "lunch", "lunge", "magic", "major", "maker", "merry", "metal",
    "miner", "minus", "mirth", "model", "moist", "mount", "mover", "music", "naked", "nasty",
    "niche", "niece", "night", "noise", "noble", "nurse", "ocean", "offer", "often", "olive",
    "order", "other", "ounce", "owner", "pacer", "piano", "place", "plane", "plant", "plate",
    "point", "poker", "press", "price", "pride", "prize", "prone", "proof", "proud", "quail",
    "query", "quick", "quiet", "quota", "quote", "radio", "range", "rapid", "reach", "ready",
    "realm", "rebel", "refit", "relax", "reply", "reset", "retro", "rider", "ridge", "risky",
    "robot", "rough", "round", "royal", "saint", "salty", "sauce", "scale", "scare", "scene",
    "scent", "scope", "score", "scout", "serve", "shape", "sharp", "sheep", "sheer", "shift",
    "shirt", "shout", "sight", "slant", "small", "smart", "smell", "smile", "snail", "snake",
    "solid", "solve", "space", "speak", "spear", "speed", "spice", "squad", "stage", "steal",
    "stone", "store", "storm", "style", "table", "tally", "taste", "tease", "thing", "think",
    "thumb", "timer", "tooth", "track", "trade", "train", "trick", "trust", "truth", "tulip",
    "uncle", "upset", "urban", "usual", "valid", "value", "vapor", "viola", "voice", "voter",
    "waste", "watch", "wheel", "whisk", "wince", "witty", "world", "write", "yield", "zebra"
]

#ANSI color codes may not work on some ide's

def game():
    count=0
    guess=str.upper(random.choice(words))
    while True:
        first=str.upper(input("Enter your guess:"))
        if first== "BAS BHAI":
            console.print(f"Game Aborted! The Word was: [green]{guess}[/green]")
            dumb=str.upper(input("Want to play again?(YES/NO)"))
            if dumb=="YES":
                return game()
            else:
                console.print("Ending Game...",style="bold red")
                break
            
            
        if len(first)!=5:     
            console.print("Error:Guess must contain 5 letters!",style="bold red")
            continue
        elif first.isalpha():
            count+=1
            lst=[False] * len(guess)

            word=[]
            for i,letter in enumerate(first):
                if letter==guess[i]:
                    word.append(f"[green]{letter}[/green]")
                    lst[i]= True
                else:
                    word.append("?")
                    
            final=[]
            for i,letter in enumerate(first):
                if word[i] !="?":
                    final.append( word[i])
                elif letter in guess:
                    matched= False
                    for j in range(len(guess)):
                        if guess[j]==letter and not lst[j]:
                            final.append(f"[yellow]{letter}[/yellow]")
                            lst[j]= True
                            matched= True
                            break
            
                    if not matched:
                        final.append(letter)
                else:
                    final.append(letter)

            console.print("".join(final))

            if first==guess:
                console.print("Diabolical Mate!",style="bold green")
                print(f"Total Guesses: {count}")
                ask=str.upper(input("Want to play again?(YES/NO)"))
                if ask=="YES":
                    return game()
                else:
                    console.print("Ending Game...",style="bold red")
                    break
                    
            else:
                console.print("Try Again",style="bold yellow")
                print(f"Enter 'bas bhai' if you want to quit")
        else:
            console.print("Enter only ALPHABETS!",style="bold red")

    input("Press Enter to exit..")

if __name__=="__main__":
    console.print("Guess the 5 Letter Word!",style="bold cyan")
    game()
