import requests
import time
import os

class Scanner:
    def __init__(self, api_key):
        self.api_key = api_key

    def _verificar_virus_virustotal(self, arquivo):
        url = 'https://www.virustotal.com/vtapi/v2/file/scan'
        params = {'apikey': self.api_key}

        with open(arquivo, 'rb') as f:
            files = {'file': (arquivo, f)}
            response = requests.post(url, files=files, params=params)
            json_response = response.json()

            resource = json_response['resource']
            scan_id = json_response['scan_id']

            return resource, scan_id

    def _obter_relatorio_virustotal(self, resource):
        url = f'https://www.virustotal.com/vtapi/v2/file/report'
        params = {'apikey': self.api_key, 'resource': resource}

        response = requests.get(url, params=params)
        json_response = response.json()

        return json_response
    

    def start(self, arquivo):
        number = 15
        resource, scan_id = self._verificar_virus_virustotal(arquivo)
        print(f'Scan ID: {scan_id}')

        for i in range(number):
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"faltam {number} segundos para continuar")
            number -= 1
            time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        input('Pressione Enter para continuar após o upload...')

        relatorio = self._obter_relatorio_virustotal(resource)

        if relatorio['response_code'] == 1:
            print(f'Resultados para o arquivo {arquivo}:')
            for scan, resultado in relatorio['scans'].items():
                print(f'{scan}: {resultado["result"]}')
        else:
            print('O relatório não está disponível.')

