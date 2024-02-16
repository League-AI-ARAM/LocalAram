from enum import Enum, auto


class Platform(Enum):
    BR1 = auto()
    EUN1 = auto()
    EUW1 = auto()
    JP1 = auto()
    KR = auto()
    LA1 = auto()
    LA2 = auto()
    NA1 = auto()
    OC1 = auto()
    PH2 = auto()
    RU = auto()
    SG2 = auto()
    TH2 = auto()
    TR1 = auto()
    TW2 = auto()
    VN2 = auto()

    def __str__(self):
        return self.name

class Region(Enum):
    AMERICAS = [Platform.BR1, Platform.NA1, Platform.LA1, Platform.LA2]
    ASIA = [Platform.JP1, Platform.KR]
    EUROPE = [Platform.EUN1, Platform.EUW1, Platform.TR1, Platform.RU]
    SEA = [Platform.OC1, Platform.PH2, Platform.SG2, Platform.TH2, Platform.TW2, Platform.VN2]

    @classmethod
    def get_region(cls, platform):
        for region in cls:
            if platform in region.value:
                return region.name
        raise Exception("Could not get region name from platform :" + platform)