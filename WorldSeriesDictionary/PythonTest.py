import os


def build_dictionaries(filename="WorldSeriesWinners.txt"):

    Teams = {}
    Years = {}

    start_year = 1903
    skip_years = {1904, 1994}
    current_year = start_year

    try:
        with open(filename, "r") as file:

            winners = [line.strip() for line in file.readlines() if line.strip()]

            for winner in winners:

                while current_year in skip_years:
                    Years[current_year] = "No World Series"
                    current_year += 1

                Years[current_year] = winner
                Teams[winner] = Teams.get(winner, 0) + 1
                current_year += 1
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found")
        return None, None
    except Exception as e:
        print(f"An unexpected error occured: {e}")
        return None, None
    return Teams, Years


def main():
    Teams = None
    Years = None

    Teams, Years = build_dictionaries("WorldSeriesWinners.txt")

    if Teams is None or Years is None:
        return

    while True:
        try:
            user_input = input(
                "Enter a year between 1903 and 2021 (or type 'quit' to exit): "
            ).strip()
            if user_input.lower() == "quit":
                print("\nSession Terminated. Have a nice day!")
                break

            year = int(user_input)

            if 1903 <= year <= 2021:
                print(f"\n--- Results for {year} ---")

                winner = Years.get(year)

                if winner is None:
                    print(f"Error: Winner information for {year} is unavailable.")

                elif winner == "No World Series":
                    print(f"The World Series was NOT played in {year}.")
                    print("No Winner Data to be reported")

                else:
                    print(f"The {winner} won the World Series in {year}")
                    wincount = Teams.get(winner, 0)
                    print(
                        f"The {winner} have won the world Series {wincount} time(s) in total"
                    )

                print("-" * 30)
            else:
                print("Invalid year. Please enter a year between 1903 and 2021.")

        except ValueError:
            print("Invalid input. Please enter a whole number year.")


if __name__ == "__main__":
    main()