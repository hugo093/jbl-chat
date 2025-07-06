const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const path = require("path");
const webpack = require('webpack')

module.exports = {
    target: 'web',
    context: path.resolve(__dirname),
    module: {
        rules: [
            {
                test: /.js?$/,
                loader: 'babel-loader',
                include: [path.join(__dirname, 'src/js')],
                options: {presets: [require.resolve('@babel/preset-env')]}
            },
            {
                test: /\.woff2?$/,
                type: "asset/resource",
            },
            {
                test: /\.css$/i,
                use: ['style-loader',
                    'css-loader']
            },
            {
                test: /\.s[ac]ss$/,
                use: [
                    MiniCssExtractPlugin.loader,
                    {loader: 'css-loader', options: {importLoaders: 1}},
                    "sass-loader"
                ]
            }
        ]
    },
    entry: {
        'global': {'import': path.join(__dirname, '/src/js/global.js')},
        'sign-in': {'import': path.join(__dirname, '/src/scss/sign-in.scss')},
        'dashboard': {'import': path.join(__dirname, '/src/scss/dashboard.scss')}
    },
    output: {
        path: path.join(__dirname, '/dist/js'),
        filename: '[name].js',
    },
    plugins: [
        // new MomentLocalesPlugin(),
        new MiniCssExtractPlugin({
            filename: '../css/[name].min.css'
        }),
        new webpack.ProvidePlugin({
            $: "jquery",
            jQuery: "jquery"
        })
    ]
}