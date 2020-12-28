
class PcData:

    def __init__ (self, cores = 0, rmax = 0, rpeak = 0, power = 0):
        self.cores = cores
        self.rmax = rmax
        self.rpeak = rpeak
        self.power = power

    def divide(self, a):
        self.cores /= a
        self.rmax  /= a
        self.rpeak /= a
        self.power /= a

    def add(self, other):
        self.cores += other.cores
        self.rmax  += other.rmax
        self.rpeak += other.rpeak
        self.power += other.power