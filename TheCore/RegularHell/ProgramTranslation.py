def programTranslation(solution, args):
    argumentVariants = '|'.join(args)
    pattern = r'\b((?<!\$)({}))\b'.format('|'.join(args))
    repl = r'$\1'
    return re.sub(pattern, repl, solution)
