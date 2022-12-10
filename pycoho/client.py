from datetime import date
from typing import List

import requests


class Client:
    """
    Client to interface with the Companies House API.

    Enumerations link:
    https://raw.githubusercontent.com/companieshouse/
    api-enumerations/master/constants.yml
    """

    def __init__(self, api_key) -> None:
        self._domain = "https://api.company-information.service.gov.uk/"
        self._session = requests.Session()

        # Basic authentication with API key as username (no password)
        self._session.auth = (api_key, "")

    def search_all(
        self, q: str = None, items_per_page: int = None, start_index: int = None
    ):
        url = f"{self._domain}search"
        resp = self._session.get(
            url,
            params={
                "q": q,
                "items_per_page": items_per_page,
                "start_index": start_index,
            },
        )
        resp.raise_for_status()
        return resp.json()

    def advanced_company_search(
        self,
        company_name_includes: str = None,
        company_name_excludes: str = None,
        company_status: List[str] = None,
        company_subtype: str = None,
        company_type: List[str] = None,
        dissolved_from: date = None,
        dissolved_to: date = None,
        incorporated_from: date = None,
        incorporated_to: date = None,
        location: str = None,
        sic_codes: List[str] = None,
        size: int = None,
        start_index: str = None,
    ):
        url = f"{self._domain}advanced-search/companies"
        resp = self._session.get(
            url,
            params={
                "company_name_includes": company_name_includes,
                "company_name_excludes": company_name_excludes,
                "company_status": company_status,
                "company_subtype": company_subtype,
                "company_type": company_type,
                "dissolved_from": dissolved_from,
                "dissolved_to": dissolved_to,
                "incorporated_from": incorporated_from,
                "incorporated_to": incorporated_to,
                "location": location,
                "sic_codes": sic_codes,
                "size": size,
                "start_index": start_index,
            },
        )
        resp.raise_for_status()
        return resp.json()
