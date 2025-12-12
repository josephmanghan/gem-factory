import eslintConfigPrettier from 'eslint-config-prettier/flat';
import yml from 'eslint-plugin-yml';

export default [
  // Global ignores for files/folders that should not be linted
  {
    ignores: ['node_modules/**', '.claude/**', '.cursor/**', '.history/**'],
  },

  // YAML files configuration
  {
    files: ['**/*.{yaml,yml}'],
  },

  // YAML linting
  ...yml.configs['flat/recommended'],

  // Place Prettier last to disable conflicting stylistic rules
  eslintConfigPrettier,

  // Project-specific rules
  {
    rules: {
      // Allow console for CLI tools and scripts in this repo
      'no-console': 'off',
      // Enforce .yaml file extension for consistency
      'yml/file-extension': [
        'error',
        {
          extension: 'yaml',
          caseSensitive: true,
        },
      ],
      // Prefer double quotes in YAML wherever quoting is used, but allow single to avoid escapes
      'yml/quotes': [
        'error',
        {
          prefer: 'double',
          avoidEscape: true,
        },
      ],
    },
  },

  // GitHub workflow files may use empty mapping values intentionally
  {
    files: ['.github/**/*.yaml'],
    rules: {
      'yml/no-empty-mapping-value': 'off',
    },
  },
];
