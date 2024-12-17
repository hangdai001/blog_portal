$(document).ready(function () {
  // Show the overlay when the "View" button is clicked
  $("[unique-script-id='w-w-dm-id'] .btn-box .btn").click(function () {
    $(this).closest(".project").find(".overlay").fadeIn(300);
  });

  // Hide the overlay when the "Close" button is clicked
  $("[unique-script-id='w-w-dm-id'] .close").click(function () {
    $(this).closest(".overlay").fadeOut(300);
  });

  // Filter functionality for project images
  $("[unique-script-id='w-w-dm-id'] .list").click(function () {
    const value = $(this).attr("data-filter");

    if (value === "all") {
      $("[unique-script-id='w-w-dm-id'] .squareImg").fadeIn(300);
    } else {
      $("[unique-script-id='w-w-dm-id'] .squareImg")
        .not("." + value)
        .fadeOut(300);
      $("[unique-script-id='w-w-dm-id'] .squareImg")
        .filter("." + value)
        .fadeIn(300);
    }

    // Add 'active' class to the clicked list item and remove it from siblings
    $(this).addClass("active").siblings().removeClass("active");
  });
});


<div id="carouselExampleControls" class="carousel slide overlay" data-ride="carousel">
  <div class="carousel-inner overlay-inner">
    <div class="carousel-item active">
      <img class="d-block w-100" src="..." alt="First slide">
    </div>
  </div>
  <a class="carousel-control-prev" href="#carouselExampleControls" role="button" data-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="carousel-control-next" href="#carouselExampleControls" role="button" data-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div>

<div class="project">
          <img class="squareImg three" src="https://workik-widget-assets.s3.amazonaws.com/widget-assets/images/d78.png">
          <div class="overlay">
            <div class="overlay-inner">
              <button class="close">
                Close X
              </button>
              <div class="hdImgs">
                <img alt="" class="againImg" src="https://workik-widget-assets.s3.amazonaws.com/widget-assets/images/d78.png">
              </div>
            </div>
          </div>
          <div class="btn-box">
            <button class="btn">
              View
            </button>
          </div>
        </div>