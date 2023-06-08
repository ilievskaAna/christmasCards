import os

def make_card(name):
    template = "template.txt"
    output_dir = "christmasCards"
    output_file = os.join(output_dir, name + ".txt")

    with open(template, 'r') as template_file:
        letter = template_file.read().replace("<name>", name)

    with open(output_file, 'w') as output:
        output.write(letter)

def main():
    names_file = "names.txt"
    names = []

    with open(names_file, 'r') as file:
        names = [name for name in file.readlines()]

    os.makedir("christmasCards", exist_ok=True)

    for name in names:
        make_card(name)

