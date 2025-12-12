export default {
  $schema: 'https://json.schemastore.org/prettierrc',
  printWidth: 100,
  tabWidth: 2,
  useTabs: false,
  semi: true,
  singleQuote: true,
  trailingComma: 'all',
  bracketSpacing: true,
  arrowParens: 'always',
  endOfLine: 'lf',
  proseWrap: 'preserve',
  overrides: [
    {
      files: ['*.md'],
      options: {
        proseWrap: 'preserve',
        embeddedLanguageFormatting: 'auto',
      },
    },
    {
      files: ['deploy/**/*.md'],
      options: {
        proseWrap: 'always',
        embeddedLanguageFormatting: 'auto',
      },
    },
    {
      files: ['*.yaml', '*.yml'],
      options: {
        singleQuote: false,
      },
    },
    {
      files: ['*.json', '*.jsonc'],
      options: {
        singleQuote: false,
      },
    },
  ],
  plugins: ['prettier-plugin-packagejson'],
};
