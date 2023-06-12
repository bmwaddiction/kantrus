module.exports = {
  'kratus-file': {
    input: {
      target: 'server/openapi.json',
    },
    output: {
      target: 'src/api/endpoints.ts',
      mode: 'split',
      schemas: 'src/api/model',
      client: 'react-query',
      prettier: true,
      tsconfig: true,
    },
  },
};
