from httpx import get
import os


def get_response_for(keyword, results_per_page, page=1):
    """
    This function makes an HTTP request to the Unsplash API to get
    photos based on the given keyword and number of results per page.

    Args:
        keyword (str): The keyword to search for.
        results_per_page (int): The number of results to return per page.

    Returns:
        dict: The JSON response from the API.

    Raises:
        HTTPError: If the request returns an error.
    """
    #url = f"https://unsplash.com/napi/search/photos?per_page={results_per_page}&query={keyword}&xp=semantic-search%3Acontrol"
    url = f"https://unsplash.com/napi/search/photos?page={page}&per_page={results_per_page}&query={keyword}&xp=semantic-search%3Acontrol"
    resp = get(url)

    if resp.status_code == 200:
        return resp.json()
    
def get_img_urls(data):
    results = data["results"]

    img_urls = [x["urls"]["raw"] for x in results if x["premium"] is False]
    img_urls = [x.split("?")[0] for x in img_urls]
    return img_urls

if __name__ == "__main__":
    #print(get_response_for("python", 3))
    data = get_response_for("python", 3)
    print(get_img_urls(data))