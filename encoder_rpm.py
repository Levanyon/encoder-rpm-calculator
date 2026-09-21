from __future__ import annotations

import argparse
import math


def calculate_rpm(pulses: int, ppr: int, interval_seconds: float) -> float:
    """Calculate shaft speed in revolutions per minute."""
    if pulses < 0:
        raise ValueError("pulses cannot be negative")
    if ppr <= 0:
        raise ValueError("ppr must be greater than zero")
    if interval_seconds <= 0:
        raise ValueError("interval_seconds must be greater than zero")

    revolutions = pulses / ppr
    revolutions_per_second = revolutions / interval_seconds
    return revolutions_per_second * 60.0


def rpm_to_rad_s(rpm: float) -> float:
    """Convert revolutions per minute to radians per second."""
    if rpm < 0:
        raise ValueError("rpm cannot be negative")
    return rpm * 2.0 * math.pi / 60.0


def speed_status(rpm: float, max_rpm: float) -> str:
    """Return whether the measured speed is within the configured limit."""
    if rpm < 0:
        raise ValueError("rpm cannot be negative")
    if max_rpm <= 0:
        raise ValueError("max_rpm must be greater than zero")
    return "OVER LIMIT" if rpm > max_rpm else "OK"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Calculate motor/shaft speed from encoder pulse measurements."
    )
    parser.add_argument("pulses", type=int, help="Pulse count measured in the interval")
    parser.add_argument("ppr", type=int, help="Encoder pulses per revolution")
    parser.add_argument(
        "interval_seconds",
        type=float,
        help="Measurement interval in seconds",
    )
    parser.add_argument(
        "--max-rpm",
        type=float,
        default=None,
        help="Optional maximum allowed RPM",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()

    try:
        rpm = calculate_rpm(args.pulses, args.ppr, args.interval_seconds)
        rad_s = rpm_to_rad_s(rpm)
    except ValueError as exc:
        raise SystemExit(f"Error: {exc}") from exc

    print(f"RPM: {rpm:.2f}")
    print(f"Angular speed: {rad_s:.2f} rad/s")

    if args.max_rpm is not None:
        try:
            print(f"Status: {speed_status(rpm, args.max_rpm)}")
        except ValueError as exc:
            raise SystemExit(f"Error: {exc}") from exc


if __name__ == "__main__":
    main()
