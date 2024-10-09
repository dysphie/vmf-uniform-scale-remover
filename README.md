**Helper script to convert `uniformscale` prop_static in VMF files to standard prop_static.**

Useful for porting CSGO maps to games that don't support this feature.

# Usage
- Ensure that `CrowbarCommandLineDecomp.exe` is included in your system's PATH.
- Create an `assets.txt` file that lists the asset folders to scan (each folder must contain a `models` subfolder).
- Run the script using the command: `./descaler.py path/to/map.vmf`.

This will generate a new .qc file for each affected model and create a new VMF `*_descaled.vmf` with patched model references

You can then use Crowbar to bulk compile the `scaled_qcs` folder 

## Requirements

- Python 3.x
- [Crowbar Command-Line Decompiler](https://github.com/UltraTechX/Crowbar-Command-Line)
