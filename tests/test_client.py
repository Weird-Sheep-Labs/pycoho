from unittest import TestCase

from requests import HTTPError

from pycoho import BaseClient


class TestBaseClient(TestCase):
    def setUp(self) -> None:
        self.base_client = BaseClient(api_key="dummy_api_key")
        return super().setUp()

    def test_company_profile(self):
        # Doesn't matter what the actual response is
        expected_return = {"test": "response"}
        self.mocked_request.return_value = self._mocked_response(200, expected_return)
        returned = self.base_client.company_profile(company_number="012345")
        assert returned == expected_return
        self.mocked_request.assert_called_once_with(
            "GET",
            "https://api.company-information.service.gov.uk/company/012345",
            allow_redirects=True,
        )

    def test_search_all(self):
        # Doesn't matter what the actual response is
        expected_return = {"test": "response"}
        self.mocked_request.return_value = self._mocked_response(200, expected_return)
        returned = self.base_client.search_all(q="tesco")
        assert returned == expected_return
        self.mocked_request.assert_called_once_with(
            "GET",
            "https://api.company-information.service.gov.uk/search",
            params={"q": "tesco", "items_per_page": None, "start_index": None},
            allow_redirects=True,
        )

    def test_search_companies(self):
        # Doesn't matter what the actual response is
        expected_return = {"test": "response"}
        self.mocked_request.return_value = self._mocked_response(200, expected_return)
        returned = self.base_client.search_companies(q="tesco")
        assert returned == expected_return
        self.mocked_request.assert_called_once_with(
            "GET",
            "https://api.company-information.service.gov.uk/search/companies",
            params={
                "q": "tesco",
                "items_per_page": None,
                "start_index": None,
                "restrictions": None,
            },
            allow_redirects=True,
        )

    def test_advanced_company_search(self):
        # Doesn't matter what the actual response is
        expected_return = {"test": "response"}
        self.mocked_request.return_value = self._mocked_response(200, expected_return)
        returned = self.base_client.advanced_company_search(
            company_name_includes="tesco", company_status="active", company_type=["ltd"]
        )
        assert returned == expected_return
        self.mocked_request.assert_called_once_with(
            "GET",
            "https://api.company-information.service.gov.uk/advanced-search/companies",
            params={
                "company_name_includes": "tesco",
                "company_name_excludes": None,
                "company_status": "active",
                "company_subtype": None,
                "company_type": ["ltd"],
                "dissolved_from": None,
                "dissolved_to": None,
                "incorporated_from": None,
                "incorporated_to": None,
                "location": None,
                "sic_codes": None,
                "size": None,
                "start_index": None,
            },
            allow_redirects=True,
        )

    def _mocked_response(self, status, json, ok=True):
        class Response:
            def __init__(self, status, json, ok):
                self.status = status
                self._json = json
                self.ok = ok

            def json(self):
                return self._json

            def raise_for_status(self):
                if not self.ok:
                    raise HTTPError

        return Response(status, json, ok)
