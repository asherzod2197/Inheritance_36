# 36. Onlayn do‘kon savati

class Cart:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price          # bir dona narxi ($)
        self.quantity = quantity    # miqdori (dona)

    def total_cost(self):
        """Mahsulot uchun umumiy narx = narx × miqdor"""
        return self.price * self.quantity

    def __str__(self):
        total = self.total_cost()
        return f"{self.name:14} | {self.price:7.2f}$ | {self.quantity:4} dona | {total:9.2f}$"


# -----------------------------------------------
# Voris sinflar (chiroyli chiqish + emoji)
# -----------------------------------------------

class ElectronicsCart(Cart):
    def __str__(self):
        total = self.total_cost()
        return f"📱 {self.name:12} → {self.price:6.2f}$ × {self.quantity:2} = {total:7.2f}$"


class ClothingCart(Cart):
    def __str__(self):
        total = self.total_cost()
        return f"👕 {self.name:12} → {self.price:6.2f}$ × {self.quantity:2} = {total:7.2f}$"


# --------------------------------------------------
# Savatdagi mahsulotlar va umumiy hisob
# --------------------------------------------------

def show_shopping_cart(items):
    print("\n" + "═" * 70)
    print("       ONLAYN DO‘KON SAVATI — UMUMIY HISOB       ".center(70))
    print("═" * 70)
    print("Mahsulot nomi      Birlik narxi   Miqdor   Jami narx ($)")
    print("─" * 70)

    grand_total = 0

    for item in items:
        print(item)
        grand_total += item.total_cost()

    print("─" * 70)
    print(f"UMUMIY SAVAT NARXI:                                 {grand_total:10.2f}$")
    print("═" * 70 + "\n")


# Test ma'lumotlari
savat = [
    ElectronicsCart("Telefon (iPhone 15)", 999.00, 1),
    ClothingCart("Ko‘ylak (erkaklar)", 45.00, 2),
    ElectronicsCart("Quloqchin (AirPods Pro)", 249.00, 1),
    ClothingCart("Shim (jeans)", 79.90, 3),
    ElectronicsCart("Planshet (iPad)", 599.00, 1),
]

show_shopping_cart(savat)


# Sizning misol qiymatlaringiz bilan:
print("\nSizning misol savatingiz:\n")
misol_savat = [
    ElectronicsCart("Telefon", 500, 2),
    ClothingCart("Ko‘ylak", 30, 3),
]

show_shopping_cart(misol_savat)
