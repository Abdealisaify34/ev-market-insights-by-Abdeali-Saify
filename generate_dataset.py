"""Builds data/ev_market.csv (synthetic, realistic ranges). Replace with your real/Kaggle EV data if you have one."""
import random, pandas as pd
random.seed(42)
MAKERS = {  # maker: (country, battery weights)
 "Tesla":("USA",["NMC","LFP","NCA"]),"BYD":("China",["LFP","LFP","NMC"]),
 "Tata Motors":("India",["LFP","NMC"]),"MG Motor":("UK",["NMC","LFP"]),
 "Hyundai":("South Korea",["NMC","NCA"]),"Nissan":("Japan",["NMC"]),
 "BMW":("Germany",["NMC","NCA"]),"Volkswagen":("Germany",["NMC","LFP"]),
 "Ola Electric":("India",["LFP","NMC"]),"NIO":("China",["NMC","Solid-State"]),
 "Ather":("India",["LFP","NMC"]),"Ashok Leyland":("India",["LFP"])}
CATS = {"Hatchback":(30,70,250,420,9e3),"Sedan":(55,95,380,600,2.2e4),
 "SUV":(60,110,350,560,2.8e4),"Electric Bus":(200,350,200,320,1.5e3),
 "Electric Truck":(150,300,180,350,1.2e3),"Two-Wheeler":(2,6,80,200,6e4)}
rows=[]
for i in range(1,2501):
    mk=random.choice(list(MAKERS)); ctry,bats=MAKERS[mk]
    cat=random.choices(list(CATS),weights=[18,16,26,6,6,28])[0]
    lo,hi,rl,rh,base=CATS[cat]
    bat=random.choice(bats+(["Sodium-Ion"] if random.random()<.03 else []))
    cap=round(random.uniform(lo,hi),1); rng=int(random.uniform(rl,rh)*(1.06 if bat=="NCA" else 1))
    yr=random.choice(range(2019,2026)); growth=1+0.18*(yr-2019)
    rows.append(dict(Vehicle_ID=i,Manufacturer=mk,Model=f"{mk[:3].upper()}-{cat[:3].upper()}-{random.randint(100,999)}",
      Vehicle_Category=cat,Battery_Type=bat,Battery_Capacity_kWh=cap,Driving_Range_km=rng,
      Price_USD=int(cap*random.uniform(450,900)),Annual_Sales_Units=int(base*random.uniform(.2,1.4)*growth/12),
      Customer_Rating=round(min(5,max(2.5,random.gauss(4.1,.45))),1),Manufacturing_Country=ctry,Sales_Year=yr))
pd.DataFrame(rows).to_csv("data/ev_market.csv",index=False); print("rows:",len(rows))
