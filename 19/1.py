from common import get_scanners, get_mappings, normalize

normalize(scanners := get_scanners(), get_mappings(scanners))
print(len({beacon for scanner in scanners for beacon in scanners[scanner]}))
