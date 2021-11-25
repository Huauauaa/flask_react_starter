const path = require('path');
const { PROXY } = process.env;

module.exports = {
  assetsDir: process.env.NODE_ENV === 'production' ? '../static' : 'static',
  publicPath: process.env.NODE_ENV === 'production' ? './' : '/',
  outputDir: path.resolve(__dirname, '../backend/templates'),
  devServer: {
    proxy: {
      '/api': {
        target: PROXY || 'http://127.0.0.1:5000',
        changeOrigin: true,
        pathRewrite: { '^/api': '/api' },
      },
    },
  },
};
