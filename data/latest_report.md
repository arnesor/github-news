# GitHub New Releases Report 2026-02-22

**[marimo-team/marimo 0.20.0](https://github.com/marimo-team/marimo/releases/tag/0.20.0)**

# marimo 0.20.0 Release Notes

### Summary
marimo 0.20.0 introduces enhanced interactive widgets for scientific computing and deep learning, including reactive Matplotlib plots and editable matrices. It also refines the reactive execution engine with a more predictable `mo.stop` behavior to prevent common dependency-related errors.

### ⭐ Highlights
*   **Reactive Matplotlib Selections:** `mo.ui.matplotlib` now adds interactive box and lasso selection to scatter plots. Users can select data points directly on the plot and reactively use those selections in downstream cells.
*   **Editable Matrix & Vector Inputs:** The new `mo.ui.matrix` widget provides a reactive numeric grid for NumPy arrays or nested lists. It supports per-element bounds, symmetric constraints, and custom precision for interactive linear algebra workflows.
*   **Rich PyTorch Visualization:** PyTorch `nn.Module` instances now render as interactive, collapsible HTML trees. This includes color-coded layer categories, trainable parameter counts, and hover-enabled documentation lookups.

### 🚨 Breaking Changes
*   **`mo.stop` Dependency Logic:** To prevent `NameError` exceptions, marimo now waits for **all** of a cell’s dependencies to be unblocked before execution. Previously, a cell would trigger if only one of multiple stopped branches was unblocked, often leading to errors when variables from other branches were still undefined.

### ✨ Other Key Enhancements
*   Added Matplotlib SVG output support for crisper visuals.
*   Masked `getpass.getpass()` input in the notebook UI for better security.
*   New PDF export option to exclude code blocks.
*   Preview feature: Initial backend logic for a new Storage Inspector.