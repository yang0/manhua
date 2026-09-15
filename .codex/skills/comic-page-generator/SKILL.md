---
name: comic-page-generator
description: Generate a finished comic page from a project style ID, storyboard ID, and theme. Use when the user requests a comic using this project's 120-style and 80-storyboard library.
---

# Comic Page Generator

Create one coherent, finished comic page from three required inputs:

- Style ID: `1`–`120`
- Storyboard ID: `1`–`80`
- Theme: the story, character, event, or message to depict

Accept concise requests such as `风格 36，分镜 79，主题：雨夜侠客在山寺重逢`.

## Workflow

1. Run `scripts/build_prompt.py` with the requested IDs and theme. It reads the maintained source CSV files in `data-and-prompts`; do not guess a style or storyboard definition.
2. If an ID is out of range, ask the user for a valid replacement. If the theme is missing, ask only for the theme.
3. For an image request, send the script's complete output to the available image-generation tool and deliver the resulting image. Do not silently substitute a different style or storyboard.
4. If the user asks only for a prompt, return the script output without generating an image.

The gallery at `gallery.html` is the visual index. Preview images group four consecutive IDs; use the displayed ID labels to choose the matching entry.
