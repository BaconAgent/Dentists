from django.test import TestCase
import http.client


class TestLogin(TestCase):
    def setUp(self):
        return

    def test_get_token(self):
        conn = http.client.HTTPSConnection("dev-twctg5mxoooke8y4.eu.auth0.com")

        payload = '{"client_id":"pwUKbbecVvEJEwZ8yj0Jv2heslRSuRAI","client_secret":"cvUX_hQFGZJwx2si0TdgLtCe-LjBqKrC3OLr8Y7A3KiYn8XbE0D1bnPy88b2x-Aq","audience":"https:/dentists-backend","grant_type":"client_credentials"}'

        headers = {"content-type": "application/json"}

        conn.request("POST", "/oauth/token", payload, headers)

        res = conn.getresponse()
        data = res.read()

        print(data.decode("utf-8"))

    def test_send_token(self):

        conn = http.client.HTTPConnection("dev-twctg5mxoooke8y4.eu.auth0.com")

        headers = {
            "authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik80UktlT0RSaHFMQkVOTU9iMHdVUCJ9.eyJpc3MiOiJodHRwczovL2Rldi10d2N0ZzVteG9vb2tlOHk0LmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJwd1VLYmJlY1Z2RUpFd1o4eWowSnYyaGVzbFJTdVJBSUBjbGllbnRzIiwiYXVkIjoiaHR0cHM6L2RlbnRpc3RzLWJhY2tlbmQiLCJpYXQiOjE3MTU2OTA3NDMsImV4cCI6MTcxNTc3NzE0MywiZ3R5IjoiY2xpZW50LWNyZWRlbnRpYWxzIiwiYXpwIjoicHdVS2JiZWNWdkVKRXdaOHlqMEp2Mmhlc2xSU3VSQUkifQ.ENl4Oz-sw1Bo2v8jYBSEXxMptMoHQWjjM0oiZDALCg_xL01AoSwbjtv8tgku4ZPTYMPJIb_MX7Z1G3gPiVB3fCdXABgVZjkJOSBN5qitOEtXELu03h-gzNf8tAgoVRxX1uMkwQEr2CdrSa0KFuLYrXHOQQS7SwNHK5hiEtqezQVtW_BqMjlyvNQQcOLH-N2uRydWBQKjbkcsVpPq-6RSV68zwwf_SHNte5r4wzVd3ID489-hvEkvixSpSfuKI4lHRPMzHoCUgj-X12_OC76e7nWzQAZ0Frb29zu_w_E1UuzvgH1x5mHiEW65l2ZlMzxAy0eiY40P1UNzr2hsKmsOfQ"
        }

        conn.request("GET", "/", headers=headers)

        res = conn.getresponse()
        data = res.read()

        print(data.decode("utf-8"))
