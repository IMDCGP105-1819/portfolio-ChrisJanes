import string

song = """ 
hello, hello, hello, hello, one, two, three.
goodbye, goodbye, goodbye, goodbye, three, four, five.
"""

song_1 = """Don't be so quick to walk away
Dance with me
I wanna rock your body
Please stay
Dance with me
You don't have to admit you wanna play
Dance with me
Just let me rock you
Till the break of day
Dance with me

Guy time, but I don't mind
Just wanna rock you girl
I'll have whatever you have
Come on, just give it a whirl
See I've been watching you
I like the way you move
So go ahead, girl, just do
That ass shaking thing you do

So you grab your girls
And you grab a couple more
And you all come meet me
In the middle of the floor
Said the air is thick, it's smelling right
So you pass to the left and you sail to the right

Don't be so quick to walk away
Dance with me
I wanna rock your body
Please stay
Dance with me
You don't have to admit you wanna play
Dance with me
Just let me rock you
Till the break of day
Dance with me

I don't mean no harm
Just wanna rock you girl
Make a move, but be calm
Let's go, let's give it a whirl
See it appears to me
You like the way I move
I'll tell you what I'm gonna do
Pull you close and share my groove

So you grab your girls
And you grab a couple more
And you all come meet me
In the middle of the floor
Said the air is thick, it's smelling right
So you pass to the left and you sail to the right

Don't be so quick to walk away
Dance with me
I wanna rock your body
Please stay
Dance with me
You don't have to admit you wanna play
Dance with me
Just let me rock you
Till the break of day
Dance with me

Talk to me boy
No disrespect, I don't mean no harm
Talk to me boy
I can't wait to have you in my arms
Talk to me boy
Hurry up cause you're taking too long
Talk to me boy
Bet I'll have you naked by the end of this song

So what did you come for
I came to dance with you
And you know that you don't want to hit the floor
I came to romance with you
You're searching for love forever more
It's time to take a chance
If love is here on the floor, girl

Hey
Dance with me
Yea
Come on baby

Don't be so quick to walk away
(Don't walk away)
(Come on and)
Dance with me
I wanna rock your body
(Let me rock your body)
Please stay
(Come on and)
Dance with me
You don't have to admit you wanna play
(You don't have to admit you wanna play, just)
Dance with me
Just let me rock you
(Do do do do)
Till the break of day
(Come on and)
Dance with me

Talk to me boy
No disrespect, I don't mean no harm
Talk to me boy
But I can't wait to have you in my arms
Talk to me boy
Hurry up cause you're taking too long
Talk to me boy
Bet I'll have you naked by the end of this song

Don't be so quick to walk away
(Just think of me and you)
Don't be so quick to walk away
(We could do something)
Don't be so quick to walk away
(I like the way you look right now)
Don't be so quick to walk away
(Come over here baby)

Are you feeling me?
Let's do something
Let's make a bet
Cause I, gotta have you naked by the end of this song""" 

def word_frequency(lyrics, high = -1, less = False):
    frequency = {}

    lyrics = lyrics.translate(str.maketrans('', '', string.punctuation))
    lyrics = lyrics.lower()

    words = [word.strip(string.punctuation) for word in lyrics.split()]
    
    for word in words:
        if word not in frequency:
            frequency[word] = 1
        else:
            frequency[word] += 1

    highest = high
    most_frequent = []

    sorted_words = sorted(frequency, key=frequency.get, reverse=True)

    if less == False:
        highest = frequency[sorted_words[0]]

    for word in sorted_words:
        if frequency[word] == highest:
            most_frequent.append(word)
                    
    return (most_frequent, highest)

def word_frequency_with_boundary(lyrics, boundary):
    result = []

    (_, highest) = word_frequency(lyrics)

    if boundary > highest:
        return result

    for n in range(highest, boundary-1, -1):
        (freq, count) = word_frequency(lyrics, n, True)
        
        if len(freq) > 0:
            result.append((freq, count))

    return result

print(word_frequency_with_boundary(song, 2))