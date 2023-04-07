# Simple general topology using permutations of the ascii alphabet.

import click


ALPHABET = [chr(i) for i in range(97, 123)]


def GetAlphabetPoint(x, y):
  """Construct point designation using x and y coordinates, allowing for looping
  boundary condition.
  """
  a = ALPHABET[x % len(ALPHABET)]
  b = ALPHABET[y % len(ALPHABET)]
  return a + b


def SubsetSize(radius):
  """Calculate size of the subset given a radius.

  'radius' is used loosely here, since we're dealing with a square matrix. But
  that's valid in topology since the distance function is mutable. This is
  effectively therefore the definition of ᴨr**2 in this space.
  """
  return (1 + 2*radius)**2


def MakeTopos(ymax, xmax, radius):
  topos = []
  for y in range (ymax):
    for x in range(xmax):
      subset = set()

      for suby in range(y - radius, y + radius + 1):
        for subx in range(x - radius, x + radius + 1):
          # Rendered as string, to emphasize that this is not a coordinate pair.
          # It's an abstract "point".
          subset.add(GetAlphabetPoint(subx, suby))

      topos.append(subset)
  return topos


def RenderSet(subset):
  return ','.join(p for p in subset)


def UniquePoints(topos):
  unique_map = set()
  for sub in topos:
    for point in sub:
      unique_map.add(point)
  return unique_map


def IntersectedPoints(topos):
  # hack to get it started
  intermap = topos[0].intersection(topos[1])
  for x,sub in enumerate(topos):
    intermap = sub.intersection(intermap)
  return intermap


def FindPoint(topos, point):
  submap = []
  for sub in topos:
    for subpoint in sub:
      if point == subpoint:
        submap.append(sub)
  return submap


@click.command()
@click.option(
    '--xmax',
    default=20,
    show_default=True,
    help='range of the x axis of our matrix'
)
@click.option(
    '--ymax',
    default=20,
    show_default=True,
    help='range of the y axis of our matrix'
)
@click.option(
    '--radius', '-r',
    default=2,
    show_default=True,
    help='radius of constructed subsets'
)
@click.option(
    '--find', '-f',
    type=str,
    help='point to search for. Two character string, lowercase.'
)
@click.option(
    '--unique', '-u',
    is_flag=True,
    help='whether to print out the unique set of all points.'
)
@click.option(
    '--intersect', '-i',
    is_flag=True,
    help='whether to print out the intersected set of all points.'
)
def Main(xmax, ymax, radius, find, unique, intersect):
  print("xmax:", xmax, "ymax:", ymax, "radius:", radius)
  topos = MakeTopos(ymax, xmax, radius)

  print("total subsets: ", len(topos))
  print("subset size: ", SubsetSize(radius))
  print("total nonunique points: ", len(topos) * SubsetSize(radius))

  if unique:
    unique_map = UniquePoints(topos)
    print("\n unique point collection:")
    print("\n unique point size: ", len(unique_map))
    print(RenderSet(unique_map))

  if intersect:
    print("\n intersected point collection:")
    intermap = IntersectedPoints(topos)
    print(RenderSet(intermap))

  if find:
    sublist = FindPoint(topos, find)
    print(f"\n subsets containing {find}: {len(sublist)}")
    print(
    f"\n subset granularity: {len(sublist)}/{len(topos)} = {len(sublist) / len(topos)}")


if __name__ == '__main__':
  Main()
