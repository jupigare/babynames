jQuery(document).ready(function ($) {

  var jssor_1_options = {
    $AutoPlay: true,
    $AutoPlaySteps: 1,
    $SlideDuration: 2000,
    $SlideWidth: 300,
    $SlideHeight: 300,
    $SlideSpacing: 3,
    $Cols: 3,
    $ArrowNavigatorOptions: {
      $Class: $JssorArrowNavigator$,
      $Steps: 1
    },
    $BulletNavigatorOptions: {
      $Class: $JssorBulletNavigator$,
      $SpacingX: 1,
      $SpacingY: 1
    }
  };

  var jssor_1_slider = new $JssorSlider$("jssor_1", jssor_1_options);
});