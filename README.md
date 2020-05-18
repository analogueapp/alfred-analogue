Analogue for Alfred [![CodeFactor](https://www.codefactor.io/repository/github/analogue-app/alfred-analogue/badge)](https://www.codefactor.io/repository/github/analogue-app/alfred-analogue)
==============
i
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

V1 - Basics
- [ ] Goto analogue front page `analogue`
- [ ] Goto analogue feed `analogue feed`
- [ ] Goto current user [your] profile `analogue profile`
- [ ] Goto activity/notification page `analogue activity`
- [ ] Goto collections `analogue col books`
- [ ] Goto user `analogue user rojo`
- [ ] Create log `analogue add {link}`
- [ ] Create a new collection `analogue create {title}`
- [ ] Search Analogue for people or content `analogue search {query}`
- [ ] Search your library `analogue content {query}`

V2 - Fun

- [ ] Feeling lucky (picks a random log off of analogue) `analogue random`
- [ ] Give a book recommendation `analogue recommend book`
    - This could develop into other content types (shows, videos, etc)
- [ ] Create log `analogue add {link}` with type ahead
- [ ] Goto collections `analogue col books` with type ahead
- [ ] Navigate collections
  - `analogue collection {query}`
    - returns autocomplete of your collections
    - Arrow key up/down to a collection
      - `Enter` to open browser to collection
      - `+ {url}` to add url to library and collection
- [ ] Uses OAuth 2.0 to authorize the workflow
- [ ] Saves your access_token securely in OS X's keychain

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
