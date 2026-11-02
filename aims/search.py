def search_by_title(title, dvds):
    """Return DVDs whose titles contain ``title``.

    Matching is case-insensitive and preserves the order of ``dvds``.
    """
    return [dvd for dvd in dvds if title.lower() in dvd.title.lower()]