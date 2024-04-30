#!/usr/bin/env python3

from dataclasses import dataclass

@dataclass
class Player:
    firstName:str = ""
    lastName:str = ""
    position:str = ""
    at_bats:int = 0
    hits:int = 0

    def full_name(self) -> str:
        return f"{self.firstName} {self.lastName}"

    def batting_average(self) -> float:
        if self.at_bats == 0:
            return 0.0
        return self.hits / self.at_bats

def main():
    pass

# if started as the main module, call the main function
if __name__ == "__main__":
    main()
