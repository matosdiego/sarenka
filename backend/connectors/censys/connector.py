from typing import Dict, Tuple, Sequence, List, NoReturn
import sys
import json
import requests
from censys.certificates import CensysCertificates
from censys.ipv4 import CensysIPv4
from censys.websites import CensysWebsites
from censys.base import CensysNotFoundException, CensysRateLimitExceededException, CensysUnauthorizedException

from connectors.credential import Credential 
from connector_interface import ConnectorInterface
from common.common import Common
from wrappers.ip_wrapper import IPWrapper

class Connector(ConnectorInterface):
    def __init__(self, censys_credentials):
        super().__init__(censys_credentials)

    def search_by_ip(self, ip):
        """
        https://censys.io/ipv4/8.8.8.8
        """
        response = self.ipv4.view(ip)
        return IPWrapper(response)

    def search_by_fingerprint(self, certificate_hash):
        return self.certificate.view(certificate_hash)

    def search_by_website(self, domain):
        return self.website.view(domain)

if __name__ == "__main__":
    censys_credentials = Credential().censys
    connector = Connector(censys_credentials)
    # response = connector.search_by_ip("8.8.8.8") # 
    response = connector.search_by_ip("212.77.98.9") # dziala

    print(response)
    # Common.save_dict_to_file("C:\\Users\\dp\\Desktop\\sarenka\\backend\\connectors\\censys\\censys_ip.json", response)
    # print(connector.search_by_fingerprint("48177e03b47bdcb3b6ab28a92f8005b95302418cd5b9ede77a97eb918e4a2da2"))
    # print(connector.search_by_fingerprint("48177e03b47bdcb3b6ab28a92f8005b95302418cd5b9ede77a97eb918e4a2da2"))