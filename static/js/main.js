function main() {

    (function () {
        'use strict';

        $('a.page-scroll').click(function () {
            if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
                var target = $(this.hash);
                target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
                if (target.length) {
                    $('html,body').animate({
                        scrollTop: target.offset().top - 40
                    }, 900);
                    return false;
                }
            }
        });


        // Show Menu on Book
        $(window).bind('scroll', function () {
            var navHeight = $(window).height() - 500;
            if ($(window).scrollTop() > navHeight) {
                $('.navbar-default').addClass('on');
            } else {
                $('.navbar-default').removeClass('on');
            }
        });

        $('body').scrollspy({
            target: '.navbar-default',
            offset: 80
        });

        // Hide nav on click
        $(".navbar-nav li a").click(function (event) {
            // check if window is small enough so dropdown is created
            var toggle = $(".navbar-toggle").is(":visible");
            if (toggle) {
                $(".navbar-collapse").collapse('hide');
            }
        });

        // Portfolio isotope filter
        $(window).load(function () {
            var $container = $('.portfolio-items');
            $container.isotope({
                filter: '*',
                animationOptions: {
                    duration: 750,
                    easing: 'linear',
                    queue: false
                }
            });
            $('.cat a').click(function () {
                $('.cat .active').removeClass('active');
                $(this).addClass('active');
                var selector = $(this).attr('data-filter');
                $container.isotope({
                    filter: selector,
                    animationOptions: {
                        duration: 750,
                        easing: 'linear',
                        queue: false
                    }
                });
                return false;
            });

        });

        // Nivo Lightbox
        $('.portfolio-item a').nivoLightbox({
            effect: 'slideDown',
            keyboardNav: true,
        });

    }());

    $(document).ready(function () {
        $('#alert-message').fadeOut(5000);
    });
}

main();

document.addEventListener('click', function(event) {
});

function showMessage(text) {
	let $item = $('<div class="alert alert-success" role="alert" id="alert-message">' + text + '</div>');
    $item.css("left", event.clientX - 100 + 'px');
    $item.css("top", event.clientY + 30 + 'px');
	$item.appendTo($('.message-box')).delay(1000).fadeToggle(450, function(){
	    $item.remove();
	});
}

function showCountCart(count) {
     let cartCount = document.getElementById('nav-cart-count');
     if (cartCount) {cartCount.textContent = count;}
}

function addToCart(url) {
    const textOk = "Добавлено в корзину!";
    let cartCount = document.getElementById('nav-cart-count');
    fetch(url).then(r => r.json()).then(r => showCountCart(r.count));
    showMessage(textOk);
}

const orderCreateButton = document.getElementById("order-form-button");

orderCreateButton.addEventListener("click", function (event) {
    const phone = document.getElementById("phone-number");
    const regex = /^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$/;
    if (!regex.test(phone.value)) {
    phone.setCustomValidity("Пожалуйста, введите номер телефона.");
  } else {
    phone.setCustomValidity("");
  }
});