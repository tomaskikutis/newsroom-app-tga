const config = require('newsroom-core/webpack.config');

config.devServer = {
    compress: true,
    disableHostCheck: true,
};

module.exports = config;
