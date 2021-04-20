from blood_bank.models import Bloodbank, Inventory
bloodbank1 = Bloodbank.objects.get(pk=1)
bloodbank2 = Bloodbank.objects.get(pk=2)

for i in range(1, 51):
	donorname1 = "Random Donor " + str(i)
	donorname2 = "Sample donor " + str(i)
	blood1 = Inventory.objects.create(blood_bank=bloodbank1, blood_group= 'B+', donor_name=donorname1, donor_address="Savar, Dhaka", donor_mobile_no="1233433344", donation_date="2021-4-13", expiry_date="2021-5-25")
	blood2 = Inventory.objects.create(blood_bank=bloodbank2, blood_group= 'O+', donor_name=donorname2, donor_address="Uttara, Dhaka", donor_mobile_no="1212121212", donation_date="2021-4-10", expiry_date="2021-5-22")
	blood1.save()
	blood2.save()

"""
In [1]: from blood_bank.models import Bloodbank, Inventory
   ...: bloodbank1 = Bloodbank.objects.get(pk=1)
   ...: bloodbank2 = Bloodbank.objects.get(pk=2)
   ...: 
   ...: for i in range(1, 51):
   ...:     donorname1 = "Random Donor " + str(i)
   ...:     donorname2 = "Sample donor " + str(i)
   ...:     blood1 = Inventory.objects.create(blood_bank=bloodbank1, blood_group= 'B+', donor_name=donorname1, donor_address="Savar, Dhaka", donor_mobile_no="1233433344", donation_date="2021
   ...: -4-13", expiry_date="2021-5-25")
   ...:     blood2 = Inventory.objects.create(blood_bank=bloodbank2, blood_group= '0+', donor_name=donorname2, donor_address="Uttara, Dhaka", donor_mobile_no="1212121212", donation_date="202
   ...: 1-4-10", expiry_date="2021-5-22")
   ...:     blood1.save()
   ...:     blood2.save()
   """