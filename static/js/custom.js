var scrollingTo = function(divString){
    $('html, body').animate({scrollTop: $(divString).offset().top}, 1000);
};