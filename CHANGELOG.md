# CHANGELOG



## v1.0.20 (2023-08-10)

### Fix

* fix: add a manual publish workflow

Manual publish workflow to allow publishing in case of GH token failure ([`9833082`](https://github.com/Definedge-Securities/pyintegrate/commit/9833082fcd6e03f2f56a52f6dfd834dd7d0aec40))


## v1.0.19 (2023-08-10)

### Fix

* fix: modified ws.py

Uncommented close_on_exception line for demonstration in a example ([`4809b19`](https://github.com/Definedge-Securities/pyintegrate/commit/4809b19ceabce176c8592b1a15cdef8c1a4ee420))

### Unknown

* Update issue templates

Added bug report and feature report issue templates ([`2bfa7ee`](https://github.com/Definedge-Securities/pyintegrate/commit/2bfa7eecae567b6635a37a50d007ae417d94bfd4))


## v1.0.18 (2023-08-09)

### Ci

* ci: checking precommit run ([`8f98dec`](https://github.com/Definedge-Securities/pyintegrate/commit/8f98dec0143ad25b90fc0e73055fe06f9a08d6f8))

* ci: retesting with cache ([`5cede8e`](https://github.com/Definedge-Securities/pyintegrate/commit/5cede8e2dbf6a0737c557fe224be6ffa279e1b7d))

### Fix

* fix: revert pyproject.toml and separate CIs

Revert pysemrel build command, separate CI files for release &amp; pr check ([`9fd19ef`](https://github.com/Definedge-Securities/pyintegrate/commit/9fd19ef6d1d649b26241799ab3644ae7f62d2148))


## v1.0.17 (2023-08-09)

### Chore

* chore: modified PATH env ([`4b72339`](https://github.com/Definedge-Securities/pyintegrate/commit/4b723396ac930905363466d6fa5d846542e5092d))

* chore: removed macos ([`f60195e`](https://github.com/Definedge-Securities/pyintegrate/commit/f60195e72691930cc7d51c5cd1afba1e260e4916))

* chore: testing caching in GH Actions ([`74ae5ea`](https://github.com/Definedge-Securities/pyintegrate/commit/74ae5ea25e0e591a4ae4fa0d12506a343bb9ae88))

### Ci

* ci: checking with master branch

removed python install, reverted poetry install in pyproject.toml ([`cb8a701`](https://github.com/Definedge-Securities/pyintegrate/commit/cb8a7011219f512ebe3d033431f1d56041294e25))

* ci: reverting from master to 8.0.4 ([`875f078`](https://github.com/Definedge-Securities/pyintegrate/commit/875f07851d7d4575408da553178af6c4ac68f62b))

* ci: set PATH explicitly for pysemrel ([`09833c4`](https://github.com/Definedge-Securities/pyintegrate/commit/09833c48bb26a8fcc9cc21fdbbf8078a8c2ea114))

* ci: test without poetry binary cache ([`6adc528`](https://github.com/Definedge-Securities/pyintegrate/commit/6adc528f280ece2d4cefcec6f020944c2c6234e8))

* ci: testing poetry and dependencies caching ([`90c9e30`](https://github.com/Definedge-Securities/pyintegrate/commit/90c9e3006ed755b0f93681a79962b493d06d589e))

### Fix

* fix: removed GITHUB_API_URL from env

Removed env variable as can&#39;t change the above value ([`3832296`](https://github.com/Definedge-Securities/pyintegrate/commit/3832296d4c8aa08e530bfe0aaf3d6b8c3f178783))


## v1.0.16 (2023-08-09)

### Chore

* chore: testing cache and GH release ([`63b80fd`](https://github.com/Definedge-Securities/pyintegrate/commit/63b80fd7cb04b01926ee3766a02f611113ed5f37))

### Fix

* fix: reverted poetry cache actions ([`2523de1`](https://github.com/Definedge-Securities/pyintegrate/commit/2523de17234e1bfcba076efc566a40feb3c9c29f))


## v1.0.15 (2023-08-09)

### Fix

* fix: update readme and ws.py

Fix stop method to close the connection cleanly and stop reactor ([`63ff3d1`](https://github.com/Definedge-Securities/pyintegrate/commit/63ff3d1c21e6b3933abfad38f16d956983cfc12a))


## v1.0.14 (2023-08-09)

### Fix

* fix: update README

Fixed line 154 - Warning - Title underline too short. ([`6f522ca`](https://github.com/Definedge-Securities/pyintegrate/commit/6f522ca83f723851d8fc98720d3d91873d64c506))


## v1.0.13 (2023-08-09)

### Fix

* fix: update docs and examples

1. Moved contributing readme to CONTRIBUTING.md
2. Updated README with ws example
3. Added on_exception callback for Python exceptions ([`fddec7b`](https://github.com/Definedge-Securities/pyintegrate/commit/fddec7b408b03e156dedeb484ef206bb07b85ac1))


## v1.0.12 (2023-08-09)

### Fix

* fix: update ws.py

Changed code 1001 to 1000 during close ([`6f37e17`](https://github.com/Definedge-Securities/pyintegrate/commit/6f37e17faf498ff27542ee22caf6aff1a0f2db62))


## v1.0.11 (2023-08-09)

### Fix

* fix: update ws.py

Update code to 1001 to close connection ([`8d27866`](https://github.com/Definedge-Securities/pyintegrate/commit/8d27866b1f28dcb8afad37f7efc791f95d8d183a))


## v1.0.10 (2023-08-09)

### Fix

* fix: update ws.py

Close websocket connection in case token is invalid ([`3d3822a`](https://github.com/Definedge-Securities/pyintegrate/commit/3d3822a541fc40b3c16d228d68d2a674cb286a18))


## v1.0.9 (2023-08-09)

### Fix

* fix: modified ws.py

Renamed variable token to t to resolve conflict ([`5014836`](https://github.com/Definedge-Securities/pyintegrate/commit/50148363f3bfc50d461e42a1a1ad471ad2ca6096))


## v1.0.8 (2023-08-09)

### Fix

* fix: update README and ws

1. Remove typing.Union in websocket example in README
2. Added a method to check token validity in ws.py ([`d1c1a2b`](https://github.com/Definedge-Securities/pyintegrate/commit/d1c1a2b6fbf2cc981f4ea0676da2524921e1ff61))


## v1.0.7 (2023-08-09)

### Fix

* fix: update ws.py with order callback in README ([`72088f1`](https://github.com/Definedge-Securities/pyintegrate/commit/72088f159fab7ef2ed9031530d8f7b2a1a814f1d))


## v1.0.6 (2023-08-08)

### Fix

* fix: test ci.yml ([`a643fc0`](https://github.com/Definedge-Securities/pyintegrate/commit/a643fc0c0743f6ae8fa416ace0405fb3166a8ec0))


## v1.0.5 (2023-08-08)

### Fix

* fix: fix FileNotFoundError for allmaster.csv ([`41340b4`](https://github.com/Definedge-Securities/pyintegrate/commit/41340b4b6ed6a86ed908683655aaacd2bd643f99))

* fix: update CONTRIBUTING.md ([`0f22dda`](https://github.com/Definedge-Securities/pyintegrate/commit/0f22dda30ff196d46c695e8c99d407bddf37f153))

* fix: update CONTRIBUTING.md ([`345b5db`](https://github.com/Definedge-Securities/pyintegrate/commit/345b5dbe49e29c3fbc53f511604c5f1131c78652))

### Unknown

* Merge branch &#39;main&#39; of https://github.com/Definedge-Securities/pyintegrate ([`6b50e06`](https://github.com/Definedge-Securities/pyintegrate/commit/6b50e06025863feebed308e956963dad1e671e02))


## v1.0.4 (2023-08-08)

### Fix

* fix: README and constants ([`db1a4e2`](https://github.com/Definedge-Securities/pyintegrate/commit/db1a4e2abd2eb06e239ae102de94155257fc69b0))

### Unknown

* Merge branch &#39;main&#39; of https://github.com/Definedge-Securities/pyintegrate ([`b98d797`](https://github.com/Definedge-Securities/pyintegrate/commit/b98d797eb30de7d1754cdba98b72f7e110fab29c))


## v1.0.3 (2023-08-08)

### Chore

* chore: fix docstrings, add margins example ([`e84aa3a`](https://github.com/Definedge-Securities/pyintegrate/commit/e84aa3accfe24b647870707a38c5591bfec3aef7))

### Fix

* fix: added examples link in readme and index ([`67e1cf2`](https://github.com/Definedge-Securities/pyintegrate/commit/67e1cf28f336fc45a848b7bb113eeeae2e148e51))

### Unknown

* Merge branch &#39;main&#39; of https://github.com/Definedge-Securities/pyintegrate ([`417dc37`](https://github.com/Definedge-Securities/pyintegrate/commit/417dc37092642ffb1215d83597a8b5b69c403295))


## v1.0.2 (2023-08-04)

### Fix

* fix: trailing comma ([`2ed5060`](https://github.com/Definedge-Securities/pyintegrate/commit/2ed50601cac64064bf7e8cacdcaa84ccca25326a))

* fix: classifiers ([`3e793d7`](https://github.com/Definedge-Securities/pyintegrate/commit/3e793d79c893827fd0c1ab4b3c7bbd61d0c0a5a8))


## v1.0.1 (2023-08-04)

### Fix

* fix: remove api token ([`1ed998d`](https://github.com/Definedge-Securities/pyintegrate/commit/1ed998d7b0472bf0aa407aca46190b70aa623a5e))

### Unknown

* Merge branch &#39;main&#39; of https://github.com/Definedge-Securities/pyintegrate ([`680099b`](https://github.com/Definedge-Securities/pyintegrate/commit/680099b4c1f72682552652c520402ec23e944a63))


## v1.0.0 (2023-08-04)

### Breaking

* docs: Updated README

Added comment with symbol names for tokens mentioned in the example

BREAKING CHANGE: Update to 1.0.0 ([`b52ccc4`](https://github.com/Definedge-Securities/pyintegrate/commit/b52ccc4d03f3604f0b13741e1ec67f4566919d5e))

### Ci

* ci: pypi-publish version change ([`01fc292`](https://github.com/Definedge-Securities/pyintegrate/commit/01fc292d40e7a821d678a3afda8e7312cf3c1af7))

### Unknown

* Merge branch &#39;main&#39; of https://github.com/Definedge-Securities/pyintegrate ([`e2ec921`](https://github.com/Definedge-Securities/pyintegrate/commit/e2ec9217bffcb010351f61110a48c173f5f98fbc))


## v0.0.1 (2023-08-04)

### Ci

* ci: fixed sem rel to 8.0.4 ([`c18d9a9`](https://github.com/Definedge-Securities/pyintegrate/commit/c18d9a9ac10c3c88883362c056cf91d424d9148f))

* ci: testing deployment with testpypi ([`441d92f`](https://github.com/Definedge-Securities/pyintegrate/commit/441d92fb484dbdb720c26f8af73b5292522ac9a8))

* ci: updated release section ([`cdbb753`](https://github.com/Definedge-Securities/pyintegrate/commit/cdbb753904168fff4cf595a87ab12202314d7b98))

* ci: change python-semantic-release to 7.33.5 ([`2e842ad`](https://github.com/Definedge-Securities/pyintegrate/commit/2e842adad00bbacec5dce629895cadbf0252cc21))

### Fix

* fix: conf py ([`e62ceb0`](https://github.com/Definedge-Securities/pyintegrate/commit/e62ceb0445bb4b506373f9d7c645ff128ee2b8df))

* fix: version variable ([`c7dbd21`](https://github.com/Definedge-Securities/pyintegrate/commit/c7dbd2111c7d09f111ff78e45166f1b72e9ac61b))

* fix: version_variable ([`cc88c41`](https://github.com/Definedge-Securities/pyintegrate/commit/cc88c4169023cbffcdbc89b6969f51e9b3564e89))

* fix: version_toml as list and readme ([`4c6afec`](https://github.com/Definedge-Securities/pyintegrate/commit/4c6afecb6386818fc1f572b03d9bee7b56385eb4))

* fix: changed from tuple to list ([`3c9450a`](https://github.com/Definedge-Securities/pyintegrate/commit/3c9450aab928bca1a4fd72630b34ee82d9ca0397))

* fix: version variable name ([`b0c9bc3`](https://github.com/Definedge-Securities/pyintegrate/commit/b0c9bc3dd6ad7c072625b22a8eedee34e6433002))

* fix: changed list to tuple in toml ([`795f925`](https://github.com/Definedge-Securities/pyintegrate/commit/795f925f587406c24498bacc185f7eb479782876))

* fix: websocket test, dep version up ([`4295642`](https://github.com/Definedge-Securities/pyintegrate/commit/42956429460f5b54a6afd235da6916a1b475e78c))

* fix: readme, python version in ci.yml, poetry ci ([`578728a`](https://github.com/Definedge-Securities/pyintegrate/commit/578728a524ce4279a03cd9b42dcb2f621bcce3a5))

### Unknown

* Initial commit ([`811e9a0`](https://github.com/Definedge-Securities/pyintegrate/commit/811e9a0a6b9869e9c1dafc8a2af4780f30920dd0))
