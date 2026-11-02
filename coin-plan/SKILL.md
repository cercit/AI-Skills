---
name: coin-plan
description: Research methodology for building complete coin series checklists from a Numista CSV export. ALWAYS activate when the user asks to cross-reference their collection against a series, find gaps in their collection, plan which coins to collect next, suggest new series to pursue, or analyze a Numista export file. Also activate for coin fair shopping lists or series completion planning. This skill covers the full pipeline from CSV parsing through series research to gap analysis and priority ranking.
---

# Coin Collection Planning Methodology

## When to use
- User uploads a Numista CSV export and wants gap analysis
- User asks "what am I missing from [series]"
- User wants to start a new series and needs the complete list
- User asks for coin fair shopping list or buying priorities
- User wants series suggestions based on existing collection patterns

## Step 1: Parse Numista Export

The CSV columns that matter:
```
Country, Issuer, Ruling authority, Title, Type, Face value,
Reference, N# number, Gregorian year, Mintmark, Composition,
Grade, Collection, Comment
```

### Key parsing patterns:

**Design name extraction** — names are in parentheses after portrait info:
```python
import re
m = re.search(r'\((.*?)\)', title)
design_name = m.group(1) if m else title
```

**For multi-portrait series (UK)** — strip portrait prefix:
```python
m = re.search(r'portrait;\s*(.+?)\)', title)
```

**Filter non-circulation** (if the collector excludes silver/gold proofs):
```python
if 'silver' in comp.lower() and 'clad' not in comp.lower():
    continue  # skip pure silver
```

**Dedup by (design, year, mint)** — same design+year+mint = one entry, track count.

## Step 2: Build Series Master List

### Research sources (in order of reliability):
1. **Numista catalogue pages** — authoritative for KM#, dates, compositions
2. **Web search** for series overviews (PCGS, NGC articles, Baidu Baike for China)
3. **Cross-reference** user's Numista export N# numbers against known series

### Series identification from collection patterns:
- Look at `Type` field: "Circulating commemorative" vs "Standard circulation"
- Group by denomination + composition to identify series
- Check year ranges for continuous sequences (gaps = missing coins)

### Common series structures:

| Country | Series | Denomination | Format | Years |
|---------|--------|-------------|--------|-------|
| US | 50 State Quarters | 25c | Cu-Ni clad | 1999-2008 |
| US | DC & Territories | 25c | Cu-Ni clad | 2009 |
| US | America the Beautiful | 25c | Cu-Ni clad | 2010-2021 |
| US | American Women | 25c | Cu-Ni clad | 2022-2025 |
| UK | Round Pound Emblems | £1 | Ni-Brass | 1983-2015 |
| UK | 12-Sided Pound | £1 | Bimetallic | 2016-present |
| China | Lunar Zodiac | 10 Yuan | Bimetallic | 2015-2026 |
| China | World Cultural Heritage | 5 Yuan | Brass | 2002-2006 |
| China | World Heritage Mountains | 5 Yuan | Brass (square) | 2019-present |
| China | Peking Opera | 5 Yuan | Brass | 2023-2027 |
| China | National Parks | 10 Yuan | Bimetallic | 2023-present |
| China | Calligraphy "He" | 5 Yuan | Brass | 2013-2022 |
| China | Famous Sights Taiwan | 5 Yuan | Brass | 2003-2005 |
| China | Red Book Animals | 5 Yuan | Copper | 1995-1998 |
| India | Princely States | Various | Various | Various |

## Step 3: Gap Analysis

### Build collected set:
```python
collected = {}  # (design_name, year) -> set of mints or count
```

### Cross-reference against master:
```python
for year, name in master_list:
    if (name, year) in collected:
        status = "HAVE"
    else:
        status = "NEED"
```

### For mint-variant series (US quarters):
Track P and D separately. Show both as columns — bold if collected, light grey if not.

### For single-variant series (UK pounds, China):
Simple tick/no-tick checkbox.

## Step 4: Suggest New Series

When user asks "what else should I collect", apply these filters:

### Compatibility criteria:
1. **Same denomination/format** as existing collection (if user collects 5 Yuan brass, suggest other 5 Yuan brass series)
2. **Same price range** — circulating commemoratives, not proofs/bullion
3. **Completable** — finite series with known total count
4. **Available** — coins still obtainable from dealers at reasonable prices
5. **Thematic match** — the collector's stated interests (see Collector profile below)

### Priority ranking for suggestions:
- **High**: Same format, same country, <20 coins, cheap, available
- **Medium**: Same country, different format but affordable
- **Low**: Different country but thematic match

## Step 5: Shopping List

### For coin fairs:
- Prioritize by geography (local fairs stock local and regional coins best, e.g. a fair in South India is the best place for South Indian princely states)
- Group by priority: HIGH (likely present), MEDIUM (ask dealers), SPECIALIST (dedicated dealers only)
- Include specific denomination names dealers would recognize
- Add empty checkboxes for ticking off at the fair

### For online buying:
- Note which coins are common circulation (cheap) vs commemorative (premium)
- Flag any coins that are scarce or have high collector demand

## Step 6: Output

Generate output using the `a5-coin` skill for binder-ready PDFs, or Excel with openpyxl for digital tracking.

### Excel output columns:
S.No, Official Name, Year, Denomination, Current State/Country, Region, British Era (for India), In Collection?, Coins Owned, Priority

### PDF output:
Use `a5-coin` skill — Carlito font, grayscale, 6-hole punch, continuous flow layout.

## Collector profile (fill in your own)

Keep this section short and update it as the collection changes. The skill uses it for suggestions and shopping lists.

- Numista username: <your handle>
- Approximate collection size: <number>
- Active sub-collections: <e.g. British Round Pounds, Chinese Lunar Zodiac, US Quarters>
- Printing: <colour / grayscale>, binder: <A5 Filofax / other>
- Home city (for coin fair lists): <city>
- Exclusions: <e.g. no silver/gold proofs>

### Known gaps (date)
- <series>: <have>/<total>, missing <list>
