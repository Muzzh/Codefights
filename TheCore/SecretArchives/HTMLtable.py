def htmlTable(table, row, column):
    import re
    q = r'>\w+<'
    tot = len(re.findall(q,table))
    q = r'<tr>'
    num_row = len(re.findall(q,table))
    td_per_row = tot / num_row
    temp = '(?:(\w+)(?:</td><td>))'*(td_per_row-1)
    p = r'(?:<tr><td>)' + temp + r'(\w+)(?:</td></tr>)'
    headers = len(re.findall(r'(?:<tr><th>)',table))
    print headers
    tab = re.findall(p,table)
    try:
        return tab[row+headers][column]
    except IndexError:
        return 'No such cell'
    
