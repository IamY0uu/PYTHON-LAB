# create folder and store tables of 2 to 20 in different files 
for num in range(2, 21):  # 2 se 20 tak loop
    with open(f"table{num}.txt", "w") as f:  # Ek baar hi file open karenge
        f.write(f"Table of: {num}\n\n")  # Heading likhna
        
        for i in range(1, 11):  # 1 se 10 tak table likhna
            f.write(f"{num} x {i} = {num * i}\n")  # Correct way to write

            
