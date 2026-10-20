# Getting Mashhad-e-Hind to the top of Google

Nobody can guarantee the first position on Google. But the official website of a
place usually ranks first for that place's name once Google trusts it. The site
already does its part: page titles, descriptions, links between the language
versions, structured data naming the shrine, and a sitemap. The steps below are
the ones only the site owner can take. They are in order of impact.

## 1. Use a proper domain name

An address like `mashhadehind.org` looks official and ranks much better than
`mashhad-e-hind-website.pages.dev`.

- **First check whether the committee owns `mashadehind.in`.** That site already
  shows up for searches about the shrine. If it is the committee's, point that
  domain at this website. Google then carries the old site's standing over.
- Otherwise, buy a new domain, for example from Cloudflare (**Domain Registration**
  in the dashboard).
- In the Cloudflare Pages project, open **Custom domains → Set up a custom domain**
  and enter it.
- Tell Claude the new address, so every page's links and the sitemap use it.

## 2. Register the site with Google Search Console

1. Go to https://search.google.com/search-console and sign in with a Google account.
2. Click **Add property**. With a custom domain, choose **Domain** and follow the
   steps to add a DNS record in Cloudflare. Without one, choose **URL prefix**,
   enter `https://mashhad-e-hind-website.pages.dev/`, pick **HTML tag** and send the
   tag to Claude to add to the site.
3. Once it's verified, open **Sitemaps** and submit `sitemap.xml`.
4. Open **URL inspection**, enter the home page address and click **Request indexing**.

## 3. Claim the shrine on Google Maps

Searches for a place name often show the Google Maps listing above the website
results.

1. Search for the shrine on Google Maps. If a listing exists, click **Claim this
   business** (or **Own this business?**). If none exists, use **Add a missing place**.
2. Use the name "Mashhad-e-Hind (Panj Peer Mazar)", the category "Shrine", the
   exact location pin, opening hours and photos.
3. Add the website address to the listing.

## 4. Link to the site from the shrine's own pages

Links from places people already trust tell Google which site is the real one.

- Add the website address to the shrine's Facebook pages and YouTube channel
  descriptions.
- Ask anyone who has written about the shrine (news sites, heritage blogs, local
  directories) to link to it.
- Share it in community WhatsApp groups when it launches.

## 5. Keep the site complete and current

- Replace the yellow placeholders with real timings, events and contact details.
- Add photographs of the shrine and the inscription, each with a short description.
- Post each year's majlis dates on the Events page.

Expect it to take a few weeks after step 2 before the site appears in results.
