# Hub2U website (hub2u.net) — project notes for Claude

This repo is ONLY the public website. It is separate from the Hub2U app repo `hsong` — never mix them.

## Repo layout
- `docs/` — the live site (GitHub Pages: branch `main`, folder `/docs`). Do not put anything private here.
- `tools/build_site.py` — generates the 9 HTML pages (+404) into `docs/`. Edit text there, then run `python3 tools/build_site.py`.
- `docs/assets/js/config.js` — the one place to fill real info (phone, LINE, hours, links, fees). Empty values show orange `[ใส่...]` badges.
- `content/` — approved Thai copy per page; `content/00_missing-info_th.md` is the checklist of missing info.
- `design/` — Google Stitch exports (reference only, not served).

## Rules
- Answer the owner in simple Thai. Owner works alone with Claude.
- Spell "Hub2U" only. No competitor names.
- Never invent phone, LINE ID, links, QR codes, logo. Use `[ใส่...]` placeholders.
- No prices, discounts, coupons, points, reviews, App Store badges. Don't imply many shops (now 1 shop, 1 rider).
- Delivery only within 7 km straight-line of Wisitchai Market. Customers prepay via PromptPay.
- Do not write "จ่ายเงินทุกเย็น" until the owner confirms.
- Contact page has no form. Repo is public: no secrets.
- Commits: `git -c user.name="pisaen666" -c user.email="pisaen66@gmail.com"`.

## Status
- 9 pages built and live at https://pisaen666.github.io/hub2u-website/
- Waiting on owner: contact info, links, fees, logo (`docs/assets/img/logo.png`), real photos, domain hub2u.net (then add custom domain in Pages settings + CNAME).
