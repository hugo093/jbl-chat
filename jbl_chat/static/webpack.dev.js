const common =  require("./webpack.common")
const {merge} = require('webpack-merge')
const BundleAnalyzerPlugin = require('webpack-bundle-analyzer').BundleAnalyzerPlugin;

module.exports = merge(common, {
    mode: 'development',
    devtool: 'inline-source-map',
    plugins: [
        ...common.plugins,
        new BundleAnalyzerPlugin({analyzerMode: 'static', reportFilename: 'reportCommon.html'})
    ]
})