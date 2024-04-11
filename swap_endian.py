def reorder_bytes(file):
    with open(file, "rb") as original_file:
        original_bytes = original_file.read()
        reordered_bytes = b''.join(original_bytes[i:i+4][::-1] for i in range(0, len(original_bytes), 4))
    with open('reordered_file', "wb") as new_file:
        new_file.write(reordered_bytes)
reorder_bytes('../Downloads/challengefile')