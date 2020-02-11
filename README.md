Analogue for Alfred
==============

This workflow lets you manage your Analogue library with Alfred.

## Features
- Access your Analogue profile
  - `analogue`
- Add any URL to your library
  - `analogue add {url}`
- Hotkey to add new links from Chrome, Safari or your clipboard 
  - `+` key (`SHIFT + '='`)
- Create a new collection 
  - `analogue create {title}`
- Search Analogue for people or content
  - `analogue search {query}`
- Search your library
  - `analogue content {query}`
- Navigate collections
  - `analogue collection {query}`
    - returns autocomplete of your collections
    - Arrow key up/down to a collection
      - `Enter` to open browser to collection
      - `+ {url}` to add url to library and collection
- Uses OAuth 2.0 to authorize the workflow
- Saves your access_token securely in OS X's keychain

## Todo

### Version 0.1
- [x] Set up repo and README
- [ ] Define feature set
- [ ] Create initial codebase based on [alfred-pocket](https://github.com/fniephaus/alfred-pocket)
- [ ] Integrate Analogue auth with [alfred-workflow](https://github.com/deanishe/alfred-workflow)
- [ ] Build `analogue` command to open profile
- [ ] Build `analogue add` command for adding URLs

## Credits

This workflow is based on [alfred-pocket](https://github.com/fniephaus/alfred-pocket) and [alfred-workflow](https://github.com/deanishe/alfred-workflow).
