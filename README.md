**Helper script to remove `uniformscale` from static props in VMF files.**

Useful for porting CSGO maps to games that don't support this feature.

# Usage

- Set the `CROWBAR_PATH` env var to point to `CrowbarCommandLineDecomp.exe`.
- Set the `ASSETS_PATH` env var to point to the folder where your assets are located.
- Run `./descaler.py path/to/map.vmf`

This will:
1. Create a new `.qc` file for each affected model, with the scale built-in. You can then use Crowbar to compile the new rescaled models.
2. Generate a new VMF called `map_descaled.vmf` with fixed model references.

For example:

```json
"model" "models/whatever.mdl"
"uniformscale" "2.5"
```

Becomes:

```json
"model" "models/whatever_s2_5.mdl"
```

## Requirements

- Python 3.x
- [Crowbar Command-Line Decompiler](https://github.com/UltraTechX/Crowbar-Command-Line)
