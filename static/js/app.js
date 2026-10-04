const mobileMenuBtn = document.querySelector(".mobile-menu-btn");
const sidebar = document.querySelector(".sidebar");

if (mobileMenuBtn) {
    mobileMenuBtn.addEventListener("click", () => {
        sidebar.classList.toggle("show");
    });
}
/* =====================================================
   DARK / LIGHT MODE
===================================================== */

const themeToggle = document.getElementById("themeToggle");
const themeIcon = document.getElementById("themeIcon");


// Load saved theme
const savedTheme = localStorage.getItem("chargehub-theme");

if (savedTheme === "dark") {
    document.body.classList.add("dark-mode");

    if (themeIcon) {
        themeIcon.classList.remove("bi-moon-fill");
        themeIcon.classList.add("bi-sun-fill");
    }
}


// Toggle theme
if (themeToggle) {

    themeToggle.addEventListener("click", () => {

        document.body.classList.toggle("dark-mode");

        const isDark =
            document.body.classList.contains("dark-mode");


        if (isDark) {

            localStorage.setItem(
                "chargehub-theme",
                "dark"
            );

            themeIcon.classList.remove(
                "bi-moon-fill"
            );

            themeIcon.classList.add(
                "bi-sun-fill"
            );

        } else {

            localStorage.setItem(
                "chargehub-theme",
                "light"
            );

            themeIcon.classList.remove(
                "bi-sun-fill"
            );

            themeIcon.classList.add(
                "bi-moon-fill"
            );
        }

    });

}
/* =========================================================
   EV CHARGING VIDEO
========================================================= */

document.addEventListener("DOMContentLoaded", function () {

    const watchVideoBtn =
        document.getElementById("watchVideoBtn");

    const closeVideoBtn =
        document.getElementById("closeVideoBtn");

    const videoModal =
        document.getElementById("evVideoModal");

    const video =
        document.getElementById("evChargingVideo");


    if (!watchVideoBtn || !videoModal || !video) {
        return;
    }


    /* OPEN VIDEO */

    watchVideoBtn.addEventListener("click", function () {

        videoModal.classList.add("active");

        video.currentTime = 0;

        video.play().catch(function () {
            // Browser may require manual play
        });

        document.body.style.overflow = "hidden";
    });


    /* CLOSE VIDEO */

    function closeVideo() {

        video.pause();

        video.currentTime = 0;

        videoModal.classList.remove("active");

        document.body.style.overflow = "";
    }


    closeVideoBtn.addEventListener(
        "click",
        closeVideo
    );


    /* CLICK OUTSIDE VIDEO */

    videoModal.addEventListener(
        "click",
        function (event) {

            if (event.target === videoModal) {

                closeVideo();
            }
        }
    );


    /* ESC KEY */

    document.addEventListener(
        "keydown",
        function (event) {

            if (
                event.key === "Escape" &&
                videoModal.classList.contains("active")
            ) {

                closeVideo();
            }
        }
    );

});