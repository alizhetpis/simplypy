commentators = {}
while True:
    comment = input()
    if comment == "":
        break
    name = comment.split(":")[0].strip()
    if name not in commentators:
        commentators[name] = None

print("Уникальных комментаторов:", len(commentators))
