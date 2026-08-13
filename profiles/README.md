# Team profiles

One JSON file per person, checked in here the same way you'd contribute
anything else to this repo — edit or add your file and open a PR. The
[Team view](../team.html) reads every `*.json` file in this folder straight
from GitHub (client-side, no backend) and renders it as a gallery, so
whoever's file is here *is* the team. There's no separate roster to update.

## Adding your profile

1. Open the [explorer](../ds-skills-explorer.html), set your name and GitHub
   username in the toolbar, and set the nine sliders to your self-assessed
   levels (see [`skill-level-rubric.md`](../skill-level-rubric.md) if you want
   a defensible score rather than a quick pass).
2. Click **Save profile (JSON)**. It downloads a file named after your GitHub
   username.
3. Commit it into this folder as `profiles/<your-github-username>.json` (add
   or overwrite) and open a PR, same as any other change to this repo.

Re-run the same steps whenever your profile changes — the new commit
overwrites the old file, so the Team view always reflects your latest save.
There's currently no history kept beyond git's own (see issues #13 / #25 for
that as a separate piece of work).

## Schema

```json
{
  "name": "Full Name",
  "github": "githubusername",
  "updated": "2026-08-13",
  "values": [3, 3, 3, 2, 2, 3, 3, 3, 2]
}
```

- `github` **must** match the filename (`profiles/<github>.json`) — the Team
  view uses the filename to link to your GitHub profile.
- `values` is nine numbers, 0–4 in 0.5 steps, in the same fixed axis order as
  the explorer's sliders: Statistics & Modeling, AI Foundations, AI Agents &
  Frameworks, Programming, Data Engineering, Visualization, Communication,
  Storytelling, Domain Knowledge.

`example.json` is a placeholder profile (not a real person) kept here so the
Team view always has at least one card to render — delete it once real
profiles exist.
