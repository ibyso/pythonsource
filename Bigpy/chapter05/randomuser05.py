import requests
import csv

def get_github_top_repos() :
    url = "https://api.github.com/search/repositories"
    params={
        "q" : "language:python",
        "sort":"stars",
        "order":"desc",
        "per_page":10
    }

    res = requests.get(url,params=params)
    data=res.json()
    items = data['items']
    print(items)

    print("========= 인기 저장소 TOP 10 ==========")
    results = []
    for i, item in enumerate(items, 1) :
        name = item['full_name']
        stars = item['stargazers_count']
        html_url = item['html_url']

        print(f"{i}위 | {name} | ⭐{stars:,} | {html_url}")

        results.append({
            "순위" : i,
            "이름" : name,
            "star수" : stars,
            "URL" : html_url
        })

    print()
    print("=== star 10,000개 이상 저장소 ===")
    high_star_repos = [r for r in results if r["star수"] >= 10000]
    for r in high_star_repos :
        print(f"{r['이름']} {r['star수']:,}")

    #csv 저장(csv 저장시 필수, newline)
    csv_path = "C:/source/pythonsource/Bigpy/py_scrap/data/github_top10.csv"
    with open(csv_path, "w", newline="", encoding="utf-8-sig") as f :
        writer = csv.DictWriter(f, fieldnames=["순위","이름","star수","URL"])
        writer.writeheader()
        writer.writerows(results)

    print("csv 저장 완료")



if __name__ == "__main__":
    get_github_top_repos()