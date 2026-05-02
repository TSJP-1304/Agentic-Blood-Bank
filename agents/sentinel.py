import os
import django

# 1. Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from inventory.models import BloodStock, Donor
from django.db.models import F

def check_inventory():
    print("\n🔍 Sentinel Agent: Scanning blood bank inventory...")
    
    # Find stocks where units are less than the threshold
    critical_stocks = BloodStock.objects.filter(units__lt=F('threshold'))
    
    if not critical_stocks.exists():
        print("✅ All stock levels are sufficient. No action needed.")
        return

    for stock in critical_stocks:
        print(f"⚠️ ALERT: {stock.group} is CRITICAL ({stock.units} units remaining).")
        find_donors(stock.group)

def find_donors(group):
    # Find eligible donors for this specific blood group
    potential_donors = Donor.objects.filter(blood_group=group, is_eligible=True)
    
    if potential_donors.exists():
        print(f"🕵️ Matching donors for {group}: {potential_donors.count()} found.")
        for donor in potential_donors:
            print(f"📧 System ready to contact: {donor.name} at {donor.email}")
    else:
        print(f"❌ No eligible donors found for {group} in the database.")

if __name__ == "__main__":
    check_inventory()