#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script to calculate the sum of two numbers
"""

def main():
    print("Welcome to the Sum Calculator!")
    print("=" * 40)
    
    try:
        # Get input from user
        x = float(input("Please enter the value of X: "))
        y = float(input("Please enter the value of Y: "))
        
        # Calculate the sum
        result = x + y
        
        # Format the result to avoid floating point precision issues
        # Round to 10 decimal places to handle precision errors
        rounded_result = round(result, 10)
        
        # Format nicely: remove trailing zeros for cleaner display
        if rounded_result == int(rounded_result):
            formatted_result = str(int(rounded_result))
        else:
            # Convert to string with up to 10 decimal places, remove trailing zeros
            formatted_result = f"{rounded_result:.10f}".rstrip('0').rstrip('.')
        
        # Print the result with a nice message
        print("\n" + "=" * 40)
        print(f"The sum of {x} and {y} is: {formatted_result}")
        print("🎉 Great job! Calculation completed successfully! 🎉")
        print("=" * 40)
        
    except ValueError:
        print("\n❌ Error: Please enter a valid number only!")
    except Exception as e:
        print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    main()

