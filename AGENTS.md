# Gem Factory

In Gem Factory, you write and create Gemini gems following architectural and style guidelines.

## Documentation

> ⚠️ **MUST READ**

See [docs/index.md](./docs/index.md) for platform overview, architecture, and style guide.

## Creating Gems

New gems are created in the `gems/` directory. Follow the structure defined in [Architecture](./docs/architecture.md).

## Validation

Run `npm run pr` to format, lint, and validate all changes.

## Versioning

`*.package.yaml` files should reflect the three most recent releases from the Gem's `CHANGELOG`. When bumping versions, add the newest release at the top of the `release-notes` list and update the top-level `version` and `release-date` fields accordingly.
