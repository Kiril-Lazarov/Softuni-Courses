def vowel_filter(function):
    def wrapper():
        res = function()

        return [x for x in res if x.lower() in "aeiou"]
    return wrapper
@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())



