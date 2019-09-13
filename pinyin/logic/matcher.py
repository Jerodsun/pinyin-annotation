def match_pinyin(ch_chars, model):
    """Take the parsed input and try/catch match with database."""
    chars = list(ch_chars) # We take all the chars including whitespace

    # load database each time?

    ls = []

    for i in chars:
        # if i matches in database, add corresponding pinyin else null
        try:
            character = model.objects.get(character=i)
            ls.append( (i, character) )
        except (model.DoesNotExist):
            ls.append( (i, None) )

    return ls
