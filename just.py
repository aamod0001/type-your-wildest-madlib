def madlib():
    # Initialize lists
    noun = [""] * 3
    noun_plural = [""] * 3
    adjective = [""] * 2
    verb_ending_in_ing = [""] * 2
    
    # Input for nouns and plural nouns
    for _ in range(3):
        noun[_] = input("Enter noun: ")
        noun_plural[_] = input("Enter noun plural: ")
    
    # Input for adjectives and verbs ending in -ing
    for _ in range(2):
        adjective[_] = input("Enter adjective: ")
        verb_ending_in_ing[_] = input("Enter verb ending in –ing: ")
    
    # Other inputs
    relatives_name = input("Enter relative's name: ")
    adverb_ending_in_noun_plural = input("Enter adverb ending in noun, plural: ")
    exclamation = input("Enter exclamation: ")
    large_number = input("Enter large number: ")
    celebrity_name = input("Enter celebrity name: ")
    verb = input("Enter verb: ")
    something_slimy = input("Enter something slimy: ")
    body_part_plural = input("Enter body part, plural: ")
    past_noun_plural_tense_verb = input("Enter past noun, plural tense verb: ")
    
    # Print the story
    print(f"I was going to be rich! I had just invented the first electric {noun[1]}. "
          f"Using a(n) {noun[0]} from {relatives_name}’s toolbox, I built it out of old {noun_plural[0]}, "
          f"metal {noun_plural[1]}, and rubber {noun[2]}. "
          f"The first time I turned it on, the machine worked {adverb_ending_in_noun_plural}. "
          f"I couldn’t believe it! “{exclamation}!” I yelled, {verb_ending_in_ing[1]} up and down. "
          f"I invited a(n) {adjective[1]} billionaire to check out my invention. "
          f"I couldn’t wait to sell it for {large_number} million dollars and live like {celebrity_name}. "
          f"But when I turned it on, something went terribly {adjective[0]}. "
          f"The machine started {verb_ending_in_ing[0]} and began to {verb}. "
          f"Suddenly it spewed {something_slimy} and shot slices of {noun[2]} in all directions. "
          f"The billionaire started screaming at the top of his {body_part_plural} and {past_noun_plural_tense_verb} out of my lab. "
          f"Good thing I still get my weekly allowance.")

if __name__ == "__main__":
    madlib()
