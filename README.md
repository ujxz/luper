<img src="img/logo.png" alt="luper logo" width="275px">

Luper - Discovery Enumerator
=========

![License](https://img.shields.io/badge/license-MIT-green.svg)
![Build](https://img.shields.io/badge/Built%20with-Python-Blue)
![Stars](https://img.shields.io/github/stars/ujxz/luper.svg)
[![Release](https://img.shields.io/github/release/ujxz/luper.svg)](https://github.com/ujxz/luper/releases)
[![Sponsors](https://img.shields.io/github/sponsors/maurosoria)](https://github.com/sponsors/ujxz)


> Discovery Enumerator - brute-forcer

Produced by @ujxz, inspired by **Dirsearch** by [@maurosoria](https://github.com/maurosoria)

*Send me a message on twitter: [@_ujxz](https://x.com/_ujxz)*

How to use
---------------
```
$ python tests/test_brute_forcer.py -u "URL" -w "WORDLIST"
```
### exemple
---------------
```
PS $ python .\tests\test_brute_forcer.py -u "https://google.com" -w .\wordlists\common.txt

==================================================
LUPER  v0.1.7
by Jabes Eduardo (@ujxz)
==================================================
[*] target ->>  https://google.com
[*] wordlist ->>  .\wordlists\common.txt
[*] wordlist size ->>  4614
===================================================
[#] https://google.com/
(170/4614) [\-------------------][#] https://google.com/2001
(171/4614) [\-------------------][#] https://google.com/2002
(172/4614) [\-------------------][#] https://google.com/2003
(173/4614) [\-------------------][#] https://google.com/2004
(174/4614) [\-------------------][#] https://google.com/2005
(175/4614) [\-------------------][#] https://google.com/2006
(176/4614) [\-------------------][#] https://google.com/2007
(177/4614) [\-------------------][#] https://google.com/2008
(178/4614) [\-------------------][#] https://google.com/2009
(179/4614) [\-------------------][#] https://google.com/2010
(180/4614) [\-------------------][#] https://google.com/2011
(181/4614) [\-------------------][#] https://google.com/2012
(182/4614) [\-------------------][#] https://google.com/2013
(183/4614) [\-------------------][#] https://google.com/2014
(222/4614) [\-------------------][#] https://google.com/about
(241/4614) [\-------------------][#] https://google.com/accessibility
(246/4614) [\-------------------][#] https://google.com/account
(251/4614) [\-------------------][#] https://google.com/accounts
```

Contribution
---------------
To become a contributor, fork this repository or make an issue, everyone is welcome to help with this project

See [CONTRIBUTORS.md](https://github.com/ujxz/luper/blob/master/CONTRIBUTORS.md) to see who the contributors are so far.

#### Pull requests, forks and feature requests are welcomed


License
---------------
Copyright (C) ujxz [gmail](jabfxcomercial@gmail.com)

License: MIT