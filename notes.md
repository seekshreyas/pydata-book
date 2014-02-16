Python Notes
============

## Caveats / Notes

- Python Dictionary vs `defaultdict`
    - python dictionary will throw a `keyerror` if you try to get an item that isn't currently in the dictionary
    - `defaultdict` will create a new key if it doesn't exist.
        - `defaultdict(<type>)` where type can be `int`, `list` etc


## Snippets

| Task | Code |
|:-----|:-----|
| Load a __json__ file | `[json.loads(rec) for rec in records]` |
| __Dictionary__ to __List__ | `[(key, value) for key, value in count_dict.items()]` |
| Auto Reload modules in IPython | ``` %load_ext autoreload , %autoreload 2``` |
| create an numpy array | `np.arange(15).reshape(3,5)` or `np.random.randn(6,3)`|



