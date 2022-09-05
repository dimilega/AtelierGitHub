import termcolor

for color in termcolor.COLORS.keys():
    print(termcolor.colored("Hello!", color))
EOF
