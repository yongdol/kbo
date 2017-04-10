var links = [
'http://m.search.naver.com/search.naver?sm=mtb_drt&where=m&ie=utf8&query=%EC%95%BC%EA%B5%AC+%EA%B2%BD%EA%B8%B0',
'http://m.search.naver.com/search.naver?sm=mtb_hty.top&where=m&query=%EC%96%B4%EC%A0%9C+%EC%95%BC%EA%B5%AC+%EA%B2%B0%EA%B3%BC',
];
var casper = require(“casper”).create({
verbose: true,
loglevel: “debug”,
viewportSize: {
width:300,
height:200
}
});
casper.start().each(links, function(self, link, i) {
this.echo(“link: ” + link);
self.thenOpen(link, function() {
var title = this.getTitle();
this.echo(title);
var filename = '/Users/yongjoolim/project/django/kim/baseball/django_app/static/images/’ + i + ’_’ + title + ’.png’
this.captureSelector(filename, ’#ds_sports’);
});
});
casper.run();