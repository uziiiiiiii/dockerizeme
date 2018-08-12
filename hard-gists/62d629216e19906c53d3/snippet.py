import fiona
import click
from rasterio import features, Affine

def makeAffine(bounds, width):
    xD = bounds[2] - bounds[0]
    yD = bounds[3] - bounds[1]
    cS = xD / float(width - 2)

    height = int(yD / cS) + 1

    return Affine(cS, 0.00, bounds[0] - cS,
        0.00, -cS, bounds[3] + cS), height + 1

@click.command()
@click.argument('src_path', type=click.Path(exists=True))
@click.option('--width', type=int, default=100)
def printAscii(src_path, width):
    with fiona.open(src_path, 'r') as src:
        aff, height = makeAffine(src.bounds, width)
        rasarr = features.rasterize(
            ((feat['geometry'], 8) for i, feat in enumerate(src)),
            out_shape=(height, width),
            transform=aff
            )

        for i in rasarr:
            click.echo((''.join(i.astype(str).tolist())).replace('0', '.'))

if __name__ == '__main__':
    printAscii()

# USAGE
#
# $ python printascii.py <inputgeojson> --width 50
# ..................................................
# .............88888.....................88.........
# ........8888888888....8.............888888.88888..
# ...........888888888..........8...........8888....
# ............................888888................
# ..........................88888888888.............
# ........................8888888888888888..........
# .......................8888888888888888888........
# .....................88888888888888888888888......
# ...................888888888888888888888888888....
# .................888888888888888888888888888888...
# ...............88888888888888888888888888888888...
# ..............8888888888888888888888888888888.....
# ...............888888888888888888888888888........
# .................8888888888888888888888...........
# ...................88888888888888888..............
# .88888888888888888..88888888888888................
# .88888888888888888....888888888...................
# .88888888888888888......8888....88888888888888888.
# .88888888888888888..............88888888888888888.
# .88888888888888888..............88888888888888888.
# .88888888888888888..............88888888888888888.
# .88888888888888888..............88888888888888888.
# .88888888888888888..............88888888888888888.
# .88888888888888888..............88888888888888888.
# .88888888888888888..............88888888888888888.
# ................................88888888888888888.
# ................................88888888888888888.
# ................................88888888888888888.
# ................................88888888888888888.
# ..................................................