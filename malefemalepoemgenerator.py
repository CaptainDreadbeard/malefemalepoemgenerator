"""poetry line generator, by Robin Bolin
A random generator of sweet lines of cringey poetry

Tags: beginner, random, poem, word"""
import random
try:
    import pyperclip
except ImportError:
    pass

# set up constants

DESCRIPTION = ['presence', 'gait', 'smile', 'style', 'speech', 'voice', 'scent', 'intelligence', 'brain']
POSSESSIVE_PRONOUNS = ['Her', 'Their']
MALE_POSSESSIVE = ['His', 'Their']
PERSONAL_PRONOUNS = ['She', 'They']
MALE_PERSONAL = ['He', 'They']
FLOWERS = ['Roses', 'Tulips', 'Daisys', 'Indian Paintbrushes', 'Pussywillows', 'Carnations', 'Gardenias', 'Lillies', 'Hyacinths', 'Chrysanthemums', 'Daffodils', 'Sunflowers']
OBJECTS = ['A fine set of pearls', 'like they were woven by Rumpelstiltskin', 'bars of gold', 'tears of platinum', 'fine cedar', 'precious metals', 'a four-leaf clover', 'ebony', 'ivory', 'emerald', 'the finest wine', 'a vintage omega', 'crystal clear water', 'honeycombs', 'finest perfume', 'sapphire', 'myrrh', 'meadows', 'silk']
BODY_PARTS = ['eyes', 'hair', 'skin', 'hands', 'chest', 'teeth', 'jaw', 'nose', 'cheeks', 'curves', 'belly', 'navel']
ALLITERATION = ['pretty pristine', 'greatly glowing', 'lovingly luxurious', 'originally opalescent', 'energetically envigorating', 'succulently sweet', 'gorgeously glowing', 'heavenly hearth', 'shining sheen', 'kindly caring', 'titillating tickle', 'chilling charm', 'lavish lustre', 'really rambunctious']






def main():
    print('Cringey Poem Generator!')
    print('By Robin Bolin')
    print()

while True: # Keep asking until the user enters a valid key.
    print('Are you writing to a (M)an or (W)oman?')
    response = input('> ').lower()
    if response.startswith('m'):
        mode = 'male'
        break
    elif response.startswith('w'):
        mode = 'female'
        break
    print('Please enter the letter e or d.')
    

# Each of these functions returns a different type of linebreak for a woman:
def LikeLine():
    possessive = random.choice(POSSESSIVE_PRONOUNS)
    body = random.choice(BODY_PARTS)
    randomitems = random.choice(OBJECTS)
    return '{} {} were like {}'.format(possessive, body, randomitems)


def ForLine():
    allit = random.choice(ALLITERATION)
    flower = random.choice(FLOWERS)
    body = random.choice(BODY_PARTS)
    return '{} {} for {}'.format(allit, flower, body)


def RemindLine():
    pronoun = random.choice(PERSONAL_PRONOUNS)
    body = random.choice(BODY_PARTS)
    randomitems = random.choice(OBJECTS)
    return '{} had {} reminding me of {}'.format(pronoun, body, randomitems)


def FeltLine():
    flower = random.choice(FLOWERS)
    possessive = random.choice(POSSESSIVE_PRONOUNS)
    body = random.choice(BODY_PARTS)
    return '{} felt like {} {}'.format(flower, possessive, body)


def DescribeLine():
    randomitems = random.choice(OBJECTS)
    possessive = random.choice(POSSESSIVE_PRONOUNS)
    body = random.choice(BODY_PARTS)
    return '{} couldn\'t describe {} {}'.format(randomitems, possessive, body)


def MemoLine():
    flower = random.choice(FLOWERS)
    possessive = random.choice(POSSESSIVE_PRONOUNS)
    describe = random.choice(DESCRIPTION)
    return '{} recall memories of {} {}'.format(flower, possessive, describe)


def LongingLine():
    possessive = random.choice(POSSESSIVE_PRONOUNS)
    describe = random.choice(DESCRIPTION)
    randomitems = random.choice(OBJECTS)
    return '{} {} makes me long for {}'.format(possessive, describe, randomitems)


def GaveLine():
    pronoun = random.choice(PERSONAL_PRONOUNS)
    allit = random.choice(ALLITERATION)
    flower = random.choice(FLOWERS)
    return '{} gave me a feeling of {} {} on a Sunday morning.'.format(pronoun, allit, flower)

# if poem is for a female, write for female:

if mode == 'female':
    print(LikeLine())
    print(ForLine())
    print(RemindLine())
    print(FeltLine())
    print(DescribeLine())
    print(MemoLine())
    print(LongingLine())
    print(GaveLine())

# If writing for a man, print:

def MLikeLine():
    mpossessive = random.choice(MALE_POSSESSIVE)
    body = random.choice(BODY_PARTS)
    randomitems = random.choice(OBJECTS)
    return '{} {} was like {}'.format(mpossessive, body, randomitems)


def MForLine():
    allit = random.choice(ALLITERATION)
    flower = random.choice(FLOWERS)
    body = random.choice(BODY_PARTS)
    return '{} {} for {}'.format(allit, flower, body)


def MRemindLine():
    mpronoun = random.choice(MALE_PERSONAL)
    body = random.choice(BODY_PARTS)
    randomitems = random.choice(OBJECTS)
    return '{} had {} reminding me of {}'.format(mpronoun, body, randomitems)


def MFeltLine():
    flower = random.choice(FLOWERS)
    mpossessive = random.choice(MALE_POSSESSIVE)
    body = random.choice(BODY_PARTS)
    return '{} felt like {} {}'.format(flower, mpossessive, body)


def MDescribeLine():
    randomitems = random.choice(OBJECTS)
    mpossessive = random.choice(MALE_POSSESSIVE)
    body = random.choice(BODY_PARTS)
    return '{} couldn\'t describe {} {}'.format(randomitems, mpossessive, body)


def MMemoLine():
    flower = random.choice(FLOWERS)
    mpossessive = random.choice(MALE_POSSESSIVE)
    describe = random.choice(DESCRIPTION)
    return '{} recall memories of {} {}'.format(flower, mpossessive, describe)


def MLongingLine():
    mpossessive = random.choice(MALE_POSSESSIVE)
    describe = random.choice(DESCRIPTION)
    randomitems = random.choice(OBJECTS)
    return '{} {} makes me long for {}'.format(mpossessive, describe, randomitems)


def MGaveLine():
    mpronoun = random.choice(MALE_PERSONAL)
    allit = random.choice(ALLITERATION)
    flower = random.choice(FLOWERS)
    return '{} gave me a feeling of {} {} on a Sunday morning.'.format(mpronoun, allit, flower)

# if input is Male, write poem for a man

if mode == 'male':
    print(MLikeLine())
    print(MForLine())
    print(MRemindLine())
    print(MFeltLine())
    print(MDescribeLine())
    print(MMemoLine())
    print(MLongingLine())
    print(MGaveLine())

# Each of these functions returns a different type of linebreak for a man:


# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()
