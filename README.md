# Reasoning service

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

### Keep temporary files for debugging/development

When data is passed by value - i.e. passing triples as content vs passing an url referencing a ttl/n3 file - the data is stored as a tmp file before being passed to eye and by default cleaned up after the reasoning is done.

Use the `KEEP_TEMP_FILES` variable to prevent the automated cleanup:

```
    environment:
      KEEP_TEMP_FILES: "True"
    volumes:
      - ./config:/config
      - ./temp:/tmp
```

The temp files are also kept when running in development mode. cf [mu-python-template](https://github.com/mu-semtech/mu-python-template) for more info.

```
    environment:
      MODE: "development"
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
