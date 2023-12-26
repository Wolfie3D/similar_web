import datetime

class Pages:
    def parse_data(self, raw_data, fields):
        try:
            raw = raw_data.json()
        except:
            print(raw_data.text)
            raise

        country_rank_dict = raw.get('CountryRank', {})
        category_rank_dict = raw.get('CategoryRank', {})
        engagements = raw.get('Engagments', {})
        fields.update({
            'url': self.url,
            'domain': self.domain,
            'global_rank': raw.get('GlobalRank', {}).get('Rank'),
            'country_rank': country_rank_dict.get('Rank'),
            'country': self.country_name(country_rank_dict.get('CountryCode')),
            'category': category_rank_dict.get('Category'),
            'category_rank': category_rank_dict.get('Rank'),
            'bounce_rate': self.get_perc(engagements.get('BounceRate')) + '%',
            'pages_per_visit': round(float(engagements.get('PagePerVisit', 0)), 2),
            'monthly_visit': engagements.get('Visits'),
            'avg_visit_duration': self.get_duration(engagements.get('TimeOnSite')),
        })

        for date, visit in raw.get('EstimatedMonthlyVisits', {}).items():
            dt = datetime.datetime.strptime(date, '%Y-%m-%d')
            month_short_name = dt.strftime('%b').lower()
            fields[f'{month_short_name}_2023_visits'] = visit

        rank_country_list = raw.get('TopCountryShares', [])
        pos = 1
        for country in rank_country_list:
            code = self.country_name(country.get('CountryCode', ''))
            perc = round(float(country.get('Value', '')) * 100, 2)
            fields[f'country{pos}'] = code
            fields[f'country{pos}_percentage'] = str(perc) + "%"
            pos += 1

        return list(fields.values())
