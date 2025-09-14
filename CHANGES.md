Dark-mode white adjustments

- Date: 2025-09-14
- Change: Softened pure white backgrounds and button whites when user's system is in dark mode.
- Files updated:
  - `docs/stylesheets/overrides.css` — added `@media (prefers-color-scheme: dark)` rules to replace bright `white/#fff` with dimmer tones (e.g. `#e6e6e6` and semi-transparent whites).
  - `docs/problems/index.md` — removed inline bright background styles in favor of classes.
  - `docs/algorithms/index.md` — removed inline bright background styles in favor of classes.

Notes:
- MkDocs build completed successfully after the change.
- If you want a different tint, edit the color values in `docs/stylesheets/overrides.css` under the `@media (prefers-color-scheme: dark)` block.
- To preview locally: run `mkdocs serve` and open http://127.0.0.1:8000 in a browser using dark mode.
