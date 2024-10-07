module.exports = {
    // ... other configurations
    module: {
      rules: [
        {
          test: /\.py$/,
          use: 'raw-loader',
        },
      ],
    },
  };