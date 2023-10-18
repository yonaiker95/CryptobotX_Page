import requests

def data_pool():
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
        headers = {
            "User-Agent": user_agent,
            'referer': 'https://www.google.com'
        }
        url = 'https://pool.binance.com/mining-api/v1/public/pool/index'
        r = requests.get(url, headers=headers, timeout=10)
        datos = r.json()
        btcpool = []
        etcpool = []

        # Utiliza f-strings para formatear las cadenas
        btcsymbol = datos['data']['algoList'][0]['symbolInfos'][0]['symbol']
        btceffectiveCount = datos['data']['algoList'][0]['effectiveCount']
        btcpoolHash = f"{float(datos['data']['algoList'][0]['poolHash']) / 1e18:.2f}"
        btcallHash = f"{float(datos['data']['algoList'][0]['symbolInfos'][0]['allHash']) / 1e18:.2f}"
        
        etcsymbol = datos['data']['algoList'][2]['symbolInfos'][0]['symbol']
        etceffectiveCount = datos['data']['algoList'][2]['effectiveCount']
        etcpoolHash = f"{float(datos['data']['algoList'][2]['poolHash']) / 1e12:.2f}"
        etcallHash = f"{float(datos['data']['algoList'][2]['symbolInfos'][0]['allHash']) / 1e12:.2f}"

        btcpool.append(btcsymbol)
        btcpool.append(btceffectiveCount)
        btcpool.append(btcpoolHash)
        btcpool.append(btcallHash)
        etcpool.append(etcsymbol)
        etcpool.append(etceffectiveCount)
        etcpool.append(etcpoolHash)
        etcpool.append(etcallHash)
        return btcpool, etcpool

def search_payment():
        pass