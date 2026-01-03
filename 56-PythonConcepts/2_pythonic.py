def main() -> None:
    names = ["Arjan", "Marieke", "Pim", "Sanne", "Daan", "Eva", "Lars"]

    for i in range(len(names)):
        print(i, names[i])

    print("---")

    # or more pythonic
    for index, name in enumerate(names): # More pythonic way
        print(index, name)

if __name__ == "__main__":
    main()