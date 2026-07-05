import requests
import pandas as pd


class ChartService:

    BASE_URL = "https://api.exchange.coinbase.com"

    def get_candles(
        self,
        product="BTC-USD",
        granularity=3600
    ):

        url = (
            f"{self.BASE_URL}/products/"
            f"{product}/candles"
            f"?granularity={granularity}"
        )

        try:

            r = requests.get(
                url,
                timeout=10
            )

            r.raise_for_status()

            data = r.json()

            data.sort(key=lambda x: x[0])

            df = pd.DataFrame(
                data,
                columns=[
                    "time",
                    "low",
                    "high",
                    "open",
                    "close",
                    "volume"
                ]
            )

            df["time"] = pd.to_datetime(
                df["time"],
                unit="s"
            )

            return df

        except Exception as e:

            print(e)

            return None