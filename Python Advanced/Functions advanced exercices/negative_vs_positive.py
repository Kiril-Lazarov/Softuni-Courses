def neg_vs_pos(args):
    words1 = ''
    words2 = ''
    sequence = [int(x) for x in args.split()]
    positives = sum([x for x in sequence if x >0])
    negatives = sum([x for x in sequence if x <0])
    print(negatives)
    print(positives)
    if positives > abs(negatives):
        words1 = 'positives'
        words2 = 'negatives'
    elif positives < abs(negatives):
        words1 = 'negatives'
        words2 = 'positives'
    return f"The {words1} are stronger than the {words2}"

print(neg_vs_pos(input()))
