# common_lib

A fork of http://oserl.hg.sourceforge.net/hgweb/oserl/common_lib/ that builds with Rebar.

## Usage with Rebar

Add following code to your rebar.conf:

```erlang
{deps, [
  {common_lib, ".*", {git, "https://github.com/dmitrii-zolotarev/common_lib.git", {branch, "master"}}}
]}.
```

## Build

```bash
rebar compile
```

or

```bash
rebar co
```

## Run tests

```bash
rebar compile ct
```

or

```bash
rebar co ct
```
