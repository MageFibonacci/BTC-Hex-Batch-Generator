# BTC Hex Batch Generator

This Python script is designed to divide a hexadecimal range into contiguous, non-overlapping batches, making it ideal for working on Bitcoin (BTC) puzzles. Each batch represents a subsection of the specified range, useful for tasks like private key searches or targeted interval scanning.

## Key Features
- **Precise Splitting**: Calculates batches ensuring they are contiguous, with no overlaps or gaps.
- **Customizable**: Allows configuration of the hexadecimal range (`start_hex` and `end_hex`) and the desired number of batches.
- **Multiple Outputs**:
  - `hex_batches.sh` file for immediate use in shell scripts.
  - `hex_stats_batches.sh` file for analysis and further use in Python.

## Usage
1. Define the hexadecimal range (`start_hex` and `end_hex`).
2. Specify the desired number of batches.
3. Run the script to generate the output files.

## Applications
- Scanning private keys within specific hexadecimal ranges.
- Solving BTC-based puzzles.
- Efficiently managing ranges for distributed analysis.
