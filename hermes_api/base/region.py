import json


class Region(object):
    code = ''

    def repr(self):
        return json.dumps(
            {
                self.code: ''
            }
        )


class NorthAmerica(Region):
    code = 'NA'


class Europe(Region):
    code = 'EU'


class AsiaPacific(Region):
    code = 'AP'


def code_to_region(code):
    if code == 'NA':
        return NorthAmerica()
    elif code == 'EU':
        return Europe()
    elif code == 'AP':
        return AsiaPacific()
    return Region()
