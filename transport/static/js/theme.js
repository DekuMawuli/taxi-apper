(function($) {
    "use strict";

    if ($('.accrodion-grp').length) {
        var accrodionGrp = $('.accrodion-grp');
        accrodionGrp.each(function() {
            var accrodionName = $(this).data('grp-name');
            var Self = $(this);
            var accordion = Self.find('.accrodion');
            Self.addClass(accrodionName);
            Self.find('.accrodion .accrodion-content').hide();
            Self.find('.accrodion.active').find('.accrodion-content').show();
            accordion.each(function() {
                $(this).find('.accrodion-title').on('click', function() {
                    if ($(this).parent().hasClass('active') === false) {
                        $('.accrodion-grp.' + accrodionName).find('.accrodion').removeClass('active');
                        $('.accrodion-grp.' + accrodionName).find('.accrodion').find('.accrodion-content').slideUp();
                        $(this).parent().addClass('active');
                        $(this).parent().find('.accrodion-content').slideDown();
                    };


                });
            });
        });

    };

    if ($('ul.special-checkbox').length) {
        $('ul.special-checkbox').find('li').on('click', function() {
            $(this).toggleClass('active');
            $(this).find('input[type=checkbox]').prop('checked', function() {
                return !this.checked;
            });
        });
    };

    if ($('.counter').length) {
        $('.counter').counterUp({
            delay: 10,
            time: 3000
        });
    }

    if ($('.img-popup').length) {
        var groups = {};
        $('.img-popup').each(function() {
            var id = parseInt($(this).attr('data-group'), 10);

            if (!groups[id]) {
                groups[id] = [];
            }

            groups[id].push(this);
        });


        $.each(groups, function() {

            $(this).magnificPopup({
                type: 'image',
                closeOnContentClick: true,
                closeBtnInside: false,
                gallery: { enabled: true }
            });

        });

    }

    if ($('.main-navigation .navigation-box').length) {
        var subMenu = $('.main-navigation .sub-menu');
        subMenu.parent('li').children('a').append(function() {
            return '<button class="sub-nav-toggler"> <span class="sr-only">Toggle navigation</span> <span class="icon-bar"></span> <span class="icon-bar"></span> <span class="icon-bar"></span> </button>';
        });
        var mainNavToggler = $('.header-navigation .menu-toggler');
        var subNavToggler = $('.main-navigation .sub-nav-toggler');
        mainNavToggler.on('click', function() {
            var Self = $(this);
            var menu = Self.data('target');
            $(menu).slideToggle();
            $(menu).toggleClass('showen');
            return false;
        });
        subNavToggler.on('click', function() {
            var Self = $(this);
            Self.parent().parent().children('.sub-menu').slideToggle();
            return false;
        });
    }
    if ($('.video-popup').length) {
        $('.video-popup').magnificPopup({
            disableOn: 700,
            type: 'iframe',
            mainClass: 'mfp-fade',
            removalDelay: 160,
            preloader: true,

            fixedContentPos: false
        });
    }

    if ($('.banner-style-one').length) {
        $('.banner-style-one').owlCarousel({
            loop: true,
            items: 1,
            margin: 0,
            dots: true,
            nav: false,
            animateOut: 'slideOutDown',
            animateIn: 'fadeIn',
            active: true,
            smartSpeed: 1000,
            autoplay: 5000
        });
        $('.banner-carousel-btn .left-btn').on('click', function() {
            $('.banner-style-one').trigger('next.owl.carousel');
            return false;
        });
        $('.banner-carousel-btn .right-btn').on('click', function() {
            $('.banner-style-one').trigger('prev.owl.carousel');
            return false;
        });
    }

    if ($('.banner-style-two').length) {
        $('.banner-style-two').owlCarousel({
            loop: true,
            items: 1,
            margin: 0,
            dots: true,
            nav: false,
            animateOut: 'slideOutDown',
            animateIn: 'fadeIn',
            active: true,
            smartSpeed: 1000,
            autoplay: 5000
        });
        $('.banner-carousel-btn .left-btn').on('click', function() {
            $('.banner-style-two').trigger('next.owl.carousel');
            return false;
        });
        $('.banner-carousel-btn .right-btn').on('click', function() {
            $('.banner-style-two').trigger('prev.owl.carousel');
            return false;
        });
    }

    if ($('.brand-carousel-one').length) {
        $('.brand-carousel-one').owlCarousel({
            loop: true,
            margin: 10,
            nav: false,
            navText: [
                '<i class="fa fa-long-arrow-left"></i>',
                '<i class="fa fa-long-arrow-right"></i>'
            ],
            dots: false,
            autoWidth: false,
            autoplay: true,
            smartSpeed: 700,
            autoplayTimeout: 5000,
            autoplayHoverPause: true,
            responsive: {
                0: {
                    items: 1
                },
                480: {
                    items: 3
                },
                600: {
                    items: 3
                },
                991: {
                    items: 4
                },
                1000: {
                    items: 5
                },
                1200: {
                    items: 5
                }
            }
        });
    }
    if ($('.scroll-to-target').length) {
        $(".scroll-to-target").on('click', function() {
            var target = $(this).attr('data-target');
            // animate
            $('html, body').animate({
                scrollTop: $(target).offset().top
            }, 1000);

            return false;

        });
    }


    $(window).on('scroll', function() {
        if ($('.scroll-to-top').length) {
            var strickyScrollPos = 100;
            if ($(window).scrollTop() > strickyScrollPos) {
                $('.scroll-to-top').fadeIn(500);
            } else if ($(this).scrollTop() <= strickyScrollPos) {
                $('.scroll-to-top').fadeOut(500);
            }
        }
        if ($('.stricky').length) {
            var headerScrollPos = 100;
            var stricky = $('.stricky');
            if ($(window).scrollTop() > headerScrollPos) {
                stricky.removeClass('slideIn animated');
                stricky.addClass('stricky-fixed slideInDown animated');
            } else if ($(this).scrollTop() <= headerScrollPos) {
                stricky.removeClass('stricky-fixed slideInDown animated');
                stricky.addClass('slideIn animated');
            }
        }
    });
    $(window).on('load', function() {
        if ($('.preloader').length) {
            $('.preloader').fadeOut('slow');
        }

        if ($('.testimonials-slider-one').length) {
            var testiCarouselOne = $('.testimonials-slider-one').bxSlider({
                // adaptiveHeight: true,
                auto: true,
                controls: false,
                pause: 5000,
                speed: 500,
                pager: true,
                pagerCustom: '.testimonials-one-pager'
            });
            $('.testimonials-one-slider-btn .right-btn').on('click', function(e) {
                testiCarouselOne.goToNextSlide();
                e.preventDefault();
            });

            $('.testimonials-one-slider-btn .left-btn').on('click', function(e) {
                testiCarouselOne.goToPrevSlide();
                e.preventDefault();
            });
        }

        if ($('.history-slider-one').length) {
            var testiCarouselOne = $('.history-slider-one').bxSlider({
                // adaptiveHeight: true,
                auto: false,
                controls: false,
                pause: 5000,
                speed: 300,
                pager: false,
                onSlideAfter: function(currentSlideNumber, totalSlideQty, currentSlideHtmlObject) {
                    $('.history-content .pager-item').slideUp();
                    $('.history-content .pager-item').eq(currentSlideHtmlObject + 1).slideDown();
                },
                onSliderLoad: function() {
                    // $('.history-content .pager-item').slideUp();
                    $('.history-content .pager-item').eq(0).slideDown();
                }
            });
            $('.history-one-slider-btn .right-btn').on('click', function(e) {
                testiCarouselOne.goToNextSlide();
                e.preventDefault();
            });

            $('.history-one-slider-btn .left-btn').on('click', function(e) {
                testiCarouselOne.goToPrevSlide();
                e.preventDefault();
            });
        }
    });

})(jQuery);