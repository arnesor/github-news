# GitHub New Releases Report 2026-04-23

**[pola-rs/polars py-1.40.1](https://github.com/pola-rs/polars/releases/tag/py-1.40.1)**

Polars `py-1.40.1` is a patch release delivering critical bug fixes across list operations, sorting, and type stubs. Key improvements include a new parameter for sorted merges and performance optimizations for null-free NumPy interoperability.

### 🚀 Highlights
*   **`merge_sorted` Enhancement**: Added the `maintain_order` parameter to provide more control over result sequencing during sorted merges.
*   **Typing Stability**: Fixed `DataFrame` and `Series` initializers so they no longer require all optional dependencies to be installed to pass type-checking.
*   **Sampling Logic**: Corrected `list.sample()` to allow a `fraction > 1` when `with_replacement=True`, aligning it with expected statistical behavior.

### ⚠️ Breaking Changes
*   None.

### 🛠️ Key Bug Fixes
*   Fixed a bug in `reduce_balanced` affecting `pl.concat` for specific input lengths.
*   Ensured `append()` correctly errors when `upcast=False` if types do not match.
*   Fixed SQL `having` predicate honors in `GroupBy` iterators.
*   Optimized `__array_ufunc__` by skipping validity mask processing when no inputs contain nulls.