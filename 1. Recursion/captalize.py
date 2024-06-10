def capitalizeWord(a):
    if len(a) == 1:
        return str(a[0]).capitalize()
    return capitalizeWord([a[0]]) + " " + capitalizeWord(a[1:])


a = "abc new text"  # Abc New Text
print(capitalizeWord(a.split(" ")))
