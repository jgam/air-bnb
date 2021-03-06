const gulp = require('gulp');

const css = () => {
  const postCSS = require('gulp-postcss');
  const sass = require('gulp-sass');
  const minify = require('gulp-csso');
  sass.compiler = require('node-sass');
  //from assets.../ styles.css, we will pipe with all these
  //then put it in static/css as our newly created css file
  return gulp
    .src('assets/scss/styles.scss')
    .pipe(sass().on('error', sass.logError))
    .pipe(postCSS([require('tailwindcss'), require('autoprefixer')]))
    .pipe(minify())
    .pipe(gulp.dest('static/css'));
};

exports.default = css;

// static file will never be changed
// npm run css finally udpates the css file in css
