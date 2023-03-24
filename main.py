from warming.data.summary import Summary
from warming.plot.maps import World, Europe


def main():
    summary = Summary()
    world = World()
    # world.show(summary.co2(), 'CO2C')
    # world.show(summary.ch4(), 'CH4C')
    # world.show(summary.n2o(), 'N2OC')
    # world.show(summary.co2_year(), 'CO2Y')
    # world.show(summary.ch4_year(), 'CH4Y')
    # world.show(summary.n2o_year(), 'N2OY')

    europe = Europe()
    europe.show(summary.co2(), 'CO2C')


if __name__ == "__main__":
    main()
