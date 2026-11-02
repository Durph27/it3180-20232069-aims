def search_by_category(items, category):
    return [dvd for dvd in items if dvd.category and dvd.category.lower() == category.lower()]

def search_by_title(title, dvds):
    """Return DVDs whose titles contain ``title``.

    Matching is case-insensitive and preserves the order of ``dvds``.
    """
    return [dvd for dvd in dvds if title.lower() in dvd.title.lower()]