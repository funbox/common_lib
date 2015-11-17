# common_lib #
A fork of http://oserl.hg.sourceforge.net/hgweb/oserl/common_lib/ that builds with rebar

### Usage with Rebar ###
Add following code to your rebar.conf:
```
{deps, [
  {common_lib, ".*", {git, "https://github.com/dmitrii-zolotarev/common_lib.git", {branch, "master"}}}
]}.
```

### Build ###
```
$ rebar compile
```
or
```
$ rebar co
```

### Run tests ###
```
$ rebar compile ct
```
or
```
$ rebar co ct
```
