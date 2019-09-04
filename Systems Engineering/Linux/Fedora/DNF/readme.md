# DNF(Dandified YUM)

- DNF is the next generation of that package manager base-on YUM and [Hawkey].
  - DNF has been the default package manager for since the 22nd version of Fedora, Fedora 22.
  - Dandified Yum was introduced in Fedora 18.

## YUM(Yellowdog Updater, Modified)

- YUM is a package manager for RPM-based distributions.
- YUM has long been considered a poor performer.
  - It was notorious for high memory usage, and the slowness when resolving dependencies.
- DNF now uses libsolv, an external dependency resolver, and hawkey for resolving dependencies, while yum used its own, internal, dependency resolver.

### RPM(Red-Hat Package Manager)

## Hawkey，libsolv API Simplified

---

[Hawkey]:https://hawkey.readthedocs.io/en/latest/index.html#
