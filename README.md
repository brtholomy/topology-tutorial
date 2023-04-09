# Topology tutorial companion code

This is a very simple concrete introduction to general topology principles.

The idea is to use vanilla Python to illustrate the interaction of subsets and the abstract notion of a "point" divorced from any Cartesian metric.

## Usage

Play with the results like so:

```sh
python subsets.py --radius=4
```

Look for a specific point among the set of subsets, designated as a two-character string of lowercase ascii:

```sh
python subsets.py --find=xu
```

Inspect the intersected set of all points:

```sh
python subsets.py --intersect
```

See all options:

```sh
python subsets.py --help
```

## Contrasting example

The `equidistance.py` exercise is an example dealing with 1 dimensional metric space, and the possible runtime complexities of various search and/or crawl functions within that space.
