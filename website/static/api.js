 $(document).ready(function() {
     var titleTrack = document.getElementById('trackInfo');

   var widget = SC.Widget(document.getElementById('soundcloud_widget'));
     widget.bind(SC.Widget.Events.READY, function() {
       //console.log('Ready...');
     });

   $('.play').click(function() {
       widget.play();
     $('.pause').show();
     $('.play').hide();
       titleTrack.textContent = "";
       widget.getCurrentSound(function(music){
            //alert(music.user.full_name);
        titleTrack.textContent += music.title + ' | ' + music.user.full_name ;
     });
   });


  $('.pause').click(function() {
     $('.pause').hide();
     $('.play').show();
       widget.pause();
     });


  $('.next').click(function() {
    titleTrack.textContent = "";
       widget.next();
    widget.getCurrentSound(function(music){
titleTrack.textContent += music.title + ' | ' + music.user.full_name ;
    });
   });

    $('.prev').click(function() {
    titleTrack.textContent = "";
       widget.prev();
    widget.getCurrentSound(function(music){
       titleTrack.textContent += music.title + ' | ' + music.user.full_name ;
     });
   });

    });
 $(document).ready(function() {
        var widget = SC.Widget(document.getElementById('soundcloud_widget'));
        widget.bind(SC.Widget.Events.READY, function() {
          console.log('Ready...');
        });

        $('play').click(function() {widget.toggle(); });

        $('next').click(function() {widget.next();  });

        $('prev').click(function() {widget.prev();  });
      });