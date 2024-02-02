#completing challenge using for loop

file = open("Books.csv","w")
newrecord_1 = "To kill A Mockingbird, Harper Lee, 1960\n"
newrecord_2 = "A Brief History of Time, Stephen Hawking, 1988\n"
newrecord_3 = "The Great Gatsby, F. Scott Fitzgerald, 1922\n"
newrecord_4 = "The Man who Mistook His Wife for a Hat, Oliver Sacks, 1985\n"
newrecord_5 = "Pride and Prejudice, Jane Austen, 1813\n"

be_written =[ newrecord_1, newrecord_2, newrecord_3, newrecord_4, newrecord_5]
for i in be_written:
    file.write(str(i))