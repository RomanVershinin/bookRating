def copy():
    import json
    from portal.models import Books

    file_json = 'data.json'

    with open(file_json) as f:
        data = json.load(f)

    for item in data:
        b = Books()
        b.Description = item['Description']
        b.Year = item['Year']
        b.id = item['ID']
        b.PopularityRating = item['PopularityRating']
        b.BookTitle = item['BookTitle'][1:-1]
        b.Author = item['Author']
        b.Genre = item['Genre']
        b.FirstPoblicationYear = item['FirstPoblicationYear']
        b.Publisher = item['Publisher']
        b.OriginalLanguage = item['OriginalLanguage']
        b.Country = item['Country']
        b.save()
