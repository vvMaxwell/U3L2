with open("en_climate_hourly_AB_3050519_11-2023_P1H.csv") as fileDescriptor:
        data = fileDescriptor.read()
with open("x.txt", "w") as fileDescriptor:
        fileDescriptor.write(data)