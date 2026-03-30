# GitHub New Releases Report 2026-03-30

**[numpy/numpy v2.4.4](https://github.com/numpy/numpy/releases/tag/v2.4.4)**

# NumPy v2.4.4 Release Analysis

### Summary
NumPy 2.4.4 is a focused patch release designed to resolve critical bugs and stability issues identified after the 2.4.3 version. This release primarily addresses a persistent OpenBLAS threading problem on ARM architectures and ensures seamless compatibility for Python versions 3.11 through 3.14.

### Highlights
- **ARM Threading Resolution:** Successfully resolves a long-standing OpenBLAS threading bug (issue #30816) specifically affecting ARM hardware, improving reliability for mobile and cloud-native deployments.
- **Python 3.14 Readiness:** Includes updated documentation regarding `ndarray.resize` caveats for Python 3.14+ and general maintenance to support the latest Python release cycle.
- **Internal Logic Fixes:** Corrects FNV-1a 64-bit selection logic and eliminates unnecessary warnings when using `ufunc` with `where=True` but no output.

### Breaking Changes
⚠️ **None.** This is a patch release focused on stability and bug fixes. It is a drop-in replacement for users currently on any 2.4.x version.

### Maintenance & Security
- **Memory Safety:** Replaced deprecated C-function `sprintf` with the safer `snprintf` in the `numpy.i` interface.
- **Architecture Support:** Fixed POWER VSX feature mapping to ensure correct SIMD optimizations on IBM Power architectures.
---
**[python-poetry/poetry 2.3.3](https://github.com/python-poetry/poetry/releases/tag/2.3.3)**
- Error generating summary: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}