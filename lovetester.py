from random import randint

def test_love(your_n, crush_n):
    """get a random number and make it the love score"""
    love_score = randint(0, 100)
    print(f"{your_n} and {crush_n} love score: {love_score}%")
    if love_score == 100:
        return love_score, "Go get married like... Right now."
    elif love_score > 75:
        return love_score, "You've got a good chance :>"
    elif love_score > 50:
        return love_score, "Compatible enough..."
    elif love_score == 50:
        return love_score, "50/50.."
    elif love_score > 25:
        return love_score, "Not quite right..."
    elif love_score > 5:
        return love_score, "Maybe search for someone else.."
    elif love_score == 0:
        return love_score, "Yikes! Not Compatible at all!"
    else: 
        return love_score, "Not good..."
