# Mu Reasoner

Configurable reasoning service. A wrapper around the [EYE reasong engine](https://github.com/josd/eye) using the [mu-python-template](https://github.com/mu-semtech/mu-python-template) for [mu.semte.ch](http://mu.semte.ch)-microservices.

## Configuration and usage

An example config is included in `config/knows`. This creats a preconfigured reasoning api under `/reason/knows` based on this [n3 tutorial](https://n3.restdesc.org/).

- `.n3`-files contain rules and data
- `.n3q`-files contain the query (optional). If no query files are provided, the full deductive closure will be returned

```
curl --location --request POST 'https://reasoner.dev.devloed.com/reason/knows' \
--form 'data="http://n3.restdesc.org/n3/friends.n3"'
```

Or

```
curl --location --request POST 'https://reasoner.dev.devloed.com/reason/knows' \
--form 'data="@prefix ppl: <http://example.org/people#>.
@prefix foaf: <http://xmlns.com/foaf/0.1/>.

ppl:Cindy foaf:knows ppl:John.
ppl:Cindy foaf:knows ppl:Eliza.
ppl:Cindy foaf:knows ppl:Kate.
ppl:Eliza foaf:knows ppl:John.
ppl:Peter foaf:knows ppl:John."'
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
