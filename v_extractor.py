key = 0x55

# Rename Data.v to the .v file you're using
with open("Data.v", "rb") as f:
    data = bytearray(f.read())

# Remove Header
payload = data[6:]

# Decrypt XOR
for i in range(len(payload)):
    payload[i] ^= key

# Searching for ZIP signature
zip_start = payload.find(b'PK\x03\x04')

if zip_start == -1:
    print("No ZIP found")
else:
    zip_data = payload[zip_start:]

    with open("clean_archive.zip", "wb") as f:
        f.write(zip_data)

    print("ZIP found near Offset:", zip_start)