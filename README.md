**Helper script to convert `uniformscale` prop_static in VMF files to standard prop_static.**

Useful for porting CSGO maps to games that don't support this feature.

# Usage

- Set the `CROWBAR_PATH` env var to point to `CrowbarCommandLineDecomp.exe`.
- Set the `ASSETS_PATH` env var to point to the folder where your assets are located.
- Run `./descaler.py path/to/map.vmf`

This will:
1. Create a new `.qc` file for each affected model in `./scaled_qcs`, with the scale built-in. 
2. Generate a new VMF called `map_descaled.vmf` with fixed model references.

You can then use Crowbar to compile the new rescaled models.

## Requirements

- Python 3.x
- [Crowbar Command-Line Decompiler](https://github.com/UltraTechX/Crowbar-Command-Line)
