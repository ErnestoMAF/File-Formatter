# File Formatter

A tool to process and format files with a specific structure, converting hexadecimal values to decimal, extracting relevant data, and rewriting the output in a custom format.

---

## Input Format

Each line in the input file must follow this structure:
  b06:bf51:ef0f:7995:d321:4c8b:811c:1e99/60, Tabby, Jackett, tjackett9@flickr.com, Female, 148.202.30.5

---

## Output Format

The tool will transform each line into the following format:
  Jackett 2822 : 48977 : 61199 : 31125 : 54049 : 19595 : 33052 : 7833 : 94.CA.1E.5

---

## How It Works

The tool processes each line using the following steps:

1. **Hexadecimal to Decimal Conversion**:
   - The first part of the input (e.g., `b06:bf51:ef0f:7995:d321:4c8b:811c:1e99`) is a hexadecimal value.
   - Each hexadecimal group is converted to its decimal equivalent.

2. **Extract the Second Text String**:
   - The second text string (e.g., `Jackett`) is extracted and used as the first part of the output.

3. **Convert IP Address to Hexadecimal**:
   - The last part of the input (e.g., `148.202.30.5`) is an IP address.
   - Each octet is converted to its hexadecimal equivalent in uppercase (e.g., `148` → `94`, `202` → `CA`).

4. **Rewrite in the Desired Format**:
   - The output is formatted as:
     ```
     [Second Text String] : [Decimal Values] : [Hexadecimal IP Address]
     ```

---

## Features

- **Single Line Formatting**: Process and format a single line of input.
- **Batch File Formatting**: Process an entire file line by line.

---

## Code Design

The project is built following **SOLID principles** to ensure:
- **Maintainability**: Clean and modular code.
- **Scalability**: Easy to extend with new features.
- **Reusability**: Components can be reused in other projects.

---

## Future

- Intended to scale the project to accept custom inputs and deliver custom outputs.

