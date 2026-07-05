from core.brains.atlas import Atlas


class AtlasService:

    def __init__(self):

        self.atlas = Atlas()

    def analyze_markets(self, markets):

        analyses = []

        for coin, market in markets:

            analysis = self.atlas.analyze(coin, market)

            analyses.append(analysis)

        return analyses