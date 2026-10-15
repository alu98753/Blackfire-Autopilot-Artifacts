# Blackfire Autopilot Public Landing Page — V1

Status: Final product/content definition

This document is a lightweight website contract. It is **not** a Blackfire Autopilot runtime task package and does not participate in the private repository task lifecycle.

## Purpose

Create one durable public entry point where a Blackfire Crusade player can quickly understand:

1. what Blackfire Autopilot is;
2. how it reduces repetitive grinding;
3. how it can improve resource collection while the player is away;
4. which core Activities it can automate;
5. how it handles daily/resource work, bag maintenance, stamina/cooldown situations, and user rules;
6. where to get the latest beta through Discord;
7. where to watch a real demo on YouTube.

The page is a product landing page, not developer documentation.

## Messaging direction

Primary tone: efficiency / progress / resource optimization.

Secondary emotional benefit: spend less active time repeating chores and more time enjoying the parts of the game the player actually wants to play.

Primary headline direction:

> Automate the grind. Maximize your progress.

## Information order

1. Hero / product promise
2. Bread quantitative hook
3. Battle Activities
4. Daily + Resource automation
5. Bag Automation
6. Smart Recovery / Safety
7. Your Rules
8. Discord + YouTube CTA
9. Small FAQ

## Bread hook

Known game rule used by the first quantitative section:

- 1 Bread per 80 seconds
- Bakery capacity: 160 Bread
- capacity reached in roughly 3 hours 33 minutes
- theoretical 24-hour production: roughly 1,080 Bread

The page must not imply every manual player collects only once per day. The 160 vs ~1,080 example is explicitly labeled as a one-daily-check-in example and says actual gain depends on the player's normal collection frequency.

## Core public Activities

### Battle

- Stage
- Dungeon
- Domain
- Lord Boss
- Demon Lords

### Daily / Resource

- Bread Collection
- Diamond Collection
- Mystery Chest
- Hero Draw
- Blood Altar
- Bulletin Board

### Maintenance

- Automatic Bag Cleanup
- Bag Sorting
- Full Bag Protection
- Blood Sacrifice
- Item Selling

## Smart behavior framing

Do not expose internal state-machine names. Explain behavior from the player perspective, for example:

> No stamina → stop the current farming flow safely → return to Town → wait / collect useful resources → resume when appropriate.

The product should be framed as managing a farming loop, not as a simple mouse macro.

## User control framing

Use the message:

> Automation does the repetitive work. You decide the rules.

Examples include enabled Activities, targets, cooldown continuation policy, and bag cleanup quality choices.

## CTA

Primary: Discord

- purpose: get/download the latest Blackfire Autopilot beta and chat with other players
- URL remains a placeholder until supplied by the product owner

Secondary: YouTube

- purpose: watch Blackfire Autopilot running in real Blackfire Crusade gameplay
- URL remains a placeholder until supplied by the product owner

## Placeholder contract

Missing evidence/media does not block the V1 layout. Every missing real asset must be visibly labeled in Traditional Chinese so it can be replaced later without redesigning the page.

Examples:

- `[PLACEHOLDER：Blackfire Autopilot 實際執行畫面]`
- `[PLACEHOLDER：Dungeon 自動戰鬥實際畫面]`
- `[PLACEHOLDER：背包自動清理前後比較圖]`
- `[PLACEHOLDER：Discord Channel URL]`
- `[PLACEHOLDER：YouTube Demo URL]`

## Art direction

- dark, game-tool visual language
- high contrast and readable over imagery
- avoid generic corporate SaaS styling
- use game imagery as atmosphere, not as a replacement for feature explanation
- main background may cross-fade between 3–5 pre-generated montage images
- respect `prefers-reduced-motion`

## Montage build/cache contract

Private template PNGs are source inputs only. They are not copied wholesale into this public repository.

Build flow:

```text
private templates/*.png
        ↓
source file path + bytes SHA-256
        ↓
manifest source_hash comparison
        ↓
unchanged + outputs exist → CACHED / no rebuild
changed → deterministic montage generation
        ↓
public assets/montage/montage-XX.jpg
        + assets/montage/manifest.json
```

Website runtime only loads the already-generated files from the manifest. It never composites the source PNGs in the browser.

## V1 FAQ

Keep the FAQ short. It may state the current beta boundary at a high level: Windows 10/11 64-bit, Traditional Chinese Blackfire Crusade interface, 1920×1080 recommended, and Beta status. Detailed unsupported-case documentation does not belong on the landing page.

## V1 completion criterion

A new player should be able to answer within a short visit:

- What is this?
- What repetitive work does it remove?
- What resources/progress can it preserve or increase?
- What can it farm?
- What happens to Daily work and a full bag?
- What happens when stamina/cooldown prevents progress?
- Can I control what it does?
- Where do I download/join?
- Where do I see a demo?
