# Mashhad-e-Hind, Samana — website

A static website for Mashhad-e-Hind (Panj Peer Mazar), the shrine of Imamzada Syed
Mashhad Ali in Samana, Patiala district, Punjab. Plain HTML and CSS, no build step.

## Languages

| Language | Folder | Notes |
|---|---|---|
| English | `/` | |
| Urdu | `/ur/` | Right-to-left layout, Noto Nastaliq Urdu font |
| Punjabi | `/pa/` | Gurmukhi script, Noto Sans Gurmukhi font |

Each page links to the same page in the other two languages. The Urdu and Punjabi text
was translated from the English and **should be reviewed by a native speaker** before
the site goes live. A Punjabi Shahmukhi version (`/pnb/`) could be added later the same
way, reusing the Urdu right-to-left styling.

## Pages

`index.html` (home), `history.html`, `timings.html`, `events.html`, `contact.html`,
`location.html`, in each language folder, plus `404.html`.

## Placeholders

Anything not yet confirmed is shown in a yellow dashed box like
`<span class="placeholder">[phone number]</span>`. Replace the whole span with the
confirmed text. Paragraphs with `class="uncertain"` flag history the committee should
review. `RESEARCH-NOTES.md` lists the source for each historical statement and what the
committee needs to confirm.

## Editing

Edit the `.html` files directly, or edit the content in `tools/generate.py` and run
`python3 tools/generate.py` to rewrite all 18 pages at once (useful for changes to the
menu or footer). Cloudflare does not run this script; it only serves the HTML.

## Deploying to Cloudflare Pages

1. Push this folder to a GitHub repository.
2. In the Cloudflare dashboard, go to **Workers & Pages → Create → Pages → Connect to Git**
   and choose the repository.
3. Build settings: **Framework preset: None**, **Build command: (leave empty)**,
   **Build output directory: `/`**.
4. Click **Save and Deploy**. The site will be live at `<project-name>.pages.dev`.
5. Optional: under the project's **Custom domains** tab, add your own domain.

Every later push to the main branch redeploys the site automatically.

Without GitHub, you can instead use **Create → Pages → Upload assets** and drag in this
folder.
