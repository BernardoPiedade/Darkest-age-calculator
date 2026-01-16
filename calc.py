import sys
  
import os
  
import json
  
from datetime import datetime, timedelta
  

  
# Cores ANSI (Windows 10+)
  
RESET = "\033[0m"
  
RED = "\033[31m"
  
GREEN = "\033[32m"
  
YELLOW = "\033[33m"
  
CYAN = "\033[36m"
  
MAGENTA = "\033[35m"
  
BOLD = "\033[1m"
  

  
MARKET_FILE = "market.json"
  

  
def load_market():
  
    if not os.path.exists(MARKET_FILE):
  
        with open(MARKET_FILE, "w") as f:
  
            json.dump([], f)  # cria lista vazia
  
    with open(MARKET_FILE, "r") as f:
  
        return json.load(f)
  

  
def save_market(market):
  
    with open(MARKET_FILE, "w") as f:
  
        json.dump(market, f, indent=4)
  

  
def parse_value_or_range(s):
  
    s = s.replace(" ", "")
  
    if "-" in s:
  
        a, b = s.split("-", 1)
  
        a = int(a)
  
        b = int(b)
  
        if b < a:
  
            b = a
  
        return a, b
  
    else:
  
        v = int(s)
  
        return v, v
  

  
def scenarios(min_v, max_v):
  
    if min_v == max_v:
  
        return [("Fixed", min_v)]
  
    d = max_v - min_v
  
    return [
  
        ("Minimum", min_v),
  
        ("Median", min_v + d // 3),
  
        ("Higher Median", min_v + 2 * d // 3),
  
    ]
  

  
def format_time(hours):
  
    h = int(hours)
  
    m = int((hours - h) * 60)
  
    return f"{h}h {m}m"
  

  
def calc_xp_c():
  
    while True:
  
        try:
  

  
            print(BOLD + CYAN + "Darkest Age — Calculator" + RESET)
  
            print("(Ctrl+C to close or 0 to return to main screen)\n")
  
            print(BOLD + CYAN + "New XP/C Calculation" + RESET)
  
            
  
            m = int(input("Mobs killed: "))
  

  
            if m == 0:
  
                return
  

  
            xp_input = input("XP per mob (value or min-max): ")
  
            c_input = input("Crowns per mob (value or min-max): ")
  
            t = float(input("Time in minutes: "))
  

  
            xp_atual_raw = input("Current XP (Enter to ignore): ").strip()
  
            xp_total_raw = input("Total XP to evolve (Enter to ignore): ").strip()
  

  

  
            if t <= 0 or m <= 0:
  
                print(RED + "Invalid values.\n" + RESET)
  
                continue
  

  
            xp_atual = int(xp_atual_raw) if xp_atual_raw else None
  
            xp_total_need = int(xp_total_raw) if xp_total_raw else None
  

  
            xp_min, xp_max = parse_value_or_range(xp_input)
  
            c_min, c_max = parse_value_or_range(c_input)
  

  
            xp_scen = scenarios(xp_min, xp_max)
  
            c_scen = scenarios(c_min, c_max)
  

  
            print()
  
            print(BOLD + MAGENTA + "Results per scenario:" + RESET)
  
            now = datetime.now()
  
            print(BOLD + YELLOW + f"Current time: {now.strftime('%H:%M')}\n" + RESET)
  
            print("-" * 40)
  

  
            for i, (label, xp_val) in enumerate(xp_scen):
  
                c_val = c_scen[min(i, len(c_scen) - 1)][1]
  

  
                xp_total = xp_val * m
  
                c_total = c_val * m
  

  
                xp_m = xp_total / t
  
                c_m = c_total / t
  

  
                xp_h = xp_total * 60 / t
  
                c_h = c_total * 60 / t
  

  
                color = RED if label == "Minimum" else GREEN if "Higher" in label else YELLOW
  

  
                print(color + BOLD + f"[{label.upper()}]" + RESET)
  
                print(f"XP per mob: {xp_val}")
  
                print(f"XP total: {xp_total}")
  
                print(f"XP per hour: {int(xp_h)}")
  
                print(f"XP per minute: {int(xp_m)}")
  
                print(YELLOW + "-" * 40)
  
                print(RESET + f"Crowns per mob: {c_val}")
  
                print(f"Crowns total: {c_total}")
  
                print(f"Crowns per hour: {int(c_h)}")
  
                print(f"Crowns per minute: {int(c_m)}")
  

  
                if xp_atual is not None and xp_total_need is not None:
  
                    xp_falta = max(0, xp_total_need - xp_atual)
  

  
                    if xp_falta == 0:
  
                        print(YELLOW + "-" * 40)
  
                        print(GREEN + "Time until evolving: 0h 0m" + RESET)
  
                    else:
  
                        horas_para_level = xp_falta / xp_h
  
                        finish_time = now + timedelta(hours=horas_para_level)
  

  
                        print(YELLOW + "-" * 40)
  
                        print(RESET + f"Time until evolving: {format_time(horas_para_level)} (≈ {finish_time.strftime('%H:%M')})")
  

  
                print("-" * 40)
  

  
            print()
  

  
        except KeyboardInterrupt:
  
            print("\nLeaving...")
  
            sys.exit(0)
  
        except Exception as e:
  
            print(RED + f"Error: {e}\n" + RESET)
  

  
def calc_io():
  
    while True:
  
        try:
  

  
            print(BOLD + CYAN + "\nDarkest Age — Calculator" + RESET)
  
            print("(Ctrl+C to close or 0 to return to main screen)\n")
  
            print(BOLD + CYAN + "New Infernal Ore Calculation" + RESET)
  
            
  
            o = int(input("Ores owned: "))
  

  
            if o == 0:
  
                return
  

  
            o_value = int(input("Price per ore: "))
  

  
            _v = o * o_value
  
            v_t = _v * 0.10
  
            v = _v - v_t
  

  
            print("\n")
  
            print("-" * 40)
  
            print(BOLD + MAGENTA + "Results per scenario:" + RESET)
  

  
            print(f"Total value without tax: {_v}")
  
            print(f"Total value with tax: {v}")
  
            print("-" * 40)
  

  
        except KeyboardInterrupt:
  
            print("\nLeaving...")
  
            sys.exit(0)
  
        except Exception as e:
  
            print(RED + f"Error: {e}\n" + RESET)
  

  
def u_market():
  
    while True:
  

  
        os.system("cls")
  
        print(BOLD + CYAN + "Darkest Age — Calculator" + RESET)
  
        print("(Ctrl+C or 0 to close)\n\n")
  
        market = load_market()
  
        total_items = sum(item['quantity'] for item in market)
  
        total_gold = sum(item['quantity'] * item['price'] for item in market)
  

  
        _g = total_gold * 0.10
  
        g = total_gold - _g
  

  
        print("\n" + "="*40)
  
        print(f"Nº of items on the list: {total_items}")
  
        print(f"Gold total expected (with tax): {g}")
  
        print("="*40)
  
        print("1 - See list")
  
        print("2 - Add item to list")
  
        print("3 - Remove item from list")
  
        print("0 - Return")
  
        print("="*40)
  

  
        choice = input("-> ").strip()
  

  
        if choice == "1":
  
            if not market:
  
                print("The list is empty.")
  
                input("Press Enter to continue...")
  
            else:
  
                print("\nItems for sale:")
  
                for idx, item in enumerate(market, 1):
  
                    print(f"{idx}. {item['name']} - Quantity: {item['quantity']} - Price per unit: {item['price']} - Total: {item['quantity']*item['price']}")
  
        elif choice == "2":
  
            name = input("Item name: ").strip()
  
            if not name:
  
                print("Invalid name.")
  
                input("Press Enter to continue...")
  
                continue
  
            try:
  
                quantity = int(input("Quantity: "))
  
                price = int(input("Price per unit: "))
  
            except ValueError:
  
                print("Quantity and price must be integers.")
  
                input("Press Enter to continue...")
  
                continue
  
            market.append({"name": name, "quantity": quantity, "price": price})
  
            save_market(market)
  
            print(f"Item {name} added to list.")
  
        elif choice == "3":
  
            if not market:
  
                print("There aren't any items to remove.")
  
                input("Press Enter to continue...")
  
                continue
  
            for idx, item in enumerate(market, 1):
  
                print(f"{idx}. {item['name']} - Quantity: {item['quantity']} - Price: {item['price']}")
  
            try:
  
                to_remove = int(input("Choose the number of the item to remove: "))
  
                if 1 <= to_remove <= len(market):
  
                    removed_item = market.pop(to_remove-1)
  
                    save_market(market)
  
                    print(f"Item {removed_item['name']} removed.")
  
                else:
  
                    print("Invalid number.")
  
                    input("Press Enter to continue...")
  
            except ValueError:
  
                print("Wrong input.")
  
                input("Press Enter to continue...")
  
        elif choice == "0":
  
            break
  
        else:
  
            print("Invalid option.")
  

  
def main():
  
    while True:
  
        try:
  
            os.system("cls")
  
            print(BOLD + CYAN + "Darkest Age — Calculator" + RESET)
  
            print("(Ctrl+C or 0 to close)\n\n")
  

  
            print("1 - XP and Crowns Calculator")
  
            print("2 - Infernal Ore Price Calculator")
  
            print("3 - Market List")
  
            print("0 - Close")
  

  
            a = int(input("\n-> "))
  

  
            if a == 1:
  
                os.system("cls")
  
                calc_xp_c()
  
            if a == 2:
  
                os.system("cls")
  
                calc_io()
  
            if a == 3:
  
                os.system("cls")
  
                u_market()
  

  
        except KeyboardInterrupt:
  
            print("\nLeaving...")
  
            sys.exit(0)
  
        except Exception as e:
  
            print(RED + f"Error: {e}\n" + RESET)
  

  
if __name__ == '__main__':
  
    main()
