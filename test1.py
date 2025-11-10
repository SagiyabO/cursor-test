#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script to calculate the sum of two numbers
"""

from datetime import datetime
from typing import Optional

from colorama import Fore, Style, init

init(autoreset=True)


def main() -> None:
    """Collect two numbers from the user, calculate their sum, and display the result."""
    print("Welcome to the Sum Calculator!")
    print("=" * 40)

    def get_number(label: str) -> Optional[float]:
        """Prompt for a number, allowing exit and gentle validation nudges."""
        while True:
            raw_value = input(f"Please enter the value of {label} (or 'q' to quit): ").strip()
            if raw_value.lower() == "q":
                return None
            if not raw_value:
                print(f"{Fore.YELLOW}⚠️ Hint: enter a number such as 42 or 3.14; blank input won't work.{Style.RESET_ALL}")
                continue
            if "," in raw_value:
                print(f"{Fore.YELLOW}⚠️ Hint: use a dot for decimals (e.g., 3.14) instead of a comma.{Style.RESET_ALL}")
                continue
            try:
                return float(raw_value)
            except ValueError:
                print(f"{Fore.YELLOW}⚠️ Couldn't interpret '{raw_value}'. Please try a numeric value.{Style.RESET_ALL}")

    while True:
        try:
            x: Optional[float] = get_number("X")
            if x is None:
                print(f"{Fore.MAGENTA}👋 Thanks for using the Sum Calculator. See you next time!{Style.RESET_ALL}")
                break

            y: Optional[float] = get_number("Y")
            if y is None:
                print(f"{Fore.MAGENTA}👋 Thanks for using the Sum Calculator. See you next time!{Style.RESET_ALL}")
                break

            # Calculate the sum
            result: float = x + y

            # Format the result to avoid floating point precision issues
            # Round to 10 decimal places to handle precision errors
            rounded_result: float = round(result, 10)

            # Format nicely: remove trailing zeros for cleaner display
            if rounded_result == int(rounded_result):
                formatted_result = str(int(rounded_result))
            else:
                # Convert to string with up to 10 decimal places, remove trailing zeros
                formatted_result = f"{rounded_result:.10f}".rstrip("0").rstrip(".")

            # Print the result with a nice message
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print("\n" + "=" * 40)
            print(f"{Fore.CYAN}The sum of {x} and {y} is: {formatted_result}{Style.RESET_ALL}")
            print(f"{Fore.GREEN}🎉 Great job! Calculation completed successfully at {timestamp}! 🎉{Style.RESET_ALL}")
            print("=" * 40)
        except Exception as e:
            print(f"\n{Fore.RED}❌ Error: {e}{Style.RESET_ALL}")
            break

        choice = input("Press Enter to calculate again or type 'q' to quit: ").strip().lower()
        if choice == "q":
            print(f"{Fore.MAGENTA}👋 Thanks for using the Sum Calculator. See you next time!{Style.RESET_ALL}")
            break
        print("-" * 40)

if __name__ == "__main__":
    main()

