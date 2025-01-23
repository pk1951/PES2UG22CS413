from locust import task, run_single_user, FastHttpUser


class BrowseUser(FastHttpUser):
    """
    Locust user simulating browsing behavior.
    """
    host = "http://localhost:5000"
    default_headers = {
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
        "DNT": "1",
        "Sec-GPC": "1",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0",
    }

    @task
    def browse(self):
        """
        Task to simulate browsing the /browse endpoint.
        """
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8",
            "Host": "localhost:5000",
            "Priority": "u=0, i",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "cross-site",
            "Upgrade-Insecure-Requests": "1",
        }
        with self.client.get(
            "/browse",
            headers=headers,
            catch_response=True,
        ) as response:
            if response.status_code != 200:
                response.failure(f"Unexpected status code: {response.status_code}")
            else:
                response.success()


if __name__ == "__main__":
    run_single_user(BrowseUser)
