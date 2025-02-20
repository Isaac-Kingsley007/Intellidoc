(function ($) {
    "use strict";

    // Force Hide Spinner on Load
    $(window).on('load', function () {
        $('#spinner').fadeOut("slow", function () {
            $(this).remove(); // Removes spinner from the DOM
        });
    });

    // If Spinner Stays Too Long, Hide it Anyway
    setTimeout(function () {
        $('#spinner').fadeOut("slow", function () {
            $(this).remove();
        });
    }, 3000); // 3-second fallback

    // Initiate wow.js animations
    new WOW().init();

    // Sticky Navbar - Adds shadow & sticks when scrolling
    $(window).scroll(function () {
        if ($(this).scrollTop() > 45) {
            $('.navbar').addClass('sticky-top shadow-sm');
        } else {
            $('.navbar').removeClass('sticky-top shadow-sm');
        }
    });

    // Back to Top Button - Shows when scrolling down
    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });

    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1000, 'easeInOutExpo');
        return false;
    });

    // Skills Progress Bar Animation (For Other Pages)
    if ($('.skill').length) {
        $('.skill').waypoint(function () {
            $('.progress .progress-bar').each(function () {
                $(this).css("width", $(this).attr("aria-valuenow") + '%');
            });
        }, {offset: '80%'});
    }

    // Counter Animation (For Other Pages)
    if ($('[data-toggle="counter-up"]').length) {
        $('[data-toggle="counter-up"]').counterUp({
            delay: 10,
            time: 2000
        });
    }

    // Testimonials Carousel (For Other Pages)
    if ($(".testimonial-carousel").length) {
        $(".testimonial-carousel").owlCarousel({
            autoplay: true,
            smartSpeed: 1000,
            margin: 25,
            dots: false,
            loop: true,
            nav: true,
            navText: [
                '<i class="bi bi-chevron-left"></i>',
                '<i class="bi bi-chevron-right"></i>'
            ],
            responsive: {
                0: { items: 1 },
                992: { items: 2 }
            }
        });
    }

    // Portfolio Isotope Filtering (For Other Pages)
    if ($('.portfolio-container').length) {
        var portfolioIsotope = $('.portfolio-container').isotope({
            itemSelector: '.portfolio-item',
            layoutMode: 'fitRows'
        });

        $('#portfolio-flters li').on('click', function () {
            $("#portfolio-flters li").removeClass('active');
            $(this).addClass('active');
            portfolioIsotope.isotope({ filter: $(this).data('filter') });
        });
    }

})(jQuery);
