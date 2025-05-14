from datetime import datetime
birth_year = input("What yeare are you born in? ")
birth_year = int(birth_year)

current_year = datetime.now().year
print(f"You are currently {current_year - birth_year} years old!")