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
    entry: './src/index.js',
    output: {
      path: path.resolve(__dirname, 'dist/spaces'),
      filename: 'bundle.js',
      publicPath: '/spaces/build'
    },
  };