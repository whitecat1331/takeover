from dotenv import load_dotenv
from icecream import ic

from takeover import *


def test():
    load_dotenv()
    domains = [os.getenv("DOMAIN"), "www.decisionedge.transunion.com","aemapi.transunion.com"
 ,"youtube.com"]
    result = main(domains=domains)
    ic(result)


if __name__ == "__main__":
    test()
