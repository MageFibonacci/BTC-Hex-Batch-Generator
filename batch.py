# Batch calculation
start_hex = int("40000000000000000", 16)
end_hex = int("7ffffffffffffffff", 16)
num_batches = 2048  # Number of batches

# Calculating batch size
step = (end_hex - start_hex + 1) // num_batches

# Batch generation
batches = []
for i in range(num_batches):
    batch_start = start_hex + i * step
    batch_end = min(batch_start + step - 1, end_hex)
    batches.append((f"{batch_start:016x}", f"{batch_end:016x}"))

# Make sure batches cover the entire range without spaces
assert int(batches[0][0], 16) == start_hex, "The first batch does not start from the beginning"
assert int(batches[-1][1], 16) == end_hex, "The last batch does not include the upper limit"
for i in range(len(batches) - 1):
    assert int(batches[i][1], 16) + 1 == int(batches[i + 1][0], 16), f"Gap detected between batches {i} and {i + 1}"

# Creating the first file (hex_batches.sh)
batch_lines = [
    f'  "{start} {end}"'
    for start, end in batches
]
file_content_batches = "BATCHES=(\n" + "\n".join(batch_lines) + "\n)"

output_file_path_batches = "hex_batches.sh"
with open(output_file_path_batches, "w") as file:
    file.write(file_content_batches)

# Creating the second file (hex_stats_batches.sh)
file_content_stats = "batches = [\n" + ",\n".join(
    [f'    ("{start}", "{end}")' for start, end in batches]
) + "\n]"

output_file_path_stats = "hex_stats_batches.sh"
with open(output_file_path_stats, "w") as file:
    file.write(file_content_stats)

print(f"File 1 saved as {output_file_path_batches}")
print(f"File 2 saved as {output_file_path_stats}")
