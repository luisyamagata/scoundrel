def regras():
    print('''Scoundrel - version 1.0 August 15th, 2011 - A Single Player Rogue-like Card Game by Zach Gage and Kurt Bieg - This virtual version was developed by Luis Yamagata
          The deck is called the Dungeon. You start with 20 health points. We'll keep track of it for you.
          The 26 Clubs and Spades in the deck are Monsters. Their damage is equal to their ordered value. (e.g.
        10 is 10, Jack is 11, Queen is 12, King is 13, and Ace is 14)
        The 9 Diamonds in the deck are Weapons. Each weapon does as much damage as its value. All
        weapons in Scoundrel are binding, meaning if you pick one up, you must equip it, and discard your
        previous weapon.
        The 9 Hearts in the deck are Health Potions. You may only use one health potion each turn, even if you
        pull two. The second potion you pull is simply discarded. You may not restore your life beyond your
        starting 20 health.
        You may locate the discard deck (any discarded cards) anywhere you wish, though I recommend to the
        right of the Room. Cards are discarded face down.
        The Game ends when either your life reaches 0 or you make your way through the entire Dungeon.
          Scoring: 

        - If your life has reached zero, find all the remaining monsters in the Dungeon, and subtract
        their values from your life, this negative value is your score.
        - If you have made your way through the entire dungeon, your score is your positive life, or if
        your life is 20, and your last card was a health potion, your life + the value of that potion.

        Gameplay:
        On your first and every turn, flip over cards off the top of the deck, one by one, until you have 4 cards face
        up in front of you to make an Room.
        You may avoid the Room if you wish. If you chose to do so, scoop up all four cards in one motion and
        place them at the bottom of the Dungeon. While you may avoid as many Rooms as you want, you may
        not avoid two Rooms in a row.
        If you choose not to avoid the Room, one by one, you must face 3 of the four cards it contains.
        Take them one at a time.
        If you chose a Weapon...
        You must equip it. Do this by placing it face up between you and the remaining Room cards. If you had a
        previous Weapon equipped, move it and any Monsters on it to the discard deck.
        If you chose a Health Potion...
        Add its number to your health, and than discard it. Your health may not exceed 20, and you may not use
        more than one Health Potion per turn. If you take two Health Potions on a single turn, the second is
        simply discarded, adding nothing to your health.
        If you chose a Monster...
        You may either fight it barehanded or with an equipped Weapon.
          Combat

        - If you choose to fight the Monster barehanded, subtract its full value from your Health, and
        move the Monster to the discard deck.
        - If you choose to fight the Monster with your equipped Weapon, place the monster face up on
        top of the weapon (and on top of any other Monsters on the Weapon. Be sure to stagger the
        placement of the Monster so that the Weapon's number is still showing. subtract the
        Weapon's value from the Monster's value and subtract any remaining value from your health.
        ! For example, if your Weapon is a 5, and you place a 3 Monster on it, you take no damage. ( 3-5 < 0)
        ! If your Weapon is a 5 and you place a Jack Monster on it, you take 6 damage. ( 11 - 5 = 5 dmg)
        It is important to note that although you retain your weapons until they are replaced, once a
        Weapon is used on a monster, the Weapon can then only be used to slay Monsters of a lower
        value (less than equal) than the previous Monster it had slain.
        ! For example, if your 5 Weapon has killed a Queen Monster and you then choose a 6 Monster, you
        ! may use !your Weapon on the 6 Monster, as 6 is less than 12.
        ! But, if you have used your 5 Weapon on a 6 Monster, and you then choose a Queen Monster,
        ! you must fight the Queen barehanded as Queen,12, is greater than 6. Despite this, the Weapon is not
        ! discarded, as it could still be used against Monsters weaker than a 6.

        Once you have chosen 3 cards (such that only one remains), your turn is complete. Leave the fourth card
        face up in front of you as part of the next Room.''')