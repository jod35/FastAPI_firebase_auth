import requests

token = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjhkMDNhZTdmNDczZjJjNmIyNTI3NmMwNjM2MGViOTk4ODdlMjNhYTkiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vZmFzdGFwaWF1dGgtM2YyNmQiLCJhdWQiOiJmYXN0YXBpYXV0aC0zZjI2ZCIsImF1dGhfdGltZSI6MTY4NzU0MTYzNSwidXNlcl9pZCI6Im9DTUozVXZ0MGxWVGFYSlF3Nmt0MHhKbTNTdDIiLCJzdWIiOiJvQ01KM1V2dDBsVlRhWEpRdzZrdDB4Sm0zU3QyIiwiaWF0IjoxNjg3NTQxNjM1LCJleHAiOjE2ODc1NDUyMzUsImVtYWlsIjoic2FtcGxlQGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJlbWFpbCI6WyJzYW1wbGVAZ21haWwuY29tIl19LCJzaWduX2luX3Byb3ZpZGVyIjoicGFzc3dvcmQifX0.ht9CELI9qRJJhQ1a4wMpVB_b_NzMolgIYVN3uEQDaVC3p-WEmtuh_eySPta7GkBaVErmzDUxyzun9xsm7y01s51E7S3vptYYKh3m_g87_hbaOmuflYUuCigDMaEDVBJX-nd4LoaTh0jLogScf05_3oxAQlz---eztUoo9r-qigIMyLHz7e7B_7mT3Te77OYHd5a9VbXFBk-2JmLU0WqjKsIpsY_MJwSGbHKmi6O6j7_WumHxneK4LYx56SzZZEppouU4VzY7gdXU3JQlHFu5Q852h8CP-TB9OkBFjsc4xlOMkTDpEh8ANvXYxvYp5mRMyXvPwPcJjKggnyaOMy8e-Q"


def test_validate_endpoint():
    headers = {
        'authorization':token
    }

    response = requests.post(
        "http://127.0.0.1:8000/ping",
        headers=headers
    )

    return response.text


print(test_validate_endpoint())


