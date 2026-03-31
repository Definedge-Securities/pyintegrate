# CHANGELOG


## v3.0.0 (2026-03-31)

### Features

- Trigger release
  ([`9f904c2`](https://github.com/Definedge-Securities/pyintegrate/commit/9f904c216b9893960adcc29ec6ad548f70d557c3))

- Trigger release
  ([`9b88b8d`](https://github.com/Definedge-Securities/pyintegrate/commit/9b88b8d6a485eba6e7bec7f8ef32c1b9ec803da5))

- Trigger release
  ([`ef7f590`](https://github.com/Definedge-Securities/pyintegrate/commit/ef7f590261805b541f67dee265af223196be8b17))

- Trigger release ([#95](https://github.com/Definedge-Securities/pyintegrate/pull/95),
  [`fa6c2c3`](https://github.com/Definedge-Securities/pyintegrate/commit/fa6c2c3706bb391358b3341259159fc06a5a5dac))


## v2.0.0 (2026-03-31)

### Features

- Added Algo Id as mandatory parameter in place order, as per SEBI regulations
  ([`59627fe`](https://github.com/Definedge-Securities/pyintegrate/commit/59627fe40ac8fe8adc2cbea89dbd8088816a110a))

BREAKING CHANGE: Due to SEBI regulations, algo id is now mandatory for placeOrder api.

### Breaking Changes

- Due to SEBI regulations, algo id is now mandatory for placeOrder api.


## v1.2.0 (2025-08-11)

### Chores

- **deps**: Bump actions/checkout from 3 to 4
  ([`efd6b72`](https://github.com/Definedge-Securities/pyintegrate/commit/efd6b72d2f17c03ce2050b1042aafb90328055eb))

Bumps [actions/checkout](https://github.com/actions/checkout) from 3 to 4. - [Release
  notes](https://github.com/actions/checkout/releases) -
  [Changelog](https://github.com/actions/checkout/blob/main/CHANGELOG.md) -
  [Commits](https://github.com/actions/checkout/compare/v3...v4)

--- updated-dependencies: - dependency-name: actions/checkout dependency-type: direct:production

update-type: version-update:semver-major ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps-dev**: Bump mypy from 1.5.1 to 1.15.0
  ([`00bb525`](https://github.com/Definedge-Securities/pyintegrate/commit/00bb5254cd76c3480b57fedf097929f29aa9adf4))

Bumps [mypy](https://github.com/python/mypy) from 1.5.1 to 1.15.0. -
  [Changelog](https://github.com/python/mypy/blob/master/CHANGELOG.md) -
  [Commits](https://github.com/python/mypy/compare/v1.5.1...v1.15.0)

--- updated-dependencies: - dependency-name: mypy dependency-type: direct:development

update-type: version-update:semver-minor ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps-dev**: Bump mypy from 1.5.1 to 1.15.0
  ([#62](https://github.com/Definedge-Securities/pyintegrate/pull/62),
  [`876126e`](https://github.com/Definedge-Securities/pyintegrate/commit/876126e752cd8be4cdfec369d44b19f83e4d83e5))

Bumps [mypy](https://github.com/python/mypy) from 1.5.1 to 1.15.0. <details>
  <summary>Changelog</summary> <p><em>Sourced from <a
  href="https://github.com/python/mypy/blob/master/CHANGELOG.md">mypy's changelog</a>.</em></p>
  <blockquote> <h1>Mypy Release Notes</h1> <h2>Next Release</h2> <p>...</p> <h2>Mypy 1.15</h2>
  <p>We’ve just uploaded mypy 1.15 to the Python Package Index (<a
  href="https://pypi.org/project/mypy/">PyPI</a>). Mypy is a static type checker for Python. This
  release includes new features, performance improvements and bug fixes. You can install it as
  follows:</p> <pre><code>python3 -m pip install -U mypy </code></pre> <p>You can read the full
  documentation for this release on <a href="http://mypy.readthedocs.io">Read the Docs</a>.</p>
  <h3>Performance Improvements</h3> <p>Mypy is up to 40% faster in some use cases. This improvement
  comes largely from tuning the performance of the garbage collector. Additionally, the release
  includes several micro-optimizations that may be impactful for large projects.</p> <p>Contributed
  by Jukka Lehtosalo</p> <ul> <li>PR <a
  href="https://redirect.github.com/python/mypy/pull/18306">18306</a></li> <li>PR <a
  href="https://redirect.github.com/python/mypy/pull/18302">18302</a></li> <li>PR <a
  href="https://redirect.github.com/python/mypy/pull/18298">18298</a></li> <li>PR <a
  href="https://redirect.github.com/python/mypy/pull/18299">18299</a></li> </ul> <h3>Mypyc
  Accelerated Mypy Wheels for ARM Linux</h3> <p>For best performance, mypy can be compiled to C
  extension modules using mypyc. This makes mypy 3-5x faster than when interpreted with pure Python.
  We now build and upload mypyc accelerated mypy wheels for <code>manylinux_aarch64</code> to PyPI,
  making it easy for Linux users on ARM platforms to realise this speedup -- just <code>pip
  install</code> the latest mypy.</p> <p>Contributed by Christian Bundy and Marc Mueller (PR <a
  href="https://redirect.github.com/mypyc/mypy_mypyc-wheels/pull/76">mypy_mypyc-wheels#76</a>, PR <a
  href="https://redirect.github.com/mypyc/mypy_mypyc-wheels/pull/89">mypy_mypyc-wheels#89</a>).</p>
  <h3><code>--strict-bytes</code></h3> <p>By default, mypy treats <code>bytearray</code> and
  <code>memoryview</code> values as assignable to the <code>bytes</code> type, for historical
  reasons. Use the <code>--strict-bytes</code> flag to disable this behavior. <a
  href="https://peps.python.org/pep-0688">PEP 688</a> specified the removal of this special case.
  The flag will be enabled by default in <strong>mypy 2.0</strong>.</p> <p>Contributed by Ali Hamdan
  (PR <a href="https://redirect.github.com/python/mypy/pull/18263">18263</a>) and Shantanu Jain (PR
  <a href="https://redirect.github.com/python/mypy/pull/13952">13952</a>).</p> <h3>Improvements to
  Reachability Analysis and Partial Type Handling in Loops</h3> <!-- raw HTML omitted -->
  </blockquote> <p>... (truncated)</p> </details> <details> <summary>Commits</summary> <ul> <li><a
  href="https://github.com/python/mypy/commit/9397454fb5aead107461b089e7cf190bf538d20a"><code>9397454</code></a>
  remove +dev from version ahead of final release</li> <li><a
  href="https://github.com/python/mypy/commit/686b591a69db216f714ad50698db785f4ac63eb0"><code>686b591</code></a>
  remove &quot;unreleased&quot; from 1.15 changelog entry</li> <li><a
  href="https://github.com/python/mypy/commit/cb4b243a5d9e03173e3e7275e5b92b98afaefb60"><code>cb4b243</code></a>
  Various small updates to 1.15 changelog (<a
  href="https://redirect.github.com/python/mypy/issues/18599">#18599</a>)</li> <li><a
  href="https://github.com/python/mypy/commit/1a265024f901399c701a772e8c1f9e6e110f45e6"><code>1a26502</code></a>
  Prepare changelog for 1.15 release (<a
  href="https://redirect.github.com/python/mypy/issues/18583">#18583</a>)</li> <li><a
  href="https://github.com/python/mypy/commit/d4515e4ad3eee6318744c64cf2eab0ea0b5b7562"><code>d4515e4</code></a>
  Fix a few PR links in the changelog (<a
  href="https://redirect.github.com/python/mypy/issues/18586">#18586</a>)</li> <li><a
  href="https://github.com/python/mypy/commit/f83b6435b0c07a327f6b567dfb5e79ffa36708a2"><code>f83b643</code></a>
  Add object self-type to tuple test fixture (<a
  href="https://redirect.github.com/python/mypy/issues/18592">#18592</a>)</li> <li><a
  href="https://github.com/python/mypy/commit/ebc2cb8befbadfc10b962af018b3fa3842d3fd87"><code>ebc2cb8</code></a>
  Prevent crash on generic NamedTuple with unresolved typevar bound (<a
  href="https://redirect.github.com/python/mypy/issues/18585">#18585</a>)</li> <li><a
  href="https://github.com/python/mypy/commit/63c251e249e52256629dbe8b8334937a092f792d"><code>63c251e</code></a>
  empty commit to trigger wheel rebuild</li> <li><a
  href="https://github.com/python/mypy/commit/c30573e7b95eef9d057ff42ebfd326438dac3c42"><code>c30573e</code></a>
  Fix literal context for ternary expressions (for real) (<a
  href="https://redirect.github.com/python/mypy/issues/18545">#18545</a>)</li> <li><a
  href="https://github.com/python/mypy/commit/23d862dd6fbb905a69bcb31e88746dc7a1eb4a43"><code>23d862d</code></a>
  Fix isinstance with explicit (non generic) type alias (<a
  href="https://redirect.github.com/python/mypy/issues/18512">#18512</a>)</li> <li>Additional
  commits viewable in <a href="https://github.com/python/mypy/compare/v1.5.1...v1.15.0">compare
  view</a></li> </ul> </details> <br />

[![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=mypy&package-manager=pip&previous-version=1.5.1&new-version=1.15.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don't alter it yourself. You can
  also trigger a rebase manually by commenting `@dependabot rebase`.

[//]: # (dependabot-automerge-start) [//]: # (dependabot-automerge-end)

---

<details> <summary>Dependabot commands and options</summary> <br />

You can trigger Dependabot actions by commenting on this PR: - `@dependabot rebase` will rebase this
  PR - `@dependabot recreate` will recreate this PR, overwriting any edits that have been made to it
  - `@dependabot merge` will merge this PR after your CI passes on it - `@dependabot squash and
  merge` will squash and merge this PR after your CI passes on it - `@dependabot cancel merge` will
  cancel a previously requested merge and block automerging - `@dependabot reopen` will reopen this
  PR if it is closed - `@dependabot close` will close this PR and stop Dependabot recreating it. You
  can achieve the same result by closing it manually - `@dependabot show <dependency name> ignore
  conditions` will show all of the ignore conditions of the specified dependency - `@dependabot
  ignore this major version` will close this PR and stop Dependabot creating any more for this major
  version (unless you reopen the PR or upgrade to it yourself) - `@dependabot ignore this minor
  version` will close this PR and stop Dependabot creating any more for this minor version (unless
  you reopen the PR or upgrade to it yourself) - `@dependabot ignore this dependency` will close
  this PR and stop Dependabot creating any more for this dependency (unless you reopen the PR or
  upgrade to it yourself)

</details>

- **deps-dev**: Bump python-semantic-release from 8.0.7 to 9.21.0
  ([`d6849f2`](https://github.com/Definedge-Securities/pyintegrate/commit/d6849f2fc15e35210dc7f791223de25b27a70cf9))

Bumps [python-semantic-release](https://github.com/python-semantic-release/python-semantic-release)
  from 8.0.7 to 9.21.0. - [Release
  notes](https://github.com/python-semantic-release/python-semantic-release/releases) -
  [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.rst)
  -
  [Commits](https://github.com/python-semantic-release/python-semantic-release/compare/v8.0.7...v9.21)

--- updated-dependencies: - dependency-name: python-semantic-release dependency-type:
  direct:development

update-type: version-update:semver-major ...

Signed-off-by: dependabot[bot] <support@github.com>

### Features

- Strike price correction in derivatives master for Symbol Generator.
  ([`c1ddaf3`](https://github.com/Definedge-Securities/pyintegrate/commit/c1ddaf39be1cd6afe6930f46bc79d802333958d4))

- Strike price correction in derivatives master for Symbol Generator.
  ([`6b464e7`](https://github.com/Definedge-Securities/pyintegrate/commit/6b464e7796cbeda72ffe192fdeb1a2fb45e72a14))

Bumps [actions/checkout](https://github.com/actions/checkout) from 3 to 4. <details>
  <summary>Release notes</summary> <p><em>Sourced from <a
  href="https://github.com/actions/checkout/releases">actions/checkout's releases</a>.</em></p>
  <blockquote> <h2>v4.0.0</h2> <h2>What's Changed</h2> <ul> <li>Update default runtime to node20 by
  <a href="https://github.com/takost"><code>@​takost</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/1436">actions/checkout#1436</a></li>
  <li>Support fetching without the --progress option by <a
  href="https://github.com/simonbaird"><code>@​simonbaird</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/1067">actions/checkout#1067</a></li>
  <li>Release 4.0.0 by <a href="https://github.com/takost"><code>@​takost</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/1447">actions/checkout#1447</a></li> </ul>
  <h2>New Contributors</h2> <ul> <li><a href="https://github.com/takost"><code>@​takost</code></a>
  made their first contribution in <a
  href="https://redirect.github.com/actions/checkout/pull/1436">actions/checkout#1436</a></li>
  <li><a href="https://github.com/simonbaird"><code>@​simonbaird</code></a> made their first
  contribution in <a
  href="https://redirect.github.com/actions/checkout/pull/1067">actions/checkout#1067</a></li> </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/actions/checkout/compare/v3...v4.0.0">https://github.com/actions/checkout/compare/v3...v4.0.0</a></p>
  <h2>v3.6.0</h2> <h2>What's Changed</h2> <ul> <li>Mark test scripts with Bash'isms to be run via
  Bash by <a href="https://github.com/dscho"><code>@​dscho</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/1377">actions/checkout#1377</a></li>
  <li>Add option to fetch tags even if fetch-depth &gt; 0 by <a
  href="https://github.com/RobertWieczoreck"><code>@​RobertWieczoreck</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/579">actions/checkout#579</a></li>
  <li>Release 3.6.0 by <a href="https://github.com/luketomlinson"><code>@​luketomlinson</code></a>
  in <a href="https://redirect.github.com/actions/checkout/pull/1437">actions/checkout#1437</a></li>
  </ul> <h2>New Contributors</h2> <ul> <li><a
  href="https://github.com/RobertWieczoreck"><code>@​RobertWieczoreck</code></a> made their first
  contribution in <a
  href="https://redirect.github.com/actions/checkout/pull/579">actions/checkout#579</a></li> <li><a
  href="https://github.com/luketomlinson"><code>@​luketomlinson</code></a> made their first
  contribution in <a
  href="https://redirect.github.com/actions/checkout/pull/1437">actions/checkout#1437</a></li> </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/actions/checkout/compare/v3.5.3...v3.6.0">https://github.com/actions/checkout/compare/v3.5.3...v3.6.0</a></p>
  <h2>v3.5.3</h2> <h2>What's Changed</h2> <ul> <li>Fix: Checkout Issue in self hosted runner due to
  faulty submodule check-ins by <a
  href="https://github.com/megamanics"><code>@​megamanics</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/1196">actions/checkout#1196</a></li>
  <li>Fix typos found by codespell by <a
  href="https://github.com/DimitriPapadopoulos"><code>@​DimitriPapadopoulos</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/1287">actions/checkout#1287</a></li>
  <li>Add support for sparse checkouts by <a
  href="https://github.com/dscho"><code>@​dscho</code></a> and <a
  href="https://github.com/dfdez"><code>@​dfdez</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/1369">actions/checkout#1369</a></li>
  <li>Release v3.5.3 by <a href="https://github.com/TingluoHuang"><code>@​TingluoHuang</code></a> in
  <a href="https://redirect.github.com/actions/checkout/pull/1376">actions/checkout#1376</a></li>
  </ul> <h2>New Contributors</h2> <ul> <li><a
  href="https://github.com/megamanics"><code>@​megamanics</code></a> made their first contribution
  in <a href="https://redirect.github.com/actions/checkout/pull/1196">actions/checkout#1196</a></li>
  <li><a href="https://github.com/DimitriPapadopoulos"><code>@​DimitriPapadopoulos</code></a> made
  their first contribution in <a
  href="https://redirect.github.com/actions/checkout/pull/1287">actions/checkout#1287</a></li>
  <li><a href="https://github.com/dfdez"><code>@​dfdez</code></a> made their first contribution in
  <a href="https://redirect.github.com/actions/checkout/pull/1369">actions/checkout#1369</a></li>
  </ul> <p><strong>Full Changelog</strong>: <a
  href="https://github.com/actions/checkout/compare/v3...v3.5.3">https://github.com/actions/checkout/compare/v3...v3.5.3</a></p>
  <h2>v3.5.2</h2> <h2>What's Changed</h2> <ul> <li>Fix: Use correct API url / endpoint in GHES by <a
  href="https://github.com/fhammerl"><code>@​fhammerl</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/1289">actions/checkout#1289</a> based on
  <a href="https://redirect.github.com/actions/checkout/issues/1286">#1286</a> by <a
  href="https://github.com/1newsr"><code>@​1newsr</code></a></li> </ul> <p><strong>Full
  Changelog</strong>: <a
  href="https://github.com/actions/checkout/compare/v3.5.1...v3.5.2">https://github.com/actions/checkout/compare/v3.5.1...v3.5.2</a></p>
  <h2>v3.5.1</h2> <h2>What's Changed</h2> <ul> <li>Improve checkout performance on Windows runners
  by upgrading <code>@​actions/github</code> dependency by <a
  href="https://github.com/BrettDong"><code>@​BrettDong</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/1246">actions/checkout#1246</a></li> </ul>
  <h2>New Contributors</h2> <ul> <li><a
  href="https://github.com/BrettDong"><code>@​BrettDong</code></a> made their first contribution in
  <a href="https://redirect.github.com/actions/checkout/pull/1246">actions/checkout#1246</a></li>
  </ul> <!-- raw HTML omitted --> </blockquote> <p>... (truncated)</p> </details> <details>
  <summary>Changelog</summary> <p><em>Sourced from <a
  href="https://github.com/actions/checkout/blob/main/CHANGELOG.md">actions/checkout's
  changelog</a>.</em></p> <blockquote> <h1>Changelog</h1> <h2>v4.0.0</h2> <ul> <li><a
  href="https://redirect.github.com/actions/checkout/pull/1067">Support fetching without the
  --progress option</a></li> <li><a
  href="https://redirect.github.com/actions/checkout/pull/1436">Update to node20</a></li> </ul>
  <h2>v3.6.0</h2> <ul> <li><a href="https://redirect.github.com/actions/checkout/pull/1377">Fix:
  Mark test scripts with Bash'isms to be run via Bash</a></li> <li><a
  href="https://redirect.github.com/actions/checkout/pull/579">Add option to fetch tags even if
  fetch-depth &gt; 0</a></li> </ul> <h2>v3.5.3</h2> <ul> <li><a
  href="https://redirect.github.com/actions/checkout/pull/1196">Fix: Checkout fail in self-hosted
  runners when faulty submodule are checked-in</a></li> <li><a
  href="https://redirect.github.com/actions/checkout/pull/1287">Fix typos found by
  codespell</a></li> <li><a href="https://redirect.github.com/actions/checkout/pull/1369">Add
  support for sparse checkouts</a></li> </ul> <h2>v3.5.2</h2> <ul> <li><a
  href="https://redirect.github.com/actions/checkout/pull/1289">Fix api endpoint for GHES</a></li>
  </ul> <h2>v3.5.1</h2> <ul> <li><a
  href="https://redirect.github.com/actions/checkout/pull/1246">Fix slow checkout on
  Windows</a></li> </ul> <h2>v3.5.0</h2> <ul> <li><a
  href="https://redirect.github.com/actions/checkout/pull/1237">Add new public key for
  known_hosts</a></li> </ul> <h2>v3.4.0</h2> <ul> <li><a
  href="https://redirect.github.com/actions/checkout/pull/1209">Upgrade codeql actions to
  v2</a></li> <li><a href="https://redirect.github.com/actions/checkout/pull/1210">Upgrade
  dependencies</a></li> <li><a href="https://redirect.github.com/actions/checkout/pull/1225">Upgrade
  <code>@​actions/io</code></a></li> </ul> <h2>v3.3.0</h2> <ul> <li><a
  href="https://redirect.github.com/actions/checkout/pull/1045">Implement branch list using
  callbacks from exec function</a></li> <li><a
  href="https://redirect.github.com/actions/checkout/pull/1050">Add in explicit reference to private
  checkout options</a></li> <li>[Fix comment typos (that got added in <a
  href="https://redirect.github.com/actions/checkout/issues/770">#770</a>)](<a
  href="https://redirect.github.com/actions/checkout/pull/1057">actions/checkout#1057</a>)</li>
  </ul> <h2>v3.2.0</h2> <ul> <li><a href="https://redirect.github.com/actions/checkout/pull/942">Add
  GitHub Action to perform release</a></li> <li><a
  href="https://redirect.github.com/actions/checkout/pull/967">Fix status badge</a></li> <li><a
  href="https://redirect.github.com/actions/checkout/pull/1002">Replace datadog/squid with
  ubuntu/squid Docker image</a></li> <li><a
  href="https://redirect.github.com/actions/checkout/pull/964">Wrap pipeline commands for
  submoduleForeach in quotes</a></li> <li><a
  href="https://redirect.github.com/actions/checkout/pull/1029">Update <code>@​actions/io</code> to
  1.1.2</a></li> <li><a href="https://redirect.github.com/actions/checkout/pull/1039">Upgrading
  version to 3.2.0</a></li> </ul> <h2>v3.1.0</h2> <ul> <li><a
  href="https://redirect.github.com/actions/checkout/pull/939">Use <code>@​actions/core</code>
  <code>saveState</code> and <code>getState</code></a></li> <li><a
  href="https://redirect.github.com/actions/checkout/pull/922">Add <code>github-server-url</code>
  input</a></li> </ul> <h2>v3.0.2</h2> <ul> <li><a
  href="https://redirect.github.com/actions/checkout/pull/770">Add input
  <code>set-safe-directory</code></a></li> </ul> <h2>v3.0.1</h2> <!-- raw HTML omitted -->
  </blockquote> <p>... (truncated)</p> </details> <details> <summary>Commits</summary> <ul> <li><a
  href="https://github.com/actions/checkout/commit/3df4ab11eba7bda6032a0b82a6bb43b11571feac"><code>3df4ab1</code></a>
  Release 4.0.0 (<a href="https://redirect.github.com/actions/checkout/issues/1447">#1447</a>)</li>
  <li><a
  href="https://github.com/actions/checkout/commit/8b5e8b768746b50394015010d25e690bfab9dfbc"><code>8b5e8b7</code></a>
  Support fetching without the --progress option (<a
  href="https://redirect.github.com/actions/checkout/issues/1067">#1067</a>)</li> <li><a
  href="https://github.com/actions/checkout/commit/97a652b80035363df47baee5031ec8670b8878ac"><code>97a652b</code></a>
  Update default runtime to node20 (<a
  href="https://redirect.github.com/actions/checkout/issues/1436">#1436</a>)</li> <li>See full diff
  in <a href="https://github.com/actions/checkout/compare/v3...v4">compare view</a></li> </ul>
  </details> <br />

[![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=actions/checkout&package-manager=github_actions&previous-version=3&new-version=4)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

You can trigger a rebase of this PR by commenting `@dependabot rebase`.

[//]: # (dependabot-automerge-start) [//]: # (dependabot-automerge-end)

---

<details> <summary>Dependabot commands and options</summary> <br />

You can trigger Dependabot actions by commenting on this PR: - `@dependabot rebase` will rebase this
  PR - `@dependabot recreate` will recreate this PR, overwriting any edits that have been made to it
  - `@dependabot merge` will merge this PR after your CI passes on it - `@dependabot squash and
  merge` will squash and merge this PR after your CI passes on it - `@dependabot cancel merge` will
  cancel a previously requested merge and block automerging - `@dependabot reopen` will reopen this
  PR if it is closed - `@dependabot close` will close this PR and stop Dependabot recreating it. You
  can achieve the same result by closing it manually - `@dependabot show <dependency name> ignore
  conditions` will show all of the ignore conditions of the specified dependency - `@dependabot
  ignore this major version` will close this PR and stop Dependabot creating any more for this major
  version (unless you reopen the PR or upgrade to it yourself) - `@dependabot ignore this minor
  version` will close this PR and stop Dependabot creating any more for this minor version (unless
  you reopen the PR or upgrade to it yourself) - `@dependabot ignore this dependency` will close
  this PR and stop Dependabot creating any more for this dependency (unless you reopen the PR or
  upgrade to it yourself)

</details>

> **Note** > Automatic rebases have been disabled on this pull request as it has been open for over
  30 days.

- Strike price correction in derivatives master for Symbol Generator.
  ([`4581a0c`](https://github.com/Definedge-Securities/pyintegrate/commit/4581a0c144d7beb3c18cb8c92b9b45a2a637b73d))

Bumps [python-semantic-release](https://github.com/python-semantic-release/python-semantic-release)
  from 8.0.7 to 9.21.0. <details> <summary>Release notes</summary> <p><em>Sourced from <a
  href="https://github.com/python-semantic-release/python-semantic-release/releases">python-semantic-release's
  releases</a>.</em></p> <blockquote> <h2>v9.21.0 (2025-02-23)</h2> <p><em>This release is published
  under the MIT License.</em></p> <h3>✨ Features</h3> <ul> <li>Add package name variant,
  <code>python-semantic-release</code>, project script (<a
  href="https://redirect.github.com/python-semantic-release/python-semantic-release/pull/1199">PR#1199</a>,
  <a
  href="https://github.com/python-semantic-release/python-semantic-release/commit/1ac97bc74c69ce61cec98242c19bf8adc1d37fb9"><code>1ac97bc</code></a>)</li>
  </ul> <h3>📖 Documentation</h3> <ul> <li><strong>github-actions</strong>: Update example workflow
  to handle rapid merges (<a
  href="https://redirect.github.com/python-semantic-release/python-semantic-release/pull/1200">PR#1200</a>,
  <a
  href="https://github.com/python-semantic-release/python-semantic-release/commit/1a4116af4b999144998cf94cf84c9c23ff2e352f"><code>1a4116a</code></a>)</li>
  </ul> <h3>✅ Resolved Issues</h3> <ul> <li><a
  href="https://redirect.github.com/python-semantic-release/python-semantic-release/issues/1195">#1195</a>:
  <em>Native <code>uvx</code> support</em></li> </ul> <hr /> <p><strong>Detailed Changes</strong>:
  <a
  href="https://github.com/python-semantic-release/python-semantic-release/compare/v9.20.0...v9.21.0">v9.20.0...v9.21.0</a></p>
  <hr /> <p><strong>Installable artifacts are available from</strong>:</p> <ul> <li> <p><a
  href="https://pypi.org/project/python-semantic-release/9.21.0">PyPi Registry</a></p> </li> <li>
  <p><a
  href="https://github.com/python-semantic-release/python-semantic-release/releases/tag/v9.21.0">GitHub
  Release Assets</a></p> </li> </ul> <h2>v9.20.0 (2025-02-17)</h2> <p><em>This release is published
  under the MIT License.</em></p> <h3>✨ Features</h3> <ul> <li> <p><strong>cmd-version</strong>:
  Enable stamping of tag formatted versions into files (<a
  href="https://redirect.github.com/python-semantic-release/python-semantic-release/pull/1190">PR#1190</a>,
  <a
  href="https://github.com/python-semantic-release/python-semantic-release/commit/8906d8e70467af1489d797ec8cb09b1f95e5d409"><code>8906d8e</code></a>)</p>
  </li> <li> <p><strong>cmd-version</strong>: Extend <code>version_variables</code> to stamp
  versions with <code>@</code> symbol separator (<a
  href="https://redirect.github.com/python-semantic-release/python-semantic-release/pull/1185">PR#1185</a>,
  <a
  href="https://github.com/python-semantic-release/python-semantic-release/commit/23f69b6ac206d111b1e566367f9b2f033df5c87a"><code>23f69b6</code></a>)</p>
  </li> </ul> <h3>📖 Documentation</h3> <ul> <li> <p><strong>configuration</strong>: Add usage
  information for tag format version stamping (<a
  href="https://redirect.github.com/python-semantic-release/python-semantic-release/pull/1190">PR#1190</a>,
  <a
  href="https://github.com/python-semantic-release/python-semantic-release/commit/8906d8e70467af1489d797ec8cb09b1f95e5d409"><code>8906d8e</code></a>)</p>
  </li> <li> <p><strong>configuration</strong>: Clarify <code>version_variables</code> config
  description &amp; <code>@</code> separator usage (<a
  href="https://redirect.github.com/python-semantic-release/python-semantic-release/pull/1185">PR#1185</a>,
  <a
  href="https://github.com/python-semantic-release/python-semantic-release/commit/23f69b6ac206d111b1e566367f9b2f033df5c87a"><code>23f69b6</code></a>)</p>
  </li> </ul> <h3>⚙️ Build System</h3> <ul> <li><strong>deps</strong>: Add
  <code>deprecated~=1.2</code> for deprecation notices &amp; sphinx documentation (<a
  href="https://redirect.github.com/python-semantic-release/python-semantic-release/pull/1190">PR#1190</a>,
  <a
  href="https://github.com/python-semantic-release/python-semantic-release/commit/8906d8e70467af1489d797ec8cb09b1f95e5d409"><code>8906d8e</code></a>)</li>
  </ul> <h3>✅ Resolved Issues</h3> <!-- raw HTML omitted --> </blockquote> <p>... (truncated)</p>
  </details> <details> <summary>Changelog</summary> <p><em>Sourced from <a
  href="https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.rst">python-semantic-release's
  changelog</a>.</em></p> <blockquote> <h1>v9.21.0 (2025-02-23)</h1> <h2>✨ Features</h2> <ul>
  <li>Add package name variant, <code>python-semantic-release</code>, project script, closes
  <code>[#1195](https://github.com/python-semantic-release/python-semantic-release/issues/1195)</code>_
  (<code>PR#1199</code><em>, <code>1ac97bc</code></em>)</li> </ul> <h2>📖 Documentation</h2> <ul>
  <li><strong>github-actions</strong>: Update example workflow to handle rapid merges
  (<code>PR#1200</code><em>, <code>1a4116a</code></em>)</li> </ul> <p>.. _<a
  href="https://redirect.github.com/python-semantic-release/python-semantic-release/issues/1195">#1195</a>:
  <a
  href="https://redirect.github.com/python-semantic-release/python-semantic-release/issues/1195">python-semantic-release/python-semantic-release#1195</a>
  .. _1a4116a: <a
  href="https://github.com/python-semantic-release/python-semantic-release/commit/1a4116af4b999144998cf94cf84c9c23ff2e352f">https://github.com/python-semantic-release/python-semantic-release/commit/1a4116af4b999144998cf94cf84c9c23ff2e352f</a>
  .. _1ac97bc: <a
  href="https://github.com/python-semantic-release/python-semantic-release/commit/1ac97bc74c69ce61cec98242c19bf8adc1d37fb9">https://github.com/python-semantic-release/python-semantic-release/commit/1ac97bc74c69ce61cec98242c19bf8adc1d37fb9</a>
  .. _PR#1199: <a
  href="https://redirect.github.com/python-semantic-release/python-semantic-release/pull/1199">python-semantic-release/python-semantic-release#1199</a>
  .. _PR#1200: <a
  href="https://redirect.github.com/python-semantic-release/python-semantic-release/pull/1200">python-semantic-release/python-semantic-release#1200</a></p>
  <p>.. _changelog-v9.20.0:</p> <h1>v9.20.0 (2025-02-17)</h1> <h2>✨ Features</h2> <ul> <li>
  <p><strong>cmd-version</strong>: Enable stamping of tag formatted versions into files, closes
  <code>[#846](https://github.com/python-semantic-release/python-semantic-release/issues/846)</code>_
  (<code>PR#1190</code><em>, <code>8906d8e</code></em>)</p> </li> <li>
  <p><strong>cmd-version</strong>: Extend <code>version_variables</code> to stamp versions with
  <code>@</code> symbol separator, closes
  <code>[#1156](https://github.com/python-semantic-release/python-semantic-release/issues/1156)</code>_
  (<code>PR#1185</code><em>, <code>23f69b6</code></em>)</p> </li> </ul> <h2>📖 Documentation</h2>
  <ul> <li> <p><strong>configuration</strong>: Add usage information for tag format version stamping
  (<code>PR#1190</code><em>, <code>8906d8e</code></em>)</p> </li> <li>
  <p><strong>configuration</strong>: Clarify <code>version_variables</code> config description &amp;
  <code>@</code> separator usage (<code>PR#1185</code><em>, <code>23f69b6</code></em>)</p> </li>
  </ul> <h2>⚙️ Build System</h2> <ul> <li><strong>deps</strong>: Add <code>deprecated~=1.2</code>
  for deprecation notices &amp; sphinx documentation (<code>PR#1190</code><em>,
  <code>8906d8e</code></em>)</li> </ul> <p>.. _<a
  href="https://redirect.github.com/python-semantic-release/python-semantic-release/issues/1156">#1156</a>:
  <a
  href="https://redirect.github.com/python-semantic-release/python-semantic-release/issues/1156">python-semantic-release/python-semantic-release#1156</a></p>
  <!-- raw HTML omitted --> </blockquote> <p>... (truncated)</p> </details> <details>
  <summary>Commits</summary> <ul> <li><a
  href="https://github.com/python-semantic-release/python-semantic-release/commit/26bb37cfab71a5a372e3db0f48a6eac57519a4a6"><code>26bb37c</code></a>
  9.21.0</li> <li><a
  href="https://github.com/python-semantic-release/python-semantic-release/commit/1a4116af4b999144998cf94cf84c9c23ff2e352f"><code>1a4116a</code></a>
  ci(release): improve concurrency restrictions to prevent release collisions (...</li> <li><a
  href="https://github.com/python-semantic-release/python-semantic-release/commit/1ac97bc74c69ce61cec98242c19bf8adc1d37fb9"><code>1ac97bc</code></a>
  feat: add package name variant, <code>python-semantic-release</code>, project script (<a
  href="https://redirect.github.com/python-semantic-release/python-semantic-release/issues/1">#1</a>...</li>
  <li><a
  href="https://github.com/python-semantic-release/python-semantic-release/commit/2e868255e9de7550f19996018d8825cb254ba7a4"><code>2e86825</code></a>
  ci(deps): bump <code>python-semantic-release/publish-action@v9.19.1</code> to 9.20.0 (<a
  href="https://redirect.github.com/python-semantic-release/python-semantic-release/issues/1">#1</a>...</li>
  <li><a
  href="https://github.com/python-semantic-release/python-semantic-release/commit/3b7466302c07c543377ec0c79bf178291d51f7ca"><code>3b74663</code></a>
  9.20.0</li> <li><a
  href="https://github.com/python-semantic-release/python-semantic-release/commit/23f69b6ac206d111b1e566367f9b2f033df5c87a"><code>23f69b6</code></a>
  feat(cmd-version): extend <code>version_variables</code> to stamp versions with <code>@</code>
  symb...</li> <li><a
  href="https://github.com/python-semantic-release/python-semantic-release/commit/8906d8e70467af1489d797ec8cb09b1f95e5d409"><code>8906d8e</code></a>
  feat(cmd-version): enable stamping of tag formatted versions into files (<a
  href="https://redirect.github.com/python-semantic-release/python-semantic-release/issues/1190">#1190</a>)</li>
  <li><a
  href="https://github.com/python-semantic-release/python-semantic-release/commit/84b203f75d30f3047705bc669dbeae90f54e2cef"><code>84b203f</code></a>
  test(main): use easiest &amp; common repo for non-comprehensive tests</li> <li><a
  href="https://github.com/python-semantic-release/python-semantic-release/commit/0363ea30bb9fcfc8b5747fea5a8ba1502bd1c4c6"><code>0363ea3</code></a>
  test(cmd-version): fix release notes test implementation to avoid date change...</li> <li><a
  href="https://github.com/python-semantic-release/python-semantic-release/commit/a900b2b21318a8a59cdb25c3d99de732340b77bb"><code>a900b2b</code></a>
  ci(tests-e2e): mark long running tests to prevent windows execution</li> <li>Additional commits
  viewable in <a
  href="https://github.com/python-semantic-release/python-semantic-release/compare/v8.0.7...v9.21">compare
  view</a></li> </ul> </details> <br />

[![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=python-semantic-release&package-manager=pip&previous-version=8.0.7&new-version=9.21.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

You can trigger a rebase of this PR by commenting `@dependabot rebase`.

[//]: # (dependabot-automerge-start) [//]: # (dependabot-automerge-end)

---

<details> <summary>Dependabot commands and options</summary> <br />

You can trigger Dependabot actions by commenting on this PR: - `@dependabot rebase` will rebase this
  PR - `@dependabot recreate` will recreate this PR, overwriting any edits that have been made to it
  - `@dependabot merge` will merge this PR after your CI passes on it - `@dependabot squash and
  merge` will squash and merge this PR after your CI passes on it - `@dependabot cancel merge` will
  cancel a previously requested merge and block automerging - `@dependabot reopen` will reopen this
  PR if it is closed - `@dependabot close` will close this PR and stop Dependabot recreating it. You
  can achieve the same result by closing it manually - `@dependabot show <dependency name> ignore
  conditions` will show all of the ignore conditions of the specified dependency - `@dependabot
  ignore this major version` will close this PR and stop Dependabot creating any more for this major
  version (unless you reopen the PR or upgrade to it yourself) - `@dependabot ignore this minor
  version` will close this PR and stop Dependabot creating any more for this minor version (unless
  you reopen the PR or upgrade to it yourself) - `@dependabot ignore this dependency` will close
  this PR and stop Dependabot creating any more for this dependency (unless you reopen the PR or
  upgrade to it yourself)

</details>

> **Note** > Automatic rebases have been disabled on this pull request as it has been open for over
  30 days.


## v1.1.2 (2025-08-11)

### Chores

- **deps**: Bump actions/cache from 3 to 4
  ([`7e295c7`](https://github.com/Definedge-Securities/pyintegrate/commit/7e295c7bbfcc175748cfdf0eedd036fc4eebf9a8))

Bumps [actions/cache](https://github.com/actions/cache) from 3 to 4. - [Release
  notes](https://github.com/actions/cache/releases) -
  [Changelog](https://github.com/actions/cache/blob/main/RELEASES.md) -
  [Commits](https://github.com/actions/cache/compare/v3...v4)

--- updated-dependencies: - dependency-name: actions/cache dependency-type: direct:production

update-type: version-update:semver-major ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump actions/cache from 3 to 4
  ([#54](https://github.com/Definedge-Securities/pyintegrate/pull/54),
  [`efa48e6`](https://github.com/Definedge-Securities/pyintegrate/commit/efa48e68f9f115d8329fae8bd83dc526fbbdd6a2))

Bumps [actions/cache](https://github.com/actions/cache) from 3 to 4. <details> <summary>Release
  notes</summary> <p><em>Sourced from <a
  href="https://github.com/actions/cache/releases">actions/cache's releases</a>.</em></p>
  <blockquote> <h2>v4.0.0</h2> <h2>What's Changed</h2> <ul> <li>Update action to node20 by <a
  href="https://github.com/takost"><code>@​takost</code></a> in <a
  href="https://redirect.github.com/actions/cache/pull/1284">actions/cache#1284</a></li> <li>feat:
  save-always flag by <a href="https://github.com/to-s"><code>@​to-s</code></a> in <a
  href="https://redirect.github.com/actions/cache/pull/1242">actions/cache#1242</a></li> </ul>
  <h2>New Contributors</h2> <ul> <li><a href="https://github.com/takost"><code>@​takost</code></a>
  made their first contribution in <a
  href="https://redirect.github.com/actions/cache/pull/1284">actions/cache#1284</a></li> <li><a
  href="https://github.com/to-s"><code>@​to-s</code></a> made their first contribution in <a
  href="https://redirect.github.com/actions/cache/pull/1242">actions/cache#1242</a></li> </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/actions/cache/compare/v3...v4.0.0">https://github.com/actions/cache/compare/v3...v4.0.0</a></p>
  <h2>v3.4.0</h2> <h2>⚠️ Important Changes</h2> <p>The cache backend service has been rewritten from
  the ground up for improved performance and reliability. <a
  href="https://github.com/actions/cache">actions/cache</a> now integrates with the new cache
  service (v2) APIs.</p> <p>The new service will gradually roll out as of <strong>February 1st,
  2025</strong>. The legacy service will also be sunset on the same date. Changes in these release
  are <strong>fully backward compatible</strong>.</p> <p><strong>We are deprecating some versions of
  this action</strong>. We recommend upgrading to version <code>v4</code> or <code>v3</code> as soon
  as possible before <strong>February 1st, 2025.</strong> (Upgrade instructions below).</p> <p>If
  you are using pinned SHAs, please use the SHAs of versions <code>v4.2.0</code> or
  <code>v3.4.0</code></p> <p>If you do not upgrade, all workflow runs using any of the deprecated <a
  href="https://github.com/actions/cache">actions/cache</a> will fail.</p> <p>Upgrading to the
  recommended versions will not break your workflows.</p> <p>Read more about the change &amp; access
  the migration guide: <a href="https://github.com/actions/cache/discussions/1510">reference to the
  announcement</a>.</p> <h3>Minor changes</h3> <p>Minor and patch version updates for these
  dependencies:</p> <ul> <li><code>@​actions/core</code>: <code>1.11.1</code></li>
  <li><code>@​actions/io</code>: <code>1.1.3</code></li> <li><code>@​vercel/ncc</code>:
  <code>0.38.3</code></li> </ul> <p><strong>Full Changelog</strong>: <a
  href="https://github.com/actions/cache/compare/v3...v3.4.0">https://github.com/actions/cache/compare/v3...v3.4.0</a></p>
  <h2>v3.3.3</h2> <h2>What's Changed</h2> <ul> <li>Cache v3.3.3 by <a
  href="https://github.com/robherley"><code>@​robherley</code></a> in <a
  href="https://redirect.github.com/actions/cache/pull/1302">actions/cache#1302</a></li> </ul>
  <h2>New Contributors</h2> <ul> <li><a
  href="https://github.com/robherley"><code>@​robherley</code></a> made their first contribution in
  <a href="https://redirect.github.com/actions/cache/pull/1302">actions/cache#1302</a></li> </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/actions/cache/compare/v3...v3.3.3">https://github.com/actions/cache/compare/v3...v3.3.3</a></p>
  <h2>v3.3.2</h2> <h2>What's Changed</h2> <ul> <li>Fixed readme with new segment timeout values by
  <a href="https://github.com/kotewar"><code>@​kotewar</code></a> in <a
  href="https://redirect.github.com/actions/cache/pull/1133">actions/cache#1133</a></li> <li>Readme
  fixes by <a href="https://github.com/kotewar"><code>@​kotewar</code></a> in <a
  href="https://redirect.github.com/actions/cache/pull/1134">actions/cache#1134</a></li> </ul> <!--
  raw HTML omitted --> </blockquote> <p>... (truncated)</p> </details> <details>
  <summary>Changelog</summary> <p><em>Sourced from <a
  href="https://github.com/actions/cache/blob/main/RELEASES.md">actions/cache's
  changelog</a>.</em></p> <blockquote> <h1>Releases</h1> <h3>4.2.0</h3> <p>TLDR; The cache backend
  service has been rewritten from the ground up for improved performance and reliability. <a
  href="https://github.com/actions/cache">actions/cache</a> now integrates with the new cache
  service (v2) APIs.</p> <p>The new service will gradually roll out as of <strong>February 1st,
  2025</strong>. The legacy service will also be sunset on the same date. Changes in these release
  are <strong>fully backward compatible</strong>.</p> <p><strong>We are deprecating some versions of
  this action</strong>. We recommend upgrading to version <code>v4</code> or <code>v3</code> as soon
  as possible before <strong>February 1st, 2025.</strong> (Upgrade instructions below).</p> <p>If
  you are using pinned SHAs, please use the SHAs of versions <code>v4.2.0</code> or
  <code>v3.4.0</code></p> <p>If you do not upgrade, all workflow runs using any of the deprecated <a
  href="https://github.com/actions/cache">actions/cache</a> will fail.</p> <p>Upgrading to the
  recommended versions will not break your workflows.</p> <h3>4.1.2</h3> <ul> <li>Add GitHub
  Enterprise Cloud instances hostname filters to inform API endpoint choices - <a
  href="https://redirect.github.com/actions/cache/pull/1474">#1474</a></li> <li>Security fix: Bump
  braces from 3.0.2 to 3.0.3 - <a
  href="https://redirect.github.com/actions/cache/pull/1475">#1475</a></li> </ul> <h3>4.1.1</h3>
  <ul> <li>Restore original behavior of <code>cache-hit</code> output - <a
  href="https://redirect.github.com/actions/cache/pull/1467">#1467</a></li> </ul> <h3>4.1.0</h3>
  <ul> <li>Ensure <code>cache-hit</code> output is set when a cache is missed - <a
  href="https://redirect.github.com/actions/cache/pull/1404">#1404</a></li> <li>Deprecate
  <code>save-always</code> input - <a
  href="https://redirect.github.com/actions/cache/pull/1452">#1452</a></li> </ul> <h3>4.0.2</h3>
  <ul> <li>Fixed restore <code>fail-on-cache-miss</code> not working.</li> </ul> <h3>4.0.1</h3> <ul>
  <li>Updated <code>isGhes</code> check</li> </ul> <h3>4.0.0</h3> <ul> <li>Updated minimum runner
  version support from node 12 -&gt; node 20</li> </ul> <h3>3.4.0</h3> <ul> <li>Integrated with the
  new cache service (v2) APIs</li> </ul> <h3>3.3.3</h3> <ul> <li>Updates
  <code>@​actions/cache</code> to v3.2.3 to fix accidental mutated path arguments to
  <code>getCacheVersion</code> <a
  href="https://redirect.github.com/actions/toolkit/pull/1378">actions/toolkit#1378</a></li>
  <li>Additional audit fixes of npm package(s)</li> </ul> <!-- raw HTML omitted --> </blockquote>
  <p>... (truncated)</p> </details> <details> <summary>Commits</summary> <ul> <li><a
  href="https://github.com/actions/cache/commit/1bd1e32a3bdc45362d1e726936510720a7c30a57"><code>1bd1e32</code></a>
  Merge pull request <a href="https://redirect.github.com/actions/cache/issues/1509">#1509</a> from
  actions/Link-/cache-4.2.0</li> <li><a
  href="https://github.com/actions/cache/commit/882d7ced4c9b8af53ed67bfa36ee600195e62940"><code>882d7ce</code></a>
  Add 3.4.0 release notes</li> <li><a
  href="https://github.com/actions/cache/commit/f2695d7a42dd0d7ad21976ed7ab91dbdbc3c2216"><code>f2695d7</code></a>
  Rerun CI</li> <li><a
  href="https://github.com/actions/cache/commit/f46ceeb60d3da27b7cbac269520a4b1bfb15f199"><code>f46ceeb</code></a>
  Add licensed output</li> <li><a
  href="https://github.com/actions/cache/commit/e6f5858749f178cf4a01b0d777917ba913710560"><code>e6f5858</code></a>
  Add lodash to list of reviewed licenses</li> <li><a
  href="https://github.com/actions/cache/commit/4ae6f21c0d820c73db2589af6983e001d8c19c1d"><code>4ae6f21</code></a>
  Add reviewed licensed packages</li> <li><a
  href="https://github.com/actions/cache/commit/c16df86586baf94b0deaa873e22eb739c59e5b15"><code>c16df86</code></a>
  Add licensed output</li> <li><a
  href="https://github.com/actions/cache/commit/b109c12f3bdd6fb6a7dd42b202df645243efbd2f"><code>b109c12</code></a>
  Upgrade <code>@​actions/core</code> to 1.11.1 and other deps</li> <li><a
  href="https://github.com/actions/cache/commit/b7d227d702af06e6be1fa308c014252c10bbc267"><code>b7d227d</code></a>
  Upgrade <code>@​vercel/ncc</code> to 0.38.3</li> <li><a
  href="https://github.com/actions/cache/commit/faf639248d95d2a6c5884b8e6588e233eb3b10a0"><code>faf6392</code></a>
  Update RELEASES.md</li> <li>Additional commits viewable in <a
  href="https://github.com/actions/cache/compare/v3...v4">compare view</a></li> </ul> </details> <br
  />

[![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=actions/cache&package-manager=github_actions&previous-version=3&new-version=4)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don't alter it yourself. You can
  also trigger a rebase manually by commenting `@dependabot rebase`.

[//]: # (dependabot-automerge-start) [//]: # (dependabot-automerge-end)

---

<details> <summary>Dependabot commands and options</summary> <br />

You can trigger Dependabot actions by commenting on this PR: - `@dependabot rebase` will rebase this
  PR - `@dependabot recreate` will recreate this PR, overwriting any edits that have been made to it
  - `@dependabot merge` will merge this PR after your CI passes on it - `@dependabot squash and
  merge` will squash and merge this PR after your CI passes on it - `@dependabot cancel merge` will
  cancel a previously requested merge and block automerging - `@dependabot reopen` will reopen this
  PR if it is closed - `@dependabot close` will close this PR and stop Dependabot recreating it. You
  can achieve the same result by closing it manually - `@dependabot show <dependency name> ignore
  conditions` will show all of the ignore conditions of the specified dependency - `@dependabot
  ignore this major version` will close this PR and stop Dependabot creating any more for this major
  version (unless you reopen the PR or upgrade to it yourself) - `@dependabot ignore this minor
  version` will close this PR and stop Dependabot creating any more for this minor version (unless
  you reopen the PR or upgrade to it yourself) - `@dependabot ignore this dependency` will close
  this PR and stop Dependabot creating any more for this dependency (unless you reopen the PR or
  upgrade to it yourself)

</details>


## v1.1.1 (2025-08-11)

### Bug Fixes

- Strike price correction in derivatives master for Symbol Generator.
  ([`6939762`](https://github.com/Definedge-Securities/pyintegrate/commit/6939762756dcf1261d46f9d4968e3107753f9d47))

Bug fix for Strike Calculation in symbols function. It was using XOR, instead of Exponentiation.


## v1.1.0 (2024-12-18)

### Chores

- Update index.rst
  ([`034344a`](https://github.com/Definedge-Securities/pyintegrate/commit/034344aeb3805ecf6b401a87c390f3522844f37e))

Modify Testing section to link to CONTRIBUTING.md

- **deps**: Bump furo from 2023.7.26 to 2023.9.10
  ([`278886f`](https://github.com/Definedge-Securities/pyintegrate/commit/278886f5cf013d87e4134e8d05af692742e92cfa))

Bumps [furo](https://github.com/pradyunsg/furo) from 2023.7.26 to 2023.9.10. - [Release
  notes](https://github.com/pradyunsg/furo/releases) -
  [Changelog](https://github.com/pradyunsg/furo/blob/main/docs/changelog.md) -
  [Commits](https://github.com/pradyunsg/furo/compare/2023.07.26...2023.09.10)

--- updated-dependencies: - dependency-name: furo dependency-type: direct:production

update-type: version-update:semver-minor ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump furo from 2023.7.26 to 2023.9.10
  ([#22](https://github.com/Definedge-Securities/pyintegrate/pull/22),
  [`4d460ba`](https://github.com/Definedge-Securities/pyintegrate/commit/4d460bab900fa40b79058a22fe65c36c08ccbf27))

Bumps [furo](https://github.com/pradyunsg/furo) from 2023.7.26 to 2023.9.10. <details>
  <summary>Changelog</summary> <p><em>Sourced from <a
  href="https://github.com/pradyunsg/furo/blob/main/docs/changelog.md">furo's
  changelog</a>.</em></p> <blockquote> <h1>Changelog</h1> <!-- raw HTML omitted --> <h2>2023.09.10
  -- Zesty Zaffre</h2> <ul> <li>Make asset hash injection idempotent, fixing Sphinx 6
  compatibility.</li> <li>Fix the check for HTML builders, fixing non-HTML Read the Docs
  builds.</li> </ul> <h2>2023.08.19 -- Xenolithic Xanadu</h2> <ul> <li>Fix missing search context
  with Sphinx 7.2, for dirhtml builds.</li> <li>Drop support for Python 3.7.</li> <li>Present
  configuration errors in a better format -- thanks <a
  href="https://github.com/AA-Turner"><code>@​AA-Turner</code></a>!</li> <li>Bump
  <code>require_sphinx()</code> to Sphinx 6.0, in line with dependency changes in Unassuming
  Ultramarine.</li> </ul> <h2>2023.08.17 -- Wonderous White</h2> <ul> <li>Fix compatiblity with
  Sphinx 7.2.0 and 7.2.1.</li> </ul> <h2>2023.07.26 -- Vigilant Volt</h2> <ul> <li>Fix compatiblity
  with Sphinx 7.1.</li> <li>Improve how content overflow is handled.</li> <li>Improve how literal
  blocks containing inline code are handled.</li> </ul> <h2>2023.05.20 -- Unassuming
  Ultramarine</h2> <ul> <li>✨ Add support for Sphinx 7.</li> <li>Drop support for Sphinx 5.</li>
  <li>Improve the screen-reader label for sidebar collapse.</li> <li>Make it easier to create
  derived themes from Furo.</li> <li>Bump all JS dependencies (NodeJS and npm packages).</li> </ul>
  <h2>2023.03.27 -- Tasty Tangerine</h2> <ul> <li>Regenerate with newer version of
  sphinx-theme-builder, to fix RECORD hashes.</li> <li>Add missing class to Font Awesome
  examples</li> </ul> <h2>2023.03.23 -- Sassy Saffron</h2> <!-- raw HTML omitted --> </blockquote>
  <p>... (truncated)</p> </details> <details> <summary>Commits</summary> <ul> <li><a
  href="https://github.com/pradyunsg/furo/commit/2718ca42930f7c8c11bc96341e0d3db6f532b08d"><code>2718ca4</code></a>
  Prepare release: 2023.09.10</li> <li><a
  href="https://github.com/pradyunsg/furo/commit/c22c99d931decfa4641e400e428606bc6184af56"><code>c22c99d</code></a>
  Update changelog</li> <li><a
  href="https://github.com/pradyunsg/furo/commit/c37e84961d9ffbc77ab7be268081d1b3497f0311"><code>c37e849</code></a>
  Quote a not-runtime-generic type annotation</li> <li><a
  href="https://github.com/pradyunsg/furo/commit/9cfdf44784dc90085549490ff1eddd2afc37c1d6"><code>9cfdf44</code></a>
  Rework infrastructure for linting</li> <li><a
  href="https://github.com/pradyunsg/furo/commit/5abeb9fc962aee61eda02e0c75e872004635e9d5"><code>5abeb9f</code></a>
  Fix the check for HTML builders</li> <li><a
  href="https://github.com/pradyunsg/furo/commit/ee2ab5459ddb0a32c3467b88c9c628611eb55073"><code>ee2ab54</code></a>
  Tweak how tests are run with nox</li> <li><a
  href="https://github.com/pradyunsg/furo/commit/cdae2366c340695ba724ca8438a4cd1e605c8848"><code>cdae236</code></a>
  Test against Sphinx minor versions in CI</li> <li><a
  href="https://github.com/pradyunsg/furo/commit/9e40071eb8c4c3e38845b57c4f5242bef2a44af2"><code>9e40071</code></a>
  Make asset hash injection idempotent</li> <li><a
  href="https://github.com/pradyunsg/furo/commit/aab86f4624b6ef38a151440be5624746d41882b1"><code>aab86f4</code></a>
  Revert &quot;Exclude incompatible Sphinx releases (<a
  href="https://redirect.github.com/pradyunsg/furo/issues/711">#711</a>)&quot;</li> <li><a
  href="https://github.com/pradyunsg/furo/commit/4dd6eec9e306b5fd0624ec8d1d90c6ad416c5182"><code>4dd6eec</code></a>
  Exclude incompatible Sphinx releases (<a
  href="https://redirect.github.com/pradyunsg/furo/issues/711">#711</a>)</li> <li>Additional commits
  viewable in <a href="https://github.com/pradyunsg/furo/compare/2023.07.26...2023.09.10">compare
  view</a></li> </ul> </details> <br />

[![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=furo&package-manager=pip&previous-version=2023.7.26&new-version=2023.9.10)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don't alter it yourself. You can
  also trigger a rebase manually by commenting `@dependabot rebase`.

[//]: # (dependabot-automerge-start) [//]: # (dependabot-automerge-end)

---

<details> <summary>Dependabot commands and options</summary> <br />

You can trigger Dependabot actions by commenting on this PR: - `@dependabot rebase` will rebase this
  PR - `@dependabot recreate` will recreate this PR, overwriting any edits that have been made to it
  - `@dependabot merge` will merge this PR after your CI passes on it - `@dependabot squash and
  merge` will squash and merge this PR after your CI passes on it - `@dependabot cancel merge` will
  cancel a previously requested merge and block automerging - `@dependabot reopen` will reopen this
  PR if it is closed - `@dependabot close` will close this PR and stop Dependabot recreating it. You
  can achieve the same result by closing it manually - `@dependabot show <dependency name> ignore
  conditions` will show all of the ignore conditions of the specified dependency - `@dependabot
  ignore this major version` will close this PR and stop Dependabot creating any more for this major
  version (unless you reopen the PR or upgrade to it yourself) - `@dependabot ignore this minor
  version` will close this PR and stop Dependabot creating any more for this minor version (unless
  you reopen the PR or upgrade to it yourself) - `@dependabot ignore this dependency` will close
  this PR and stop Dependabot creating any more for this dependency (unless you reopen the PR or
  upgrade to it yourself)

</details>

- **deps**: Bump sphinx from 7.1.2 to 7.2.0
  ([`6820dc7`](https://github.com/Definedge-Securities/pyintegrate/commit/6820dc741982d0aa5a21ec0d0aaf3a0a726d4890))

Bumps [sphinx](https://github.com/sphinx-doc/sphinx) from 7.1.2 to 7.2.0. - [Release
  notes](https://github.com/sphinx-doc/sphinx/releases) -
  [Changelog](https://github.com/sphinx-doc/sphinx/blob/master/CHANGES) -
  [Commits](https://github.com/sphinx-doc/sphinx/compare/v7.1.2...v7.2.0)

--- updated-dependencies: - dependency-name: sphinx dependency-type: direct:production

update-type: version-update:semver-minor ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump sphinx from 7.1.2 to 7.2.0
  ([#6](https://github.com/Definedge-Securities/pyintegrate/pull/6),
  [`5c84f9f`](https://github.com/Definedge-Securities/pyintegrate/commit/5c84f9fc65cc228872e910051f0b9f40be84601f))

Bumps [sphinx](https://github.com/sphinx-doc/sphinx) from 7.1.2 to 7.2.0. <details> <summary>Release
  notes</summary> <p><em>Sourced from <a
  href="https://github.com/sphinx-doc/sphinx/releases">sphinx's releases</a>.</em></p> <blockquote>
  <h2>Sphinx 7.2.0</h2> <p>Changelog: <a
  href="https://www.sphinx-doc.org/en/master/changes.html">https://www.sphinx-doc.org/en/master/changes.html</a></p>
  </blockquote> </details> <details> <summary>Changelog</summary> <p><em>Sourced from <a
  href="https://github.com/sphinx-doc/sphinx/blob/master/CHANGES">sphinx's changelog</a>.</em></p>
  <blockquote> <h1>Release 7.2.0 (released Aug 17, 2023)</h1> <h2>Dependencies</h2> <ul> <li><a
  href="https://redirect.github.com/sphinx-doc/sphinx/issues/11511">#11511</a>: Drop Python 3.8
  support.</li> <li><a href="https://redirect.github.com/sphinx-doc/sphinx/issues/11576">#11576</a>:
  Require Pygments 2.14 or later.</li> </ul> <h2>Deprecated</h2> <ul> <li><a
  href="https://redirect.github.com/sphinx-doc/sphinx/issues/11512">#11512</a>: Deprecate
  <code>sphinx.util.md5</code> and <code>sphinx.util.sha1</code>. Use <code>hashlib</code>
  instead.</li> <li><a href="https://redirect.github.com/sphinx-doc/sphinx/issues/11526">#11526</a>:
  Deprecate <code>sphinx.testing.path</code>. Use <code>os.path</code> or <code>pathlib</code>
  instead.</li> <li><a href="https://redirect.github.com/sphinx-doc/sphinx/issues/11528">#11528</a>:
  Deprecate <code>sphinx.util.split_index_msg</code> and <code>sphinx.util.split_into</code>. Use
  <code>sphinx.util.index_entries.split_index_msg</code> instead.</li> <li>Deprecate
  <code>sphinx.builders.html.Stylesheet</code> and <code>sphinx.builders.html.Javascript</code>. Use
  <code>sphinx.application.Sphinx.add_css_file()</code> and
  <code>sphinx.application.Sphinx.add_js_file()</code> instead.</li> <li><a
  href="https://redirect.github.com/sphinx-doc/sphinx/issues/11582">#11582</a>: Deprecate
  <code>sphinx.builders.html.StandaloneHTMLBuilder.css_files</code> and
  <code>sphinx.builders.html.StandaloneHTMLBuilder.script_files</code>. Use
  <code>sphinx.application.Sphinx.add_css_file()</code> and
  <code>sphinx.application.Sphinx.add_js_file()</code> instead.</li> <li><a
  href="https://redirect.github.com/sphinx-doc/sphinx/issues/11459">#11459</a>: Deprecate
  <code>sphinx.ext.autodoc.preserve_defaults.get_function_def()</code>. Patch by Bénédikt Tran.</li>
  </ul> <h2>Features added</h2> <ul> <li><a
  href="https://redirect.github.com/sphinx-doc/sphinx/issues/11526">#11526</a>: Support
  <code>os.PathLike</code> types and <code>pathlib.Path</code> objects in many more places.</li>
  <li><a href="https://redirect.github.com/sphinx-doc/sphinx/issues/5474">#5474</a>: coverage: Print
  summary statistics tables. Patch by Jorge Leitao.</li> <li><a
  href="https://redirect.github.com/sphinx-doc/sphinx/issues/6319">#6319</a>: viewcode: Add
  :confval:<code>viewcode_line_numbers</code> to control whether line numbers are added to rendered
  source code. Patch by Ben Krikler.</li> <li><a
  href="https://redirect.github.com/sphinx-doc/sphinx/issues/9662">#9662</a>: Add the
  <code>:no-typesetting:</code> option to suppress textual output and only create a linkable anchor.
  Patch by Latosha Maltba.</li> <li><a
  href="https://redirect.github.com/sphinx-doc/sphinx/issues/11221">#11221</a>: C++: Support domain
  objects in the table of contents. Patch by Rouslan Korneychuk.</li> <li><a
  href="https://redirect.github.com/sphinx-doc/sphinx/issues/10938">#10938</a>: doctest: Add
  :confval:<code>doctest_show_successes</code> option. Patch by Trey Hunner.</li> <li><a
  href="https://redirect.github.com/sphinx-doc/sphinx/issues/11533">#11533</a>: Add
  <code>:no-index:</code>, <code>:no-index-entry:</code>, and <code>:no-contents-entry:</code>.</li>
  <li><a href="https://redirect.github.com/sphinx-doc/sphinx/issues/11572">#11572</a>: Improve
  <code>debug</code> logging of reasons why files are detected as out of date. Patch by Eric
  Larson.</li> </ul> <!-- raw HTML omitted --> </blockquote> <p>... (truncated)</p> </details>
  <details> <summary>Commits</summary> <ul> <li><a
  href="https://github.com/sphinx-doc/sphinx/commit/da9f8a5c33ad5eeef05dd780f2988f3ff7351ef3"><code>da9f8a5</code></a>
  Bump to 7.2.0 final</li> <li><a
  href="https://github.com/sphinx-doc/sphinx/commit/794324ac000095aa6409a4958b44a17dc25d3b49"><code>794324a</code></a>
  Declare support for Python 3.13</li> <li><a
  href="https://github.com/sphinx-doc/sphinx/commit/03bceac43ff1e69a33fe973612504738182cf217"><code>03bceac</code></a>
  [bot]: Update message catalogues (<a
  href="https://redirect.github.com/sphinx-doc/sphinx/issues/11538">#11538</a>)</li> <li><a
  href="https://github.com/sphinx-doc/sphinx/commit/aecebcea9a3f6cbd3f379bc34f99d2ffb0f87220"><code>aecebce</code></a>
  Make <code>_resolve_toctree()</code> keyword-only</li> <li><a
  href="https://github.com/sphinx-doc/sphinx/commit/76658c49a931745da45fa4d5c8d482b7c6facd4f"><code>76658c4</code></a>
  Fix <code>sphinx.ext.autodoc.preserve_defaults</code> (<a
  href="https://redirect.github.com/sphinx-doc/sphinx/issues/11550">#11550</a>)</li> <li><a
  href="https://github.com/sphinx-doc/sphinx/commit/4dee1629901f5e5c2aefc274da42483e16770e50"><code>4dee162</code></a>
  Fix layout issues in the agogo theme for smaller viewports (<a
  href="https://redirect.github.com/sphinx-doc/sphinx/issues/11594">#11594</a>)</li> <li><a
  href="https://github.com/sphinx-doc/sphinx/commit/4ddbee4a7cdf14a7d064ffaea6cbb0c4fdb63f23"><code>4ddbee4</code></a>
  Fix <code>console_scripts</code> entry points</li> <li><a
  href="https://github.com/sphinx-doc/sphinx/commit/4add50a5f0c3ff7954edcec3d33dd1c0fa40a1a6"><code>4add50a</code></a>
  Remove unneeded type annotation</li> <li><a
  href="https://github.com/sphinx-doc/sphinx/commit/9d8ef833dbf9d7bb04771e622d6ceea738ac9d18"><code>9d8ef83</code></a>
  Fix <code>test_inspect_main_noargs</code></li> <li><a
  href="https://github.com/sphinx-doc/sphinx/commit/ddf8a8e7d4756170d5ee6dff7fc88ecd12912e59"><code>ddf8a8e</code></a>
  Add CHANGES entry for <a
  href="https://redirect.github.com/sphinx-doc/sphinx/issues/11533">GH-11533</a></li> <li>Additional
  commits viewable in <a href="https://github.com/sphinx-doc/sphinx/compare/v7.1.2...v7.2.0">compare
  view</a></li> </ul> </details> <br />

[![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=sphinx&package-manager=pip&previous-version=7.1.2&new-version=7.2.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don't alter it yourself. You can
  also trigger a rebase manually by commenting `@dependabot rebase`.

[//]: # (dependabot-automerge-start) [//]: # (dependabot-automerge-end)

---

<details> <summary>Dependabot commands and options</summary> <br />

You can trigger Dependabot actions by commenting on this PR: - `@dependabot rebase` will rebase this
  PR - `@dependabot recreate` will recreate this PR, overwriting any edits that have been made to it
  - `@dependabot merge` will merge this PR after your CI passes on it - `@dependabot squash and
  merge` will squash and merge this PR after your CI passes on it - `@dependabot cancel merge` will
  cancel a previously requested merge and block automerging - `@dependabot reopen` will reopen this
  PR if it is closed - `@dependabot close` will close this PR and stop Dependabot recreating it. You
  can achieve the same result by closing it manually - `@dependabot show <dependency name> ignore
  conditions` will show all of the ignore conditions of the specified dependency - `@dependabot
  ignore this major version` will close this PR and stop Dependabot creating any more for this major
  version (unless you reopen the PR or upgrade to it yourself) - `@dependabot ignore this minor
  version` will close this PR and stop Dependabot creating any more for this minor version (unless
  you reopen the PR or upgrade to it yourself) - `@dependabot ignore this dependency` will close
  this PR and stop Dependabot creating any more for this dependency (unless you reopen the PR or
  upgrade to it yourself)

</details>

- **deps**: Bump sphinx from 7.2.0 to 7.2.4
  ([`6bc47de`](https://github.com/Definedge-Securities/pyintegrate/commit/6bc47de314e1c0d6163883a13ab298b0e0ba3e96))

Bumps [sphinx](https://github.com/sphinx-doc/sphinx) from 7.2.0 to 7.2.4. - [Release
  notes](https://github.com/sphinx-doc/sphinx/releases) -
  [Changelog](https://github.com/sphinx-doc/sphinx/blob/master/CHANGES) -
  [Commits](https://github.com/sphinx-doc/sphinx/compare/v7.2.0...v7.2.4)

--- updated-dependencies: - dependency-name: sphinx dependency-type: direct:production

update-type: version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump sphinx from 7.2.0 to 7.2.4
  ([#14](https://github.com/Definedge-Securities/pyintegrate/pull/14),
  [`45eb3c2`](https://github.com/Definedge-Securities/pyintegrate/commit/45eb3c2416e6cba538b9e3f2f32958ab4addad33))

Bumps [sphinx](https://github.com/sphinx-doc/sphinx) from 7.2.0 to 7.2.4. <details> <summary>Release
  notes</summary> <p><em>Sourced from <a
  href="https://github.com/sphinx-doc/sphinx/releases">sphinx's releases</a>.</em></p> <blockquote>
  <h2>Sphinx 7.2.4</h2> <p>Changelog: <a
  href="https://www.sphinx-doc.org/en/master/changes.html">https://www.sphinx-doc.org/en/master/changes.html</a></p>
  <h2>Sphinx 7.2.3</h2> <p>Changelog: <a
  href="https://www.sphinx-doc.org/en/master/changes.html">https://www.sphinx-doc.org/en/master/changes.html</a></p>
  <h2>Sphinx 7.2.2</h2> <p>Changelog: <a
  href="https://www.sphinx-doc.org/en/master/changes.html">https://www.sphinx-doc.org/en/master/changes.html</a></p>
  <h2>Sphinx 7.2.1</h2> <p>Changelog: <a
  href="https://www.sphinx-doc.org/en/master/changes.html">https://www.sphinx-doc.org/en/master/changes.html</a></p>
  </blockquote> </details> <details> <summary>Changelog</summary> <p><em>Sourced from <a
  href="https://github.com/sphinx-doc/sphinx/blob/master/CHANGES">sphinx's changelog</a>.</em></p>
  <blockquote> <h1>Release 7.2.4 (released Aug 28, 2023)</h1> <h2>Bugs fixed</h2> <ul> <li><a
  href="https://redirect.github.com/sphinx-doc/sphinx/issues/11618">#11618</a>: Fix a regression in
  the MoveModuleTargets transform, introduced in <a
  href="https://redirect.github.com/sphinx-doc/sphinx/issues/10478">#10478</a> (<a
  href="https://redirect.github.com/sphinx-doc/sphinx/issues/9662">#9662</a>).</li> <li><a
  href="https://redirect.github.com/sphinx-doc/sphinx/issues/11649">#11649</a>: linkcheck: Fix
  conversions from UTC to UNIX time for timezones west of London.</li> </ul> <h1>Release 7.2.3
  (released Aug 23, 2023)</h1> <h2>Dependencies</h2> <ul> <li><a
  href="https://redirect.github.com/sphinx-doc/sphinx/issues/11576">#11576</a>: Require
  sphinxcontrib-serializinghtml 1.1.9.</li> </ul> <h2>Bugs fixed</h2> <ul> <li>Fix regression in
  <code>autodoc.Documenter.parse_name()</code>.</li> <li>Fix regression in JSON serialisation.</li>
  <li><a href="https://redirect.github.com/sphinx-doc/sphinx/issues/11543">#11543</a>: autodoc:
  Support positional-only parameters in <code>classmethod</code> methods when
  <code>autodoc_preserve_defaults</code> is <code>True</code>.</li> <li>Restore support string
  methods on path objects. This is deprecated and will be removed in Sphinx 8. Use
  :py:func:<code>os.fspath</code> to convert :py:class:<code>~pathlib.Path</code> objects to
  strings, or :py:class:<code>~pathlib.Path</code>'s methods to work with path objects.</li> </ul>
  <h1>Release 7.2.2 (released Aug 17, 2023)</h1> <h2>Bugs fixed</h2> <ul> <li>Fix the signature of
  the <code>StateMachine.insert_input()</code> patch, for when calling with keyword arguments.</li>
  <li>Fixed membership testing (<code>in</code>) for the :py:class:<code>str</code> interface of the
  asset classes (<code>_CascadingStyleSheet</code> and <code>_JavaScript</code>), which several
  extensions relied upon.</li> <li>Fixed a type error in
  <code>SingleFileHTMLBuilder._get_local_toctree</code>, <code>includehidden</code> may be passed as
  a string or a boolean.</li> <li>Fix <code>:noindex:</code> for <code>PyModule</code> and
  <code>JSModule</code>.</li> </ul> <h1>Release 7.2.1 (released Aug 17, 2023)</h1> <p>Bugs fixed</p>
  <!-- raw HTML omitted --> </blockquote> <p>... (truncated)</p> </details> <details>
  <summary>Commits</summary> <ul> <li><a
  href="https://github.com/sphinx-doc/sphinx/commit/3037f8599c8d9638c4570784ec72bcc36d9f7fd2"><code>3037f85</code></a>
  Bump version</li> <li><a
  href="https://github.com/sphinx-doc/sphinx/commit/3256f1f22092a3e9c2925472f6f0b41e4f09e902"><code>3256f1f</code></a>
  Bump to 7.2.4 final</li> <li><a
  href="https://github.com/sphinx-doc/sphinx/commit/2f025a4b226610a170d008a24eeba4f90719fa76"><code>2f025a4</code></a>
  linkcheck: Fix conversion from UTC time to the UNIX epoch (<a

href="https://redirect.github.com/sphinx-doc/sphinx/issues/11649">#11649</a>)</li> <li><a
  href="https://github.com/sphinx-doc/sphinx/commit/1567281287f780d83d5c1b1202a7e551fd0b3998"><code>1567281</code></a>
  autodoc: Fix UnboundLocalError in <code>filter_members</code> (<a

href="https://redirect.github.com/sphinx-doc/sphinx/issues/11651">#11651</a>)</li> <li><a
  href="https://github.com/sphinx-doc/sphinx/commit/5e88b9f88665dd8782b9feb381b499ae580cfa1a"><code>5e88b9f</code></a>
  Fix the MoveModuleTargets transform (<a
  href="https://redirect.github.com/sphinx-doc/sphinx/issues/11647">#11647</a>)</li> <li><a
  href="https://github.com/sphinx-doc/sphinx/commit/694fcee13d4298ca39ff08837c28b12b2485fbfd"><code>694fcee</code></a>
  Fix markup in CHANGES (<a
  href="https://redirect.github.com/sphinx-doc/sphinx/issues/11639">#11639</a>)</li> <li><a
  href="https://github.com/sphinx-doc/sphinx/commit/c503c90090efb54eab81621dde73e4c57e1af1e6"><code>c503c90</code></a>
  Improve <code>pathlib</code> type annotations (<a
  href="https://redirect.github.com/sphinx-doc/sphinx/issues/11646">#11646</a>)</li> <li><a
  href="https://github.com/sphinx-doc/sphinx/commit/bf339b123e9f01bfc62663849563d52a7099701a"><code>bf339b1</code></a>
  Bump version</li> <li><a
  href="https://github.com/sphinx-doc/sphinx/commit/2f6ea1422b08f9494f34b80c2ff6c96b5f396fdc"><code>2f6ea14</code></a>
  Bump to 7.2.3 final</li> <li><a
  href="https://github.com/sphinx-doc/sphinx/commit/511e4070aa429a41eac04e88d96806c8fd0a5cc7"><code>511e407</code></a>
  Implement <code>bool()</code> for string paths</li> <li>Additional commits viewable in <a
  href="https://github.com/sphinx-doc/sphinx/compare/v7.2.0...v7.2.4">compare view</a></li> </ul>
  </details> <br />

[![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=sphinx&package-manager=pip&previous-version=7.2.0&new-version=7.2.4)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don't alter it yourself. You can
  also trigger a rebase manually by commenting `@dependabot rebase`.

[//]: # (dependabot-automerge-start) [//]: # (dependabot-automerge-end)

---

<details> <summary>Dependabot commands and options</summary> <br />

You can trigger Dependabot actions by commenting on this PR: - `@dependabot rebase` will rebase this
  PR - `@dependabot recreate` will recreate this PR, overwriting any edits that have been made to it
  - `@dependabot merge` will merge this PR after your CI passes on it - `@dependabot squash and
  merge` will squash and merge this PR after your CI passes on it - `@dependabot cancel merge` will
  cancel a previously requested merge and block automerging - `@dependabot reopen` will reopen this
  PR if it is closed - `@dependabot close` will close this PR and stop Dependabot recreating it. You
  can achieve the same result by closing it manually - `@dependabot show <dependency name> ignore
  conditions` will show all of the ignore conditions of the specified dependency - `@dependabot
  ignore this major version` will close this PR and stop Dependabot creating any more for this major
  version (unless you reopen the PR or upgrade to it yourself) - `@dependabot ignore this minor
  version` will close this PR and stop Dependabot creating any more for this minor version (unless
  you reopen the PR or upgrade to it yourself) - `@dependabot ignore this dependency` will close
  this PR and stop Dependabot creating any more for this dependency (unless you reopen the PR or
  upgrade to it yourself)

</details>

- **deps-dev**: Bump mypy from 1.5.0 to 1.5.1
  ([`177ee12`](https://github.com/Definedge-Securities/pyintegrate/commit/177ee12cc7cb49bc7d83b6618ed781ac5762282f))

Bumps [mypy](https://github.com/python/mypy) from 1.5.0 to 1.5.1. -
  [Commits](https://github.com/python/mypy/compare/v1.5.0...v1.5.1)

--- updated-dependencies: - dependency-name: mypy dependency-type: direct:development

update-type: version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps-dev**: Bump mypy from 1.5.0 to 1.5.1
  ([#7](https://github.com/Definedge-Securities/pyintegrate/pull/7),
  [`9192d9e`](https://github.com/Definedge-Securities/pyintegrate/commit/9192d9e9b682ad400c2e9f9ad9ace6db48bc0b92))

Bumps [mypy](https://github.com/python/mypy) from 1.5.0 to 1.5.1. <details>
  <summary>Commits</summary> <ul> <li><a
  href="https://github.com/python/mypy/commit/de4f2ad99c88b885677247534dcec335621ade4d"><code>de4f2ad</code></a>
  [Release 1.5] Bump version to 1.5.1 to pick up last 2 CPs</li> <li><a
  href="https://github.com/python/mypy/commit/2ff7c0de571d434a9a1f82fa183d32fa32999b40"><code>2ff7c0d</code></a>
  [release 1.5] stubtest: Fix <code>__mypy-replace</code> false positives (<a
  href="https://redirect.github.com/python/mypy/issues/15689">#15689</a>) (<a
  href="https://redirect.github.com/python/mypy/issues/15751">#15751</a>)</li> <li><a
  href="https://github.com/python/mypy/commit/373b73abeb14fdd1f3021f4c27fe1721d2986ed4"><code>373b73a</code></a>
  [Release 1.5] Update typing_extensions stubs (<a
  href="https://redirect.github.com/python/mypy/issues/15745">#15745</a>)</li> <li>See full diff in
  <a href="https://github.com/python/mypy/compare/v1.5.0...v1.5.1">compare view</a></li> </ul>
  </details> <br />

[![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=mypy&package-manager=pip&previous-version=1.5.0&new-version=1.5.1)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don't alter it yourself. You can
  also trigger a rebase manually by commenting `@dependabot rebase`.

[//]: # (dependabot-automerge-start) [//]: # (dependabot-automerge-end)

---

<details> <summary>Dependabot commands and options</summary> <br />

You can trigger Dependabot actions by commenting on this PR: - `@dependabot rebase` will rebase this
  PR - `@dependabot recreate` will recreate this PR, overwriting any edits that have been made to it
  - `@dependabot merge` will merge this PR after your CI passes on it - `@dependabot squash and
  merge` will squash and merge this PR after your CI passes on it - `@dependabot cancel merge` will
  cancel a previously requested merge and block automerging - `@dependabot reopen` will reopen this
  PR if it is closed - `@dependabot close` will close this PR and stop Dependabot recreating it. You
  can achieve the same result by closing it manually - `@dependabot show <dependency name> ignore
  conditions` will show all of the ignore conditions of the specified dependency - `@dependabot
  ignore this major version` will close this PR and stop Dependabot creating any more for this major
  version (unless you reopen the PR or upgrade to it yourself) - `@dependabot ignore this minor
  version` will close this PR and stop Dependabot creating any more for this minor version (unless
  you reopen the PR or upgrade to it yourself) - `@dependabot ignore this dependency` will close
  this PR and stop Dependabot creating any more for this dependency (unless you reopen the PR or
  upgrade to it yourself)

</details>

- **deps-dev**: Bump pre-commit from 3.3.3 to 3.5.0
  ([`da12302`](https://github.com/Definedge-Securities/pyintegrate/commit/da12302540809c2f1addf9dffc2aa6b933bc580b))

Bumps [pre-commit](https://github.com/pre-commit/pre-commit) from 3.3.3 to 3.5.0. - [Release
  notes](https://github.com/pre-commit/pre-commit/releases) -
  [Changelog](https://github.com/pre-commit/pre-commit/blob/main/CHANGELOG.md) -
  [Commits](https://github.com/pre-commit/pre-commit/compare/v3.3.3...v3.5.0)

--- updated-dependencies: - dependency-name: pre-commit dependency-type: direct:development

update-type: version-update:semver-minor ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps-dev**: Bump pre-commit from 3.3.3 to 3.5.0
  ([#29](https://github.com/Definedge-Securities/pyintegrate/pull/29),
  [`42bc713`](https://github.com/Definedge-Securities/pyintegrate/commit/42bc713f069fd582602bea05bcf55b49094f5c0f))

Bumps [pre-commit](https://github.com/pre-commit/pre-commit) from 3.3.3 to 3.5.0. <details>
  <summary>Release notes</summary> <p><em>Sourced from <a
  href="https://github.com/pre-commit/pre-commit/releases">pre-commit's releases</a>.</em></p>
  <blockquote> <h2>pre-commit v3.5.0</h2> <h3>Features</h3> <ul> <li>Improve performance of
  <code>check-hooks-apply</code> and <code>check-useless-excludes</code>. <ul> <li><a
  href="https://redirect.github.com/pre-commit/pre-commit/issues/2998">#2998</a> PR by <a
  href="https://github.com/mxr"><code>@​mxr</code></a>.</li> <li><a
  href="https://redirect.github.com/pre-commit/pre-commit/issues/2935">#2935</a> issue by <a
  href="https://github.com/mxr"><code>@​mxr</code></a>.</li> </ul> </li> </ul> <h3>Fixes</h3> <ul>
  <li>Use <code>time.monotonic()</code> for more accurate hook timing. <ul> <li><a
  href="https://redirect.github.com/pre-commit/pre-commit/issues/3024">#3024</a> PR by <a
  href="https://github.com/adamchainz"><code>@​adamchainz</code></a>.</li> </ul> </li> </ul>
  <h3>Migrating</h3> <ul> <li>Require npm 6.x+ for <code>language: node</code> hooks. <ul> <li><a
  href="https://redirect.github.com/pre-commit/pre-commit/issues/2996">#2996</a> PR by <a
  href="https://github.com/RoelAdriaans"><code>@​RoelAdriaans</code></a>.</li> <li><a
  href="https://redirect.github.com/pre-commit/pre-commit/issues/1983">#1983</a> issue by <a
  href="https://github.com/henryiii"><code>@​henryiii</code></a>.</li> </ul> </li> </ul>
  <h2>pre-commit v3.4.0</h2> <h3>Features</h3> <ul> <li>Add <code>language: haskell</code>. <ul>
  <li><a href="https://redirect.github.com/pre-commit/pre-commit/issues/2932">#2932</a> by <a
  href="https://github.com/alunduil"><code>@​alunduil</code></a>.</li> </ul> </li> <li>Improve cpu
  count detection when run under cgroups. <ul> <li><a
  href="https://redirect.github.com/pre-commit/pre-commit/issues/2979">#2979</a> PR by <a
  href="https://github.com/jdb8"><code>@​jdb8</code></a>.</li> <li><a
  href="https://redirect.github.com/pre-commit/pre-commit/issues/2978">#2978</a> issue by <a
  href="https://github.com/jdb8"><code>@​jdb8</code></a>.</li> </ul> </li> </ul> <h3>Fixes</h3> <ul>
  <li>Handle negative exit codes from hooks receiving posix signals. <ul> <li><a
  href="https://redirect.github.com/pre-commit/pre-commit/issues/2971">#2971</a> PR by <a
  href="https://github.com/chriskuehl"><code>@​chriskuehl</code></a>.</li> <li><a
  href="https://redirect.github.com/pre-commit/pre-commit/issues/2970">#2970</a> issue by <a
  href="https://github.com/chriskuehl"><code>@​chriskuehl</code></a>.</li> </ul> </li> </ul>
  </blockquote> </details> <details> <summary>Changelog</summary> <p><em>Sourced from <a
  href="https://github.com/pre-commit/pre-commit/blob/main/CHANGELOG.md">pre-commit's
  changelog</a>.</em></p> <blockquote> <h1>3.5.0 - 2023-10-13</h1> <h3>Features</h3> <ul>
  <li>Improve performance of <code>check-hooks-apply</code> and <code>check-useless-excludes</code>.
  <ul> <li><a href="https://redirect.github.com/pre-commit/pre-commit/issues/2998">#2998</a> PR by
  <a href="https://github.com/mxr"><code>@​mxr</code></a>.</li> <li><a
  href="https://redirect.github.com/pre-commit/pre-commit/issues/2935">#2935</a> issue by <a
  href="https://github.com/mxr"><code>@​mxr</code></a>.</li> </ul> </li> </ul> <h3>Fixes</h3> <ul>
  <li>Use <code>time.monotonic()</code> for more accurate hook timing. <ul> <li><a
  href="https://redirect.github.com/pre-commit/pre-commit/issues/3024">#3024</a> PR by <a
  href="https://github.com/adamchainz"><code>@​adamchainz</code></a>.</li> </ul> </li> </ul>
  <h3>Migrating</h3> <ul> <li>Require npm 6.x+ for <code>language: node</code> hooks. <ul> <li><a
  href="https://redirect.github.com/pre-commit/pre-commit/issues/2996">#2996</a> PR by <a
  href="https://github.com/RoelAdriaans"><code>@​RoelAdriaans</code></a>.</li> <li><a
  href="https://redirect.github.com/pre-commit/pre-commit/issues/1983">#1983</a> issue by <a
  href="https://github.com/henryiii"><code>@​henryiii</code></a>.</li> </ul> </li> </ul> <h1>3.4.0 -
  2023-09-02</h1> <h3>Features</h3> <ul> <li>Add <code>language: haskell</code>. <ul> <li><a
  href="https://redirect.github.com/pre-commit/pre-commit/issues/2932">#2932</a> by <a
  href="https://github.com/alunduil"><code>@​alunduil</code></a>.</li> </ul> </li> <li>Improve cpu
  count detection when run under cgroups. <ul> <li><a
  href="https://redirect.github.com/pre-commit/pre-commit/issues/2979">#2979</a> PR by <a
  href="https://github.com/jdb8"><code>@​jdb8</code></a>.</li> <li><a
  href="https://redirect.github.com/pre-commit/pre-commit/issues/2978">#2978</a> issue by <a
  href="https://github.com/jdb8"><code>@​jdb8</code></a>.</li> </ul> </li> </ul> <h3>Fixes</h3> <ul>
  <li>Handle negative exit codes from hooks receiving posix signals. <ul> <li><a
  href="https://redirect.github.com/pre-commit/pre-commit/issues/2971">#2971</a> PR by <a
  href="https://github.com/chriskuehl"><code>@​chriskuehl</code></a>.</li> <li><a
  href="https://redirect.github.com/pre-commit/pre-commit/issues/2970">#2970</a> issue by <a
  href="https://github.com/chriskuehl"><code>@​chriskuehl</code></a>.</li> </ul> </li> </ul>
  </blockquote> </details> <details> <summary>Commits</summary> <ul> <li><a
  href="https://github.com/pre-commit/pre-commit/commit/61cc55a59cc63c7405dd3cd7c96b169fdb750333"><code>61cc55a</code></a>
  v3.5.0</li> <li><a
  href="https://github.com/pre-commit/pre-commit/commit/c9945b9aa3d90113ad2bce4ab6648ef637edbf7c"><code>c9945b9</code></a>
  Merge pull request <a
  href="https://redirect.github.com/pre-commit/pre-commit/issues/3029">#3029</a> from
  adamchainz/improve_duration_timing</li> <li><a
  href="https://github.com/pre-commit/pre-commit/commit/d988767b414495bdab9ea24532ad337e8ee3fd1f"><code>d988767</code></a>
  Improve hook duration timing</li> <li><a
  href="https://github.com/pre-commit/pre-commit/commit/0d8b2451ca61d93c3d26746da83b63c7821c73f4"><code>0d8b245</code></a>
  Merge pull request <a
  href="https://redirect.github.com/pre-commit/pre-commit/issues/3023">#3023</a> from
  pre-commit/pre-commit-ci-update-config</li> <li><a
  href="https://github.com/pre-commit/pre-commit/commit/155c52134848b05b0092a446cdd2c336a03a85c0"><code>155c521</code></a>
  [pre-commit.ci] pre-commit autoupdate</li> <li><a
  href="https://github.com/pre-commit/pre-commit/commit/676e51aa5edd91fd8749ea4c7ebe65ac2609c5e9"><code>676e51a</code></a>
  Merge pull request <a
  href="https://redirect.github.com/pre-commit/pre-commit/issues/3024">#3024</a> from
  pre-commit/pick-shebang-path-without-spaces</li> <li><a
  href="https://github.com/pre-commit/pre-commit/commit/997ea0ad52074c3e6474f3d99f76f7965e2d05f0"><code>997ea0a</code></a>
  use sys.executable instead of echo.exe in parse_shebang</li> <li><a
  href="https://github.com/pre-commit/pre-commit/commit/19aa121db0e8e7f15dd88765735657e73f94e7a6"><code>19aa121</code></a>
  Merge pull request <a
  href="https://redirect.github.com/pre-commit/pre-commit/issues/3016">#3016</a> from
  pre-commit/pre-commit-ci-update-config</li> <li><a
  href="https://github.com/pre-commit/pre-commit/commit/a4ab977cc36e06fff8a8c69cca652162407b55cf"><code>a4ab977</code></a>
  [pre-commit.ci] pre-commit autoupdate</li> <li><a
  href="https://github.com/pre-commit/pre-commit/commit/3f3760b86c4e08de82d00b7ba55505f7d0656271"><code>3f3760b</code></a>
  Merge pull request <a
  href="https://redirect.github.com/pre-commit/pre-commit/issues/3011">#3011</a> from
  hack3ric/bump-node-and-go-version</li> <li>Additional commits viewable in <a
  href="https://github.com/pre-commit/pre-commit/compare/v3.3.3...v3.5.0">compare view</a></li>
  </ul> </details> <br />

[![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=pre-commit&package-manager=pip&previous-version=3.3.3&new-version=3.5.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

You can trigger a rebase of this PR by commenting `@dependabot rebase`.

[//]: # (dependabot-automerge-start) [//]: # (dependabot-automerge-end)

---

<details> <summary>Dependabot commands and options</summary> <br />

You can trigger Dependabot actions by commenting on this PR: - `@dependabot rebase` will rebase this
  PR - `@dependabot recreate` will recreate this PR, overwriting any edits that have been made to it
  - `@dependabot merge` will merge this PR after your CI passes on it - `@dependabot squash and
  merge` will squash and merge this PR after your CI passes on it - `@dependabot cancel merge` will
  cancel a previously requested merge and block automerging - `@dependabot reopen` will reopen this
  PR if it is closed - `@dependabot close` will close this PR and stop Dependabot recreating it. You
  can achieve the same result by closing it manually - `@dependabot show <dependency name> ignore
  conditions` will show all of the ignore conditions of the specified dependency - `@dependabot
  ignore this major version` will close this PR and stop Dependabot creating any more for this major
  version (unless you reopen the PR or upgrade to it yourself) - `@dependabot ignore this minor
  version` will close this PR and stop Dependabot creating any more for this minor version (unless
  you reopen the PR or upgrade to it yourself) - `@dependabot ignore this dependency` will close
  this PR and stop Dependabot creating any more for this dependency (unless you reopen the PR or
  upgrade to it yourself)

</details>

> **Note** > Automatic rebases have been disabled on this pull request as it has been open for over
  30 days.

- **deps-dev**: Bump pytest from 7.4.0 to 7.4.3
  ([`d9b122d`](https://github.com/Definedge-Securities/pyintegrate/commit/d9b122d9bf8bbfa5e5f09739c8c76a68fa9c8f2c))

Bumps [pytest](https://github.com/pytest-dev/pytest) from 7.4.0 to 7.4.3. - [Release
  notes](https://github.com/pytest-dev/pytest/releases) -
  [Changelog](https://github.com/pytest-dev/pytest/blob/main/CHANGELOG.rst) -
  [Commits](https://github.com/pytest-dev/pytest/compare/7.4.0...7.4.3)

--- updated-dependencies: - dependency-name: pytest dependency-type: direct:development

update-type: version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps-dev**: Bump pytest from 7.4.0 to 7.4.3
  ([#34](https://github.com/Definedge-Securities/pyintegrate/pull/34),
  [`2e263e6`](https://github.com/Definedge-Securities/pyintegrate/commit/2e263e6eb7a695465faa2703e4167c2af76747f7))

Bumps [pytest](https://github.com/pytest-dev/pytest) from 7.4.0 to 7.4.3. <details> <summary>Release
  notes</summary> <p><em>Sourced from <a
  href="https://github.com/pytest-dev/pytest/releases">pytest's releases</a>.</em></p> <blockquote>
  <h2>pytest 7.4.3 (2023-10-24)</h2> <h2>Bug Fixes</h2> <ul> <li> <p><a
  href="https://redirect.github.com/pytest-dev/pytest/issues/10447">#10447</a>: Markers are now
  considered in the reverse mro order to ensure base class markers are considered first -- this
  resolves a regression.</p> </li> <li> <p><a
  href="https://redirect.github.com/pytest-dev/pytest/issues/11239">#11239</a>: Fixed
  <code>:=</code> in asserts impacting unrelated test cases.</p> </li> <li> <p><a
  href="https://redirect.github.com/pytest-dev/pytest/issues/11439">#11439</a>: Handled an edge case
  where :data:<code>sys.stderr</code> might already be closed when :ref:<code>faulthandler</code> is
  tearing down.</p> </li> </ul> <h2>pytest 7.4.2 (2023-09-07)</h2> <h1>Bug Fixes</h1> <ul> <li>
  <p><a href="https://redirect.github.com/pytest-dev/pytest/issues/11237">#11237</a>: Fix doctest
  collection of <code>functools.cached_property</code> objects.</p> </li> <li> <p><a
  href="https://redirect.github.com/pytest-dev/pytest/issues/11306">#11306</a>: Fixed bug using
  <code>--importmode=importlib</code> which would cause package <code>__init__.py</code> files to be
  imported more than once in some cases.</p> </li> <li> <p><a
  href="https://redirect.github.com/pytest-dev/pytest/issues/11367">#11367</a>: Fixed bug where
  <code>user_properties</code> where not being saved in the JUnit XML file if a fixture failed
  during teardown.</p> </li> <li> <p><a
  href="https://redirect.github.com/pytest-dev/pytest/issues/11394">#11394</a>: Fixed crash when
  parsing long command line arguments that might be interpreted as files.</p> </li> </ul>
  <h1>Improved Documentation</h1> <ul> <li><a
  href="https://redirect.github.com/pytest-dev/pytest/issues/11391">#11391</a>: Improved disclaimer
  on pytest plugin reference page to better indicate this is an automated, non-curated listing.</li>
  </ul> <h2>pytest 7.4.1 (2023-09-02)</h2> <h2>Bug Fixes</h2> <ul> <li> <p><a
  href="https://redirect.github.com/pytest-dev/pytest/issues/10337">#10337</a>: Fixed bug where fake
  intermediate modules generated by <code>--import-mode=importlib</code> would not include the child
  modules as attributes of the parent modules.</p> </li> <li> <p><a
  href="https://redirect.github.com/pytest-dev/pytest/issues/10702">#10702</a>: Fixed error
  assertion handling in <code>pytest.approx</code> when <code>None</code> is an expected or received
  value when comparing dictionaries.</p> </li> <li> <p><a
  href="https://redirect.github.com/pytest-dev/pytest/issues/10811">#10811</a>: Fixed issue when
  using <code>--import-mode=importlib</code> together with <code>--doctest-modules</code> that
  caused modules to be imported more than once, causing problems with modules that have import side
  effects.</p> </li> </ul> </blockquote> </details> <details> <summary>Commits</summary> <ul> <li><a
  href="https://github.com/pytest-dev/pytest/commit/23906106968eb95afbd61adfbc7bbb795fc9aaa9"><code>2390610</code></a>
  Tweak changelog.rst</li> <li><a
  href="https://github.com/pytest-dev/pytest/commit/a0714aa0076f38e6fb8c7321e8bb4f5f33d1792d"><code>a0714aa</code></a>
  Prepare release version 7.4.3</li> <li><a
  href="https://github.com/pytest-dev/pytest/commit/44ad1c9811d2ebf540e601ea66b9bebf8ea82969"><code>44ad1c9</code></a>
  [7.4.x] fix <a href="https://redirect.github.com/pytest-dev/pytest/issues/10447">#10447</a> -
  consider marks in reverse mro order to give base classes...</li> <li><a
  href="https://github.com/pytest-dev/pytest/commit/5dc77253d439038ac64c55a5a48692ac3a53db2e"><code>5dc7725</code></a>
  [7.4.x] Ensure logging tests always cleanup after themselves (<a
  href="https://redirect.github.com/pytest-dev/pytest/issues/11541">#11541</a>)</li> <li><a
  href="https://github.com/pytest-dev/pytest/commit/a5178273183ddbda0ef4e4c6aa2b92aab086776b"><code>a517827</code></a>
  [7.4.x] Configure ReadTheDocs to fail on warnings (<a
  href="https://redirect.github.com/pytest-dev/pytest/issues/11540">#11540</a>)</li> <li><a
  href="https://github.com/pytest-dev/pytest/commit/21fe071d797612468fa18dd0ae4d6dbf49846b6d"><code>21fe071</code></a>
  [7.4.x] fix for ValueError raised in faulthandler teardown code (<a
  href="https://redirect.github.com/pytest-dev/pytest/issues/11455">#11455</a>)</li> <li><a
  href="https://github.com/pytest-dev/pytest/commit/f8bb8572fed8627946bfc82819d24b138d587257"><code>f8bb857</code></a>
  Force terminal width when running tests (<a
  href="https://redirect.github.com/pytest-dev/pytest/issues/11425">#11425</a>) (<a
  href="https://redirect.github.com/pytest-dev/pytest/issues/11432">#11432</a>)</li> <li><a
  href="https://github.com/pytest-dev/pytest/commit/1944dc06d39404ae9869b544dc2e2b482bf472e2"><code>1944dc0</code></a>
  [7.4.x] Fix --import-mode=importlib when root contains <code>__init__.py</code> file (<a
  href="https://redirect.github.com/pytest-dev/pytest/issues/1">#1</a>...</li> <li><a
  href="https://github.com/pytest-dev/pytest/commit/946634c84cf074a1ead10bdba56ddf3e5408e95c"><code>946634c</code></a>
  Merge pull request <a href="https://redirect.github.com/pytest-dev/pytest/issues/11419">#11419</a>
  from nicoddemus/backport-11414-to-7.4.x</li> <li><a
  href="https://github.com/pytest-dev/pytest/commit/d849a3ed64c6da63a0e3713892a7bfefdd56acaf"><code>d849a3e</code></a>
  [7.4.x] fix: closes <a
  href="https://redirect.github.com/pytest-dev/pytest/issues/11343">#11343</a>'s [attr-defined] type
  errors (<a href="https://redirect.github.com/pytest-dev/pytest/issues/11421">#11421</a>)</li>
  <li>Additional commits viewable in <a
  href="https://github.com/pytest-dev/pytest/compare/7.4.0...7.4.3">compare view</a></li> </ul>
  </details> <br />

[![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=pytest&package-manager=pip&previous-version=7.4.0&new-version=7.4.3)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

You can trigger a rebase of this PR by commenting `@dependabot rebase`.

[//]: # (dependabot-automerge-start) [//]: # (dependabot-automerge-end)

---

<details> <summary>Dependabot commands and options</summary> <br />

You can trigger Dependabot actions by commenting on this PR: - `@dependabot rebase` will rebase this
  PR - `@dependabot recreate` will recreate this PR, overwriting any edits that have been made to it
  - `@dependabot merge` will merge this PR after your CI passes on it - `@dependabot squash and
  merge` will squash and merge this PR after your CI passes on it - `@dependabot cancel merge` will
  cancel a previously requested merge and block automerging - `@dependabot reopen` will reopen this
  PR if it is closed - `@dependabot close` will close this PR and stop Dependabot recreating it. You
  can achieve the same result by closing it manually - `@dependabot show <dependency name> ignore
  conditions` will show all of the ignore conditions of the specified dependency - `@dependabot
  ignore this major version` will close this PR and stop Dependabot creating any more for this major
  version (unless you reopen the PR or upgrade to it yourself) - `@dependabot ignore this minor
  version` will close this PR and stop Dependabot creating any more for this minor version (unless
  you reopen the PR or upgrade to it yourself) - `@dependabot ignore this dependency` will close
  this PR and stop Dependabot creating any more for this dependency (unless you reopen the PR or
  upgrade to it yourself)

</details>

> **Note** > Automatic rebases have been disabled on this pull request as it has been open for over
  30 days.

- **deps-dev**: Bump python-semantic-release from 8.0.6 to 8.0.7
  ([`6976dbd`](https://github.com/Definedge-Securities/pyintegrate/commit/6976dbdd12957424b3ce35901c04ccb361b00234))

Bumps [python-semantic-release](https://github.com/python-semantic-release/python-semantic-release)
  from 8.0.6 to 8.0.7. - [Release
  notes](https://github.com/python-semantic-release/python-semantic-release/releases) -
  [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md)
  -
  [Commits](https://github.com/python-semantic-release/python-semantic-release/compare/v8.0.6...v8.0.7)

--- updated-dependencies: - dependency-name: python-semantic-release dependency-type:
  direct:development

update-type: version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps-dev**: Bump python-semantic-release from 8.0.6 to 8.0.7
  ([#8](https://github.com/Definedge-Securities/pyintegrate/pull/8),
  [`929f052`](https://github.com/Definedge-Securities/pyintegrate/commit/929f052a56c0b4138ddc15fcf4016f166b19461d))

Bumps [python-semantic-release](https://github.com/python-semantic-release/python-semantic-release)
  from 8.0.6 to 8.0.7. <details> <summary>Release notes</summary> <p><em>Sourced from <a
  href="https://github.com/python-semantic-release/python-semantic-release/releases">python-semantic-release's
  releases</a>.</em></p> <blockquote> <h1>v8.0.7 (2023-08-16)</h1> <h2>Fix</h2> <ul> <li>fix: use
  correct upload url for github (<a
  href="https://redirect.github.com/python-semantic-release/python-semantic-release/issues/661">#661</a>)</li>
  </ul> <p>Co-authored-by: github-actions &lt;<a
  href="mailto:action@github.com">action@github.com</a>&gt; (<a
  href="https://github.com/python-semantic-release/python-semantic-release/commit/8a515caf1f993aa653e024beda2fdb9e629cc42a"><code>8a515ca</code></a>)</p>
  </blockquote> </details> <details> <summary>Changelog</summary> <p><em>Sourced from <a
  href="https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md">python-semantic-release's
  changelog</a>.</em></p> <blockquote> <h2>v8.0.7 (2023-08-16)</h2> <h3>Fix</h3> <ul> <li>fix: use
  correct upload url for github (<a
  href="https://redirect.github.com/python-semantic-release/python-semantic-release/issues/661">#661</a>)</li>
  </ul> <p>Co-authored-by: github-actions &lt;<a
  href="mailto:action@github.com">action@github.com</a>&gt; (<a
  href="https://github.com/python-semantic-release/python-semantic-release/commit/8a515caf1f993aa653e024beda2fdb9e629cc42a"><code>8a515ca</code></a>)</p>
  </blockquote> </details> <details> <summary>Commits</summary> <ul> <li><a
  href="https://github.com/python-semantic-release/python-semantic-release/commit/3c7db14e7c1898bd4c1e748b3fa20a2d5eef3abe"><code>3c7db14</code></a>
  8.0.7</li> <li><a
  href="https://github.com/python-semantic-release/python-semantic-release/commit/8a515caf1f993aa653e024beda2fdb9e629cc42a"><code>8a515ca</code></a>
  fix: use correct upload url for github (<a

href="https://redirect.github.com/python-semantic-release/python-semantic-release/issues/661">#661</a>)</li>
  <li>See full diff in <a
  href="https://github.com/python-semantic-release/python-semantic-release/compare/v8.0.6...v8.0.7">compare
  view</a></li> </ul> </details> <br />

[![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=python-semantic-release&package-manager=pip&previous-version=8.0.6&new-version=8.0.7)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don't alter it yourself. You can
  also trigger a rebase manually by commenting `@dependabot rebase`.

[//]: # (dependabot-automerge-start) [//]: # (dependabot-automerge-end)

---

<details> <summary>Dependabot commands and options</summary> <br />

You can trigger Dependabot actions by commenting on this PR: - `@dependabot rebase` will rebase this
  PR - `@dependabot recreate` will recreate this PR, overwriting any edits that have been made to it
  - `@dependabot merge` will merge this PR after your CI passes on it - `@dependabot squash and
  merge` will squash and merge this PR after your CI passes on it - `@dependabot cancel merge` will
  cancel a previously requested merge and block automerging - `@dependabot reopen` will reopen this
  PR if it is closed - `@dependabot close` will close this PR and stop Dependabot recreating it. You
  can achieve the same result by closing it manually - `@dependabot show <dependency name> ignore
  conditions` will show all of the ignore conditions of the specified dependency - `@dependabot
  ignore this major version` will close this PR and stop Dependabot creating any more for this major
  version (unless you reopen the PR or upgrade to it yourself) - `@dependabot ignore this minor
  version` will close this PR and stop Dependabot creating any more for this minor version (unless
  you reopen the PR or upgrade to it yourself) - `@dependabot ignore this dependency` will close
  this PR and stop Dependabot creating any more for this dependency (unless you reopen the PR or
  upgrade to it yourself)

</details>

### Features

- Added BFO segment ([#42](https://github.com/Definedge-Securities/pyintegrate/pull/42),
  [`d4f6d3f`](https://github.com/Definedge-Securities/pyintegrate/commit/d4f6d3fb268870ba0b974bffdb6e40bf7234f68a))

Now orders can be placed for BFO segment from pyintegrate with this release.


## v1.0.2 (2023-08-14)

### Bug Fixes

- Update .readthedocs.yaml
  ([`6fb6334`](https://github.com/Definedge-Securities/pyintegrate/commit/6fb63348e671213a8994f675034c043aabd3cdd6))

Change path to conf.py


## v1.0.1 (2023-08-14)

### Bug Fixes

- Create requirements.txt for readthedocs
  ([`60fe01d`](https://github.com/Definedge-Securities/pyintegrate/commit/60fe01d176131e4b11e8ff0de32ee443e1eafdc1))


## v1.0.0 (2023-08-14)

### Chores

- Bump version to 1.0.0
  ([`79cf9e1`](https://github.com/Definedge-Securities/pyintegrate/commit/79cf9e15b22ef19e85c4630e238fff95ba7b599a))

BREAKING CHANGE: bump version to 1.0.0

### Breaking Changes

- Bump version to 1.0.0
