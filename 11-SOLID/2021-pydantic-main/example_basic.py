"""
Dont know about structure of data so cant validate or santize data     
"""
import json


def main():
    """main function"""
    
    #Read data from JSON file
    with open("11-SOLID/2021-pydantic-main/data.json") as file:
        data=json.load(file)
    print(data[2]["title"])
        
if __name__ == "__main__":
    main()
