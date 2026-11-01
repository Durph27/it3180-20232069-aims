def search_by_title(title, dvds):
    """Return DVDs whose titles contain ``title``.

    Matching is case-insensitive and preserves the order of ``dvds``.
    """
    normalized_title = title.casefold()
    return [dvd for dvd in dvds if normalized_title in dvd.title.casefold()]