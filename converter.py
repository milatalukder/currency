def convert_currency():
    print("--- Welcome to the INR to BDT Converter ---")
    
    exchange_rate = 1.40 
    
    try:
        rupee_amount = float(input("Enter amount in Indian Rupee (INR): "))
        
        taka_amount = rupee_amount * exchange_rate
        
        print(f"\n[Result] {rupee_amount} INR is equal to {taka_amount:.2f} BDT")
        print("-------------------------------------------")
        
    except ValueError:
    print("Invalid input! Please enter a numeric value.")

if __name__ == "__main__":
    convert_currency()
