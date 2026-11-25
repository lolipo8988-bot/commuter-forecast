"""Write a one-line weather forecast for an invented city to /output/entry.txt.

The line is assembled the way a real bulletin is: the place, then its
conditions in broadcast order (rain easing by a stated hour, sunny
spells, the day's high), then one local detail that bends the register
without dropping it. In Drizzlewick it rains so often that even the
ducks carry umbrellas -- and today they are trading them in for
sunglasses.
"""

import os

CITY = "Drizzlewick"
CONDITIONS = ("rain easing by eight", "sunny spells", "highs of 17")
LOCAL_COLOUR = "even the ducks are trading their umbrellas in for sunglasses"


def forecast_line() -> str:
    """Assemble the single forecast line from its bulletin parts."""
    bulletin = ", ".join(CONDITIONS)
    return f"{CITY}: {bulletin} \u2014 {LOCAL_COLOUR}."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(forecast_line())


if __name__ == "__main__":
    main()
