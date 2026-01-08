# Regular Expressions

This directory contains Ruby scripts that demonstrate regular expression matching using the Oniguruma library.

## Requirements

- All scripts must start with `#!/usr/bin/env ruby`
- All scripts must be executable
- All files should end with a new line
- Regular expressions are built for the Oniguruma library (Ruby's default)

## Files

### 0-simply_match_school.rb
A Ruby script that accepts one argument and uses a regular expression to match the pattern "Holberton".

**Usage:**
```bash
./0-simply_match_school.rb <string>
```

**Examples:**
```bash
./0-simply_match_school.rb "Holberton"          # Output: Holberton
./0-simply_match_school.rb "holberton"          # Output: holberton
./0-simply_match_school.rb "H0lberton"          # Output: H0lberton
./0-simply_match_school.rb "aaahHolberton"      # Output: Holberton
./0-simply_match_school.rb "Holbertonaaa"       # Output: Holberton
```

**Pattern:** The regex matches the exact string "Holberton" (case-sensitive) within the input.

## Testing

On Ubuntu 20.04 LTS:
1. Make the script executable: `chmod +x 0-simply_match_school.rb`
2. Run the script with test strings as shown in the examples above
