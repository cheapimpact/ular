import shelve

shelfFile = shelve.open("mydata")
cats = ["Zophie", "Pooka", "Simon"]
shelfFile["cats"] = cats

print(type(shelfFile), shelfFile["cats"])
shelfFile.close()
