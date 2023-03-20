def luhn_checksum(number: str) -> bool:
    def digits_of(nr: str) -> list[int]:
        return [int(d) for d in nr]
    
    digits = digits_of(number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for digit in even_digits:
        checksum += sum(digits_of(str(digit * 2)))
    return checksum % 10 == 0 

def main():
    print(luhn_checksum(123455))
    
if __name__ == "__main__":
    main()

