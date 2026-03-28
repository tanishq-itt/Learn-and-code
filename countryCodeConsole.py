country_neighbours_mapping = {
    "IN" : ["Pakistan","Bangladesh", "Sri Lanka","China", "Nepal", "Bhutan", "Myanmar"],
    "US" : ["Mexico","Canada","Russia","Cuba"],
    "NZ" : ["Australia","France", "Tonga"]
}

isQuit = True
while isQuit:
    isExit = input("\nWant to play press any key, if not press q!: ")
    if isExit != "q":
        country_code = input("Enter the country code: ")
        country_code = country_code.upper()
        if(country_code == "IN" or country_code == "US" or country_code == "NZ"):
            print(f"The adjacent countries names for {country_code} are : ")
            for adjacent_country_name in country_neighbours_mapping[country_code]:
                print(adjacent_country_name, end= " " )
        else:
            print("Enter valid country code in the given list (IN/US/NZ)") 
            pass
    else:
        isQuit = False    

    