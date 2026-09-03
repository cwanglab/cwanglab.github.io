# Consent and photograph request

The People page now lists everyone recorded in the CV, with the statement that
entries are published with the person's consent and a removal contact in the
footer. That statement needs to be true. Send the message below once to each
group, then record replies in the table at the bottom of this file.

Two things are collected in one round trip: the opt-in, and the headshot that
both website generations currently lack.

---

## A. Current doctoral researchers (11)

Amir Javadi Rad · Boyan Si · Ehsan Mohammadi Pasand · Keji Soaga ·
Lukas Jurcaga · Luyando Mbozi · Meng Wu · Qin Jiang · Theo Harrison-Drummond ·
Xiaopeng Wu · Yuchen Pan

**Subject:** Your entry on the group website

> Hello,
>
> The group website now has a People page: https://cwanglab.github.io/people/
>
> Your entry currently shows your name, "PhD Researcher", your affiliation, and one
> sentence describing your funding route and start year. Please reply to confirm you
> are happy for it to appear, and tell me if anything is wrong or you would like it
> worded differently.
>
> If you would like a photograph on the page, attach one — head and shoulders, any
> reasonable resolution. It is entirely optional; the page works without it.
>
> If you would rather not be listed at all, just say so and I will remove the entry.
> No explanation needed.
>
> Best wishes,
> Chengjia

---

## B. Master's, undergraduate and intern alumni (20)

Aaron Bhasker · Aman Valera · Anxue Zheng · Dylan Wintle · Erzhizhi Hu ·
Ethan Smyth · Hongbo Li · Isla Gunn · Jinglei Liu · Joseph Sunley ·
Kyle Mckay · Malachy Hayward · Mariya Sebastian · Miebaka Glory Worika ·
Murtaza Akhtar · Tejaa Sei Kommuri · Xiaoming Ji · Xinyu Zhu ·
Yann Schlosser · Yuchen Mao

These appear as a roster line only — name plus programme and years, with no
individual page. Nothing else about them is published.

**Subject:** Your project with the group — website listing and where you are now

> Hello,
>
> I have put together a page listing the researchers who have worked with the group:
> https://cwanglab.github.io/people/
>
> You are listed under master's, undergraduate and intern researchers, with your
> programme and the years of your project. Please reply if you would prefer not to be
> listed, or if any detail is wrong — I will change or remove it straight away.
>
> If you are happy to say where you are now, I would like to add it. Prospective
> students find that more useful than anything else on the page, and it is the one
> thing the site is still missing.
>
> Best wishes,
> Chengjia

---

## Recording replies

| Person | Group | Consent | Photo | Destination | Date |
|---|---|---|---|---|---|
| | | | | | |

**Applying a reply**

- Photograph: save to `static/images/people/<slug>.jpg`, then set
  `photo: "/images/people/<slug>.jpg"` in `content/people/<slug>.md`.
  The People page swaps the monogram for the photo automatically.
- Destination: set `alumni_destination: "…"` in the same file.
- Withdrawal: delete the file. Nothing else references it.
