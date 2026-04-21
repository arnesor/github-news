# GitHub New Releases Report 2026-04-21

**[marimo-team/marimo 0.23.2](https://github.com/marimo-team/marimo/releases/tag/0.23.2)**

Marimo 0.23.2 introduces significant enhancements to the `marimo-pair` AI-coding experience and transitions the slides engine to **reveal.js** for more robust presentations. The update also prioritizes data visualization clarity and backend stability with several security patches and UI refinements.

### Highlights
* **marimo-pair Evolution**: Significant quality-of-life improvements for the AI-assisted coding mode, including auto-save, column support, and a new `better_inspect` module for enhanced discovery.
* **Presentation Overhaul**: Swapped the underlying slides engine from Swiper to **reveal.js**, offering a more standard and powerful framework for notebook-based presentations.
* **Data Visualization Fidelity**: Tables now visually distinguish between `null`, `NaN`, `empty`, and `Infinity` values, and Matplotlib renders now decouple resolution (DPI) from display size for sharper outputs.

### 🚨 Breaking Changes
* **`mo.ui.refresh`**: Updated typing and documentation. Users relying on specific type-hinting or undocumented behavior for this UI element may need to update their implementations.

### Priority
This release is classified as **Breaking** due to the explicitly listed changes to the `mo.ui.refresh` API, alongside significant feature additions to the presentation and AI-pairing systems.
---
**[narwhals-dev/narwhals v2.20.0](https://github.com/narwhals-dev/narwhals/releases/tag/v2.20.0)**

### Narwhals v2.20.0 Release Analysis

#### Summary
Narwhals v2.20.0 introduces significant API enhancements including fluent conditional chaining and a new top-level struct function. This update also features a major documentation overhaul to Zensical to provide a more streamlined developer experience.

#### Highlights
- **`when/then` Chaining:** Enables more expressive and readable conditional logic, allowing users to chain multiple conditions fluently within expressions.
- **Top-level `struct` Function:** Adds a dedicated `nw.struct` entry point to simplify the creation and manipulation of structured data columns across backends.
- **Documentation Migration:** The project successfully migrated its documentation to Zensical, improving overall readability and maintenance.

#### Breaking Changes
None. This release focuses on additive features and internal improvements without breaking existing APIs.

#### Priority
Minor