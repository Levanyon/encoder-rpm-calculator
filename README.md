# Encoder RPM Calculator

A small Python command-line project that calculates motor or shaft speed from incremental encoder pulse measurements.

## What it practices

- Encoder pulse / PPR relationships
- RPM calculation
- Angular speed conversion (rad/s)
- Input validation and exceptions
- Command-line arguments with `argparse`
- Automated tests with `unittest`
- GitHub Actions

## Formula

If an encoder produces `PPR` pulses per revolution and `pulses` are counted during a measurement interval:

```text
revolutions = pulses / PPR
RPM = (revolutions / interval_seconds) * 60
```

Angular speed is:

```text
rad/s = RPM * 2π / 60
```

## Usage

```bash
python encoder_rpm.py 1000 500 2
```

Example output:

```text
RPM: 60.00
Angular speed: 6.28 rad/s
```

You can also check a speed limit:

```bash
python encoder_rpm.py 1000 500 2 --max-rpm 50
```

## Run tests

```bash
python -m unittest -v
```

This project uses only Python's standard library.
