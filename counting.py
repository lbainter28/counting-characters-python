char_count = []
orig_str = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc accumsan sem ut ligula scelerisque sollicitudin. Ut at sagittis augue. Praesent quis rhoncus justo. Aliquam erat volutpat. Donec sit amet suscipit metus, non lobortis massa. Vestibulum augue ex, dapibus ac suscipit vel, volutpat eget massa. Donec nec velit non ligula efficitur luctus."""

str_list = list(orig_str)

for char in str_list:
    char_count.append({'char': char, 'count': str_list.count(char)})

for charinfo in char_count:
    print charinfo['char'] + ": " + str(charinfo['count'])