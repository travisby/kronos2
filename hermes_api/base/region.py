class Region(object):
    code = ''


class NorthAmerica(Region):
    code = 'NA'


class Europe(Region):
    code = 'EU'


class AsiaPacific(Region):
    code = 'AP'


def get_region_by_code(code):
    if code == 'NA':
        return NorthAmerica()
    elif code == 'EU':
        return Europe()
    elif code == 'AP':
        return AsiaPacific()
    return Region()
