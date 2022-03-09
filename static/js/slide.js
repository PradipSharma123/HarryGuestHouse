            var slideIndex = 0;
            showSlides();

            function showSlides() {
                var i;
                var slides = document.getElementsByClassName("mySlides");
                var dots = document.getElementsByClassName("dot");
                for (i = 0; i < slides.length; i++) {
                    slides[i].style.display = "none";
                }
                slideIndex++;
                if (slideIndex > slides.length) { slideIndex = 1 }
                for (i = 0; i < dots.length; i++) {
                    dots[i].className = dots[i].className.replace(" active", "");
                }
                slides[slideIndex - 1].style.display = "block";
                dots[slideIndex - 1].className += " active";
                setTimeout(showSlides, 3000); // Change image every 3 seconds
            }

// $(document).ready(function () {

//         $('.buttons').click(function () {

//             $(this).addClass('active').siblings().removeClass('active');

//             var filter = $(this).attr('data-filter')

//             if (filter == 'all') {
//                 $('.image').show(400);
//             } else {
//                 $('.image').not('.' + filter).hide(200);
//                 $('.image').filter('.' + filter).show(400);
//             }

//         });

//         $('.gallery').magnificPopup({

//             delegate: 'a',
//             type: 'image',
//             gallery: {
//                 enabled: true
//             }

//         });

//     });
    // End of GAllery page