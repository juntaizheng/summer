import random
vowels = ['a', 'e', 'i', 'o', 'u']
pre = ['Quite simply put, you are a', 'To put it nicely, you are a', 'It is time to address the elephant in the room. You are a',
        'To sugar coat it, you are a', 'Vile beast! Thou art a']

adj1 = ['artless', 'bawdy', 'beslubbering', 'bootless', 'churlish', 'cockered', 'clouted', 'craven', 'currish',
        'dankish', 'dissembling', 'droning', 'errant', 'fawning', 'fobbing', 'froward', 'frothy', 'gleeking', 'goatish',
        'gorbellied', 'impertinent', 'infectious', 'jarring', 'loggerheaded', 'lumpish', 'mammering', 'mangled',
        'mewling', 'paunchy', 'pribbling', 'puking', 'puny', 'qualling', 'rank', 'reeky', 'roguish', 'ruttish', 'saucy',
        'spleeny', 'spongy', 'surly', 'tottering', 'unmuzzled', 'vain', 'venomed', 'villainous', 'warped', 'wayward',
        'weedy', 'yeasty']
adj2 = ['base-court', 'bat-fowling', 'beef-witted', 'beetle-headed', 'boil-brained', 'clapper-clawed', 'clay-brained',
        'common-kissing', 'crook-pated', 'dismal-dreaming', 'dizzy-eyed', 'doghearted', 'dead-bolted', 'earth-vexing',
        'elf-skinned', 'fat-kidneyed', 'fen-sucked', 'flap-mouthed', 'fly-bitten', 'folly-fallen', 'fool-born', 'full-gorged',
        'guts-griping', 'half-faced', 'hasty-witted', 'hedge-born', 'hell-hated', 'idle-headed', 'ill-breeding', 'ill-nutured',
        'knotty-pated', 'milk-livered', 'motley-minded', 'mouth-breathing', 'mouth-and-nose-breathing', 'onion-eyed', 'paste-eating',
        'plaume-plucked', 'pottle-deep', 'pox-marked', 'reeling-ripe', 'rough-hewn', 'rude-growing', 'rump-fed', 'shard-borne', 'sheep-biting',
        'spur-galled', 'swag-bellied', 'tardy-gaited', 'tickle-brained', 'toad-spotted', 'unchin-snouted', 'weather-bitten', 'world-class-paste-eating']
adj3 = ['apple-john', 'baggage', 'barnacle', 'bladder', 'boar-pig', 'bugbear', 'bum-bailey', 'canker-blossom', 'clack-dish', 'clotpole',
        'coxcomb', 'codpiece', 'death-token', 'dewberry', 'dunderhead', 'elderberry', 'flap-dragon', 'flax-wench', 'flirt-gill', 'foot-licker',
        'fustilarian', 'giglet', 'gudgeon', 'haggard', 'hamster', 'harlot' 'harpy', 'hedge-pig', 'horn-beast', 'hugger-mugger', 'mugger-hugger',
        'joithead', 'lewdster', 'lout', 'maggot-pie', 'malt-worm', 'mammet', 'measle', 'minnow', 'miscreant', 'moldwarp', 'mumble-news',
        'nut-hook', 'pigeon-egg', 'pignut', 'puttock', 'pumpion', 'ratsbane', 'scum', 'scut', 'skainsmate', 'strumpet', 'varlot', 'vassal', 'whey-face', 'wagtail']
def zinger():
    string = random.choice(pre)
    temp = random.choice(adj1)
    if temp[0] in vowels:
        string = string + 'n'
    print(string + ' ' + temp + ', ' + random.choice(adj2) + ' ' + random.choice(adj3) + '!')
