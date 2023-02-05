import spacy 

nlp = spacy.load('en_core_web_sm')


# garden path sentences examples were too short so i used random sentences from wikipedia
gardenpathSentences = ["Because of crowding within the executive mansion itself, President Theodore Roosevelt had all work offices relocated to the newly constructed West Wing in 1901. Eight years later, in 1909, President William Howard Taft expanded the West Wing and created the first Oval Office, which was eventually moved as the section was expanded.",
"In February 1754, Dinwiddie promoted Washington to lieutenant colonel and second-in-command of the 300-strong Virginia Regiment, with orders to confront French forces at the Forks of the Ohio.[39] Washington set out for the Forks with half the regiment in April and soon learned a French force of 1,000 had begun construction of Fort Duquesne there.",
"Over thousands of years, American Indians periodically inhabited the lands that today make up Ferry Farm. Archaeological finds include a spear point made over 10,000 years ago by a big-game hunter, numerous tools associated with bands of hunter/gatherers, and pottery created by native farmers.",
"Betty's mother Mary Ball Washington was buried on the grounds, which she had liked to visit. Lewis descendants sold the house and property in 1797 after Betty Washington Lewis' death. A memorial was erected in 1894 at the Mary Ball Washington gravesite.",
"At dawn on May 6, Hancock attacked along the Plank Road, driving Hill's Corps back in confusion, but the First Corps of Lieutenant General James Longstreet arrived in time to prevent the collapse of the Confederate right flank."
]

for sentence in gardenpathSentences:
    doc = nlp(sentence)
    print("*********************")
    print("Sentence:")
    print(sentence)
    print() 
    print("Tokens:")
    print([token.orth_ for token in doc])
    print()
    print("Entities")
    print([(i, i.label_, i.label) for i in doc.ents])
    print()



# Two unusual entities I seen were: 
#   FAC, e.g. "The Plank Road", which are "Buildings, airports, highways, bridges, etc."
#   NORP, e.g. "American Indians", which are "Nationalities or religious or political groups."
