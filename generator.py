import argparse
import random
import re
import os

main_function_name = "_Z5samplei"
shift_instructions = ['lsl', 'lsr', 'rol', 'ror']
arithmetic_instructions = ['add', 'sub']
logical_instructions = ['and', 'orr', 'eor']
in_filepath = "in_filepath"
num_outputs = "num_outputs"


class Regex:
    def __init__(self):
        pass


regex = Regex()
regex.func_def = re.compile("[\t, ]*\\$fn.*:.*")
regex.func = re.compile(".*\\$fn.*")
regex.shift_function = re.compile(".*\\$ish.*")
regex.arith_or_logical_function = re.compile(".*\\$arith.*")

regex.unsigned_eight_bit = re.compile(".*\\$u8.*")
regex.hb = re.compile(".*\\$hb.*")
regex.hw = re.compile(".*\\$hw.*")
regex.shift_amount = re.compile(".*\\$sh.*")
regex.count_down = re.compile(".*\\$countDown.*")
regex.lab = re.compile(".*\\$lab.*")

input_file = None
current_write_file = None
function_number = 1


def process_new_function(line):
    global function_number  # needs to be global because we're modifying it
    line = line.replace("$fn", "f" + str(function_number))
    function_number += 1
    return line


def process_function(line):
    global function_number
    line = process_new_function(line)
    function_number -= 1
    return line


def process_shift_function(line):
    return line.replace("$ish", random.choice(shift_instructions), 1)


def process_arith_logical_function(line):
    line = line.replace("$arith", random.choice(arithmetic_instructions + logical_instructions), 1)
    return line


def process_unsigned_eight_bit(line):
    line = line.replace("$u8", str(get_random_dec_inclusive(0, 255)), 1)
    return line


def process_shift_amount(line):
    line = line.replace("$sh", str(get_random_dec_inclusive(1, 6)), 1)  # changed from original 0-6 to 1-6 to prevent
    # optimization out
    return line


def process_count_down(line):
    line = line.replace("$countDown", str(get_random_dec_inclusive(1, 20)),
                        1)  # changed from original 0-20 to 1-20 to ensure
    # instruction would not be optimized out
    return line


def process_hw(line):
    line = line.replace("$hw", str(get_random_hex_digits_inclusive_both(1, 4294967295)), 1)  # changed to 1-x
    return line


def process_hb(line):
    line = line.replace("$hb", str(get_random_hex_digits_inclusive_both(1, 255)), 1)  # changed to 1-x
    return line


def process_lab(line):
    line = line.replace("$lab", main_function_name, 1)
    return line


def get_random_hex_digits_inclusive_both(dec_min, dec_max):
    dec_num = get_random_dec_inclusive(dec_min, dec_max)
    hex_num = hex(dec_num)
    return hex_num[2:]  # get rid of 0x


def get_random_dec_inclusive(dec_min, dec_max):
    dec_num = random.randint(dec_min, dec_max)
    return dec_num


# noinspection PyUnresolvedReferences
def write(string):
    global current_write_file
    current_write_file.write(string)


def open_file_for_writing(string):
    global current_write_file
    current_write_file = open(string, 'w+')  # w for writing and + for creating the file if it doesn't already exist.
    return current_write_file


def open_input_file(string):
    global input_file
    input_file = open(string, "r")
    return input_file


# noinspection PyUnresolvedReferences
def get_line():
    return input_file.readline()


# noinspection PyTypeChecker,PyUnresolvedReferences
def main():
    parser = argparse.ArgumentParser(description="Generate Unique Assignments")
    parser.add_argument(in_filepath)
    parser.add_argument(num_outputs)
    args = parser.parse_args()
    input_filepath = args.in_filepath
    input_filepath = os.path.realpath(input_filepath)
    input_directory = os.path.dirname(input_filepath)
    filename = os.path.basename(input_filepath)
    ar = filename.split('.')
    output_directory = None
    if len(ar) != 1:
        output_directory = ''.join(ar[0:-1])
    else:
        output_directory = ar[0]
    output_directory = input_directory + "/" + output_directory
    try:
        os.mkdir(output_directory)
    except FileExistsError:
        pass
    open_input_file(input_filepath)
    for assignmentNumber in range(1, int(args.num_outputs) + 1):
        function_number = 1
        not_done = True
        open_file_for_writing(
            output_directory + "/" + os.path.basename(output_directory) + "_" + str(assignmentNumber) + "." + ar[
                -1])
        for line in input_file:
            while line is not None and "$" in line:
                if regex.func_def.match(line):
                    line = process_new_function(line)
                elif regex.func.match(line):
                    line = process_function(line)
                elif regex.shift_function.match(line):
                    line = process_shift_function(line)
                elif regex.arith_or_logical_function.match(line):
                    line = process_arith_logical_function(line)
                elif regex.unsigned_eight_bit.match(line):
                    line = process_unsigned_eight_bit(line)
                elif regex.shift_amount.match(line):
                    line = process_shift_amount(line)
                elif regex.count_down.match(line):
                    line = process_count_down(line)
                elif regex.hb.match(line):
                    line = process_hb(line)
                elif regex.hw.match(line):
                    line = process_hw(line)
                elif regex.lab.match(line):
                    line = process_lab(line)
                else:
                    raise SyntaxError("Unknown $command used in file")
            if line is not None:
                write(line)
        current_write_file.close()
        input_file.close()
        open_input_file(input_filepath)
        print(assignmentNumber)


if __name__ == "__main__":
    main()
    exit(0)
