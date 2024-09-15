from typing import Dict, Optional
from computer import Computer

class ResaleShop:

    # Attributes
    inventory: Dict[int, Computer] = {}
    IDnum: int = 0

    # Constructor
    def __init__(self):
        self.inventory: Dict[int, Computer] = {}
        self.IDnum: int = 0
        
    # Methods:

    def buy(self, computer: Computer):
        #increment ID (prevent doubling up)
        self.IDnum += 1
        #add computer to inventory
        self.inventory[self.IDnum] = computer
        return self.IDnum
        
    #sell computer    
    def sell(self, id: int):
        #if inventory has computer w/ given ID
        if id in self.inventory:
            del self.inventory[id]
            print("Item", id, "sold!")
        else: 
            print("Item", id, "not found. Please select another item to sell.")

    #display inventory
    def print_inventory(self):
        # If the inventory is not empty
        if self.inventory:
            # For each item
            for item_id in self.inventory:
                # Print its details
                print(f'Item ID: {item_id}, Description: {self.inventory[item_id].description}, Operating system: {self.inventory[item_id].operating_system}, Price: {self.inventory[item_id].price}')
        else:
            print("No inventory to display.")

    #refurbish
    def refurbish(self, item_id: int, new_os: Optional[str] = None):
        if item_id in self.inventory:
            computer = self.inventory[item_id] # locate the computer
            if int(computer.year_made) < 2000:
                computer.set_price(0) # too old to sell, donation only
            elif int(computer.year_made) < 2012:
                computer.set_price(250) # heavily-discounted price on machines 10+ years old
            elif int(computer.year_made) < 2018:
                computer.set_price(550) # discounted price on machines 4-to-10 year old machines
            else:
                computer.set_price(1000) # recent stuff

            if new_os is not None:
                computer.set_OS(new_os) # update details after installing new OS
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.")


def main():
    #create the shop
    store = ResaleShop()
    #open for business!
    print("-" * 21)
    print("COMPUTER RESALE STORE")
    print("-" * 21)

    #buy a computer
    id = store.buy(Computer("Mac Pro (Late 2013)", "3.5 GHc 6-Core Intel Xeon E5", 1024, 64, "macOS Big Sur", 2013, 1500))
    print("Checking inventory...")
    store.print_inventory()
    print("Done.\n")

    # refurbish it
    new_OS = "MacOS Monterey"
    print("Refurbishing Item ID:", id, ", updating OS to", new_OS)
    print("Updating inventory...")
    store.refurbish(id, new_OS)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    store.print_inventory()
    print("Done.\n")
    
    # Now, let's sell it!
    print("Selling Item ID:", id)
    store.sell(id)
    print("")
    
    # Make sure it worked by checking inventory
    print("Checking inventory...")
    store.print_inventory()
    print("Done.\n")


if __name__ == "__main__":
    main()