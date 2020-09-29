var urls = [];
var total = 0;
var maxImage = 10;
var interval = 1000;
console.log('crawling...');
var crawl = setInterval(() => {
    if (total < maxImage) {
        var div = document.querySelectorAll('div.qdnLaf.isv-id');
        if (div.length === 2) {
            var src = div[0].childNodes[1].firstElementChild.firstElementChild.src;
            if (urls.indexOf(src) < 0) {
                urls.push(src);
                console.log('adding...');
            }
            div[0].childNodes[0].lastElementChild.click();
        }
        if (div.length === 3) {
            var src = div[1].childNodes[1].firstElementChild.firstElementChild.src;
            if (urls.indexOf(src) < 0) {
                urls.push(src);
                console.log('adding...');
            }
            div[1].childNodes[0].lastElementChild.click();
        }
        total++;
    }
    else {
        clearInterval(crawl);

        console.log('saving....');
        var content = urls.join('\n\n');

        var hiddenElement = document.createElement('a');
        hiddenElement.href = 'data:attachment/text,' + encodeURI(content);
        hiddenElement.target = '_blank';
        hiddenElement.download = 'urls.txt';
        hiddenElement.click();

        console.log('saved');
    }
}, interval);