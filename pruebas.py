import json

ads_group = 4
ad_count = 6

with open('jobads3.json', 'r') as archive:
    all_ads = json.load(archive)

remaining_ads = [{"id": ad_id,
                  "aviso": ad_list} for ad_id, ad_list in all_ads[str(ads_group)].items()][ad_count:]

print(remaining_ads[0]["aviso"][4])
