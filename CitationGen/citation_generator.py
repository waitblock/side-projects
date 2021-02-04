#an old project i made because i was fed up with having to wait for a website to make me a citation
print("Welcome to the MLA 8 Citation Maker!")
first_name = input("Author's first name: ")
last_name = input("Author's last name: ")
title = input("Title of book: ")
title = '''"'''+(title)+ '''"'''
publisher = input("Name of publisher: ")
date_of_publish = input("Publication date: ")
print((last_name), (first_name),(title), (publisher), (date_of_publish), sep=", ")
