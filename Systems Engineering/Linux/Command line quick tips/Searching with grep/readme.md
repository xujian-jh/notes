# [Command line quick tips: Searching with grep]

## Introducing grep

- The grep utility allows you to search for text, or more specifically text patterns, on your file system.
- The name grep comes from global regular expression print.

## Regular expressions

- Harnessing all the power of regular expressions is a topic bigger than this article, for sure.
- The simplest kind of regex can be just a word, or a portion of a word.
  - That pattern is simply “the following characters, in the same order.”
    - pciutil – matches any time the 7 characters pciutil appear together — including pciutil, pciutils, pciutil123, and foopciutil.
  - The pattern is searched line by line.
    - ^pciutil – matches any time the 7 characters pciutil appear together immediately at the beginning of a line (that’s what the ^ stands for)
    - pciutil$ – matches any time the 7 characters pciutil appear together immediately before the end of a line (that’s what the $ stands for)
- Special characters are used in a regex as wildcards, or to change the way the regex works. If you want to match on one of these characters, use a `\` (backslash) before the character.
  - The `.` (period) is a wildcard that matches any single character. If you use it in the expression pci.til, it matches pciutil, pci4til, or pci!til, but does not match pcitil. There must be a character to match the . in the regular expression.
  - The `?` is a marker in a regex that marks the previous element as optional. So if you built on the previous example, the expression pci.?til would also match on pcitil because there need not be a character between i and t for a valid match.
  - The `+` and `*` are markers that stand for repetition. While `+` stands for one or more of the previous element, `*` stands for zero or more. So the regex pci.+til would match any of these: pciutil, pci4til, pci!til, pciuuuuuutil, pci423til. However, it wouldn’t match pcitil — but the regex pci.*til would.

## Examples of grep

```bash
sudo grep -r jpublic /etc/
```

- Imagine that you’re trying to find a configuration file that mentions a user account jpublic.
- Try searching the /etc folder (using sudo because some subfolders are not readable outside the root account)
- The `-r` switch searches the folder recursively.

```bash
sudo grep -irl 'ma\?cnulty' /home/shared
```

- Imagine you have a much larger selection of files in /home/shared and you need to establish which ones mention the name MacNulty (or McNulty).
- The `-i` to make the search case-insensitive
- The `-l` switch to only output filenames with a match
- The `a ?` marker for optional a in the name

---

[Command line quick tips: Searching with grep]:https://fedoramagazine.org/command-line-quick-tips-searching-with-grep/
