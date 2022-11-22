# Mu Reasoner

Configurable reasoning service. A wrapper around the [EYE reasong engine](https://github.com/josd/eye) using the [mu-python-template](https://github.com/mu-semtech/mu-python-template) for [Semantic.works](https://semantic.works/).

## Configuration and usage

An example config is included in `config/knows`. This creats a preconfigured reasoning api under `/reason/knows` based on this [n3 tutorial](https://n3.restdesc.org/).

- `.n3`-files contain rules and data
- `.n3q`-files contain the query (optional). If no query files are provided, the full deductive closure will be returned

```
curl --location --request POST 'https://reasoner.dev.devloed.com/reason/knows' \
--form 'data="http://n3.restdesc.org/n3/friends.n3"'
```

## API

```
POST /reason/<path>

data=<uriReferencesOrTTl>
```

```
GET /reason/<path>?data=<uriReferencesOrTTl>
```

Data can be both
- by value (Turtle or Notation3)
- Comma separated URLs of TTL/N3 resources

The `<path>` is optional. When empty - all the data and rules have to be provided via the data parameter in the request.

## Alternatives
- [RubenVerborgh/EyeServer](https://github.com/RubenVerborgh/EyeServer/)
