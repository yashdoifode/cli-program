# cli_program.py
def cli_program(input_value):
    
    return f"Received input from GUI: {input_value}"

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python cli_program.py [input_value]")
    else:
        input_value = sys.argv[1]
        print(cli_program(input_value))
