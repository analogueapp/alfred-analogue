Analogue for Alfred [![CodeFactor](https://www.codefactor.io/repository/github/analogue-app/alfred-analogue/badge)](https://www.codefactor.io/repository/github/analogue-app/alfred-analogue)
==============

This workflow lets you manage your Analogue library with Alfred.

## Installation
- Download/Install Alfred 4
- Download lastest workflow (.alfredworkflow file) from the [releases](https://github.com/analogue-app/alfred-analogue/releases) page
- Open the `.alfredworkflow` file to import it into Alfred

## Features

- [X] Goto analogue.app via browser `analogue`
- [X] Add any URL to your library `analogue add {url}`
- [X] Search Analogue for people or content `analogue search {query}`
- [X] View to 10 entries in your library `analogue content`
- [X] Goto current user [your] profile `analogue profile`
- [X] Goto activity/notification page `analogue activity`
- [X] Goto user `analogue user rojo`
- [X] Create log `analogue add {link}`
- [X] Create a new collection `analogue create {title}`
- [X] Search Analogue for content `analogue search {query}`

## Todo
- [ ] Create a new collection `analogue create {title}`
- [ ] Goto collections `analogue col books`
- [ ] Feeling lucky (picks a random log off of analogue) `analogue random`
- [ ] Search your library `analogue content {query}`
- [ ] Give a book recommendation `analogue recommend book`
    - This could develop into other content types (shows, videos, etc)
- [ ] Create log `analogue add {link}` with type ahead
- [ ] Goto collections `analogue col books` with type ahead
- [ ] Navigate collections `analogue collection {query}`
    - returns autocomplete of your collections
    - Arrow key up/down to a collection
      - `Enter` to open browser to collection
      - `+ {url}` to add url to library and collection
- [ ] Uses OAuth 2.0 to authorize the workflow
- [ ] Saves your access_token securely in OS X's keychain


## Credits

This workflow is based on [alfred-pocket](https://github.com/fniephaus/alfred-pocket) and [alfred-workflow](https://github.com/deanishe/alfred-workflow).
