# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

## [1.0.1] - 2026-11-02
### Fixed
- Make `search_by_title` case-insensitive (#20).

## [1.0.0] - 2026-11-02

### Added
- Added PR template (`.github/pull_request_template.md`)[cite: 30].
- Added `Cart.print_cart()` method with empty cart handling and integrated it into `main.py`[cite: 31, 32].
- Added `search_by_title()` search feature (#4)[cite: 31].
- Added use case diagram documentation[cite: 31].
- Added discount calculation feature and integrated it into `main.py`[cite: 39].
- Added notification displaying the added DVD title (#11)[cite: 40].

### Fixed
- Fixed bug where `Cart` accepted more than 20 DVDs (#6)[cite: 38].
- Fixed discount total calculation and added percentage validation[cite: 39].

### Changed
- Translated DVD addition confirmation messages to Vietnamese[cite: 40].